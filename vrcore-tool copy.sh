#!/bin/bash
## vrcore-tool [general-opts] <command> [command-args]
##
## Tool version: 0.9
##
## General options (must appear before command):
##
##    -s <device>
##        specifies the device serial number to pass to adb commands (useful
##        when more than one device is connected).
##
## Available commands:
##    info
##        print information about VrCore (version, etc).
##    install
##        Installs VrCore into /system/app
##    install-fast
##        Installs VrCore into /system/app without disabling verity (in case
##            you already have or are on an eng build)
##    sim-nfc
##        Simulates scanning of the Bandana NFC tag.
##    remove
##        removes VrCore from the system image.
##    set-oobe (true|false)
##        Sets the "Ithaca setup complete" flag.
##    set-skip-don (true|false)
##        Sets the "Skip DON flow" preference.
##    set-perf-mon (true|false)
##        Sets the "Enable performance monitoring" preference.
##    set-use-gvr-platform-library (true|false)
##        Sets the "Enable GVR platform library" preference.
##    settings
##        Launches the VrCore settings screen.
##    metaworld
##        Launches the VrCore VR metaworld screen ("QuickSettings").
##    unpair
##        Unpairs the controller.
##    list-prefs
##        Prints the preferences file.
##    edit-prefs
##        Opens an editor (uses $EDITOR) to edit the preferences file.
##    reset-prefs
##        Completely resets the VrCore preferences file.
##    kill
##        Kills VrCore.
##    logcat
##        Shows VrCore logcat.
##    gconfig-set <key> <value>
##        Sets a GConfig override.
##        For a list of the GConfig flags supported by VrCore, see:
##            //java/com/google/vr/vrcore/application/GConfigManager.java
##    gconfig-unset <key>
##        Unsets a GConfig override.
##    gconfig-list
##        List the GConfig values and overrides currently on the device.
##    gconfig-wipe
##        Wipe the GConfig value cache and overrides.
##
## Note: by default the version of adb on the PATH is used; to override,
## export the ADB variable to point to your preferred ADB binary.

ADB=${ADB:=adb}
PREFS_FILE=/data/data/com.google.vr.vrcore/shared_prefs/VrCoreSettings.xml
declare -a ADB_FLAGS
GCONFIG_DB_FILE=/data/data/com.google.android.gms/databases/config.db

function print_help() {
  grep '^##' "$0" | cut -c 4-
}

function main_menu() {
  if [ "$1" = "-s" ]; then
    if [ -z "$2" ]; then
      print_help
      exit 1
    fi
    echo "Using device: $2"
    ADB_FLAGS+=(-s "$2")
    shift
    shift
  fi

  case "$1" in
    info) do_info ;;
    remove) do_remove ;;
    install) do_install "$2" "false" ;;
    install-fast) do_install "$2" "true" ;;
    sim-nfc) do_sim_nfc ;;
    set-oobe) do_set_oobe "$2" ;;
    set-skip-don) do_set_skip_don "$2" ;;
    set-perf-mon) do_set_perf_mon "$2" ;;
    set-use-gvr-platform-library) do_set_use_gvr_platform_library "$2" ;;
    settings) do_settings ;;
    metaworld) do_metaworld ;;
    unpair) do_unpair ;;
    kill) do_kill ;;
    list-prefs) do_list_prefs ;;
    edit-prefs) do_edit_prefs ;;
    reset-prefs) do_reset_prefs ;;
    logcat) do_logcat ;;
    gconfig-set) do_gconfig set "$2" "$3" ;;
    gconfig-unset) do_gconfig unset "$2" ;;
    gconfig-list) do_gconfig_list ;;
    gconfig-wipe) do_gconfig_wipe ;;
    *)
      # Print help and quit.
      print_help
      exit 1
      ;;
  esac
}

function check_adb() {
  echo "Checking your ADB version."
  if ! "$ADB" 2>&1 | grep -q enable-verity; then
    echo "*** Your adb version doesn't support enabling/disabling verity."
    echo "*** Make sure the right adb is in your PATH."
    echo "*** The one we're using is at:"
    type "$ADB"
    echo
    echo "*** You need to update adb to at least version 1.0.32."
    echo "*** To do that on Goobuntu, either install a more recent version"
    echo "*** of the Android SDK (more specifically, the 'platform tools'"
    echo "*** component needs to be updated). Or, if you prefer, you can"
    echo "*** try to update adb directly on your Goobuntu machine:"
    echo "***"
    echo "***     sudo apt-get remove android-tools-adb"
    echo "***     sudo goobuntu-add-repo -r adb stable"
    echo "***     sudo apt-get update"
    echo "***     sudo apt-get install adb"
    echo "***"
    echo "*** Note: Your mileage may vary. This info came from this doc:"
    echo "*** https://docs.google.com/document/d/1p0dt4gzWB91AiVz-qE7CYjvRApmSZgEWzS8TUwkRl-M/edit#"
    echo
    exit 1
  fi
  echo "ADB version ok."
  echo
}

function reboot_and_wait_for_system_ready() {
  run_command "$ADB ${ADB_FLAGS[*]} reboot"
  echo -n "Waiting for device to reboot..."
  run_command "$ADB ${ADB_FLAGS[*]} wait-for-device"
  run_command "$ADB ${ADB_FLAGS[*]} root"
  run_command "$ADB ${ADB_FLAGS[*]} remount"
  echo
  echo -n "Waiting for system to finish starting up..."
  while true; do
    if "$ADB" "${ADB_FLAGS[@]}" shell getprop sys.boot_completed | \
        grep "1" > /dev/null; then
      echo "Done.";
      break
    else
      echo -n ".";
      sleep 1;
    fi
  done
}

function disable_verity() {
  echo
  echo "Disabling verity on your device. This may take a while and will"
  echo "require a device reboot."
  echo
  echo "*** DO NOT DISCONNECT OR DO ANYTHING ON YOUR DEVICE"
  echo "*** UNTIL THIS SCRIPT ENDS."
  echo
  run_command "$ADB ${ADB_FLAGS[*]} root"
  # Must enable verity and then disable (this works around a bug).
  run_command "$ADB ${ADB_FLAGS[*]} enable-verity"
  run_command "$ADB ${ADB_FLAGS[*]} disable-verity"
  reboot_and_wait_for_system_ready
}

function get_approval() {
  local ans
  echo -n "Do you wish to proceed? [y/N] "
  read ans
  if [[ "$ans" != "y" && "$ans" != "Y" ]]; then
    echo "*** Aborted."
    exit 1
  fi
}

function do_remove() {
  check_adb
  echo "This will remove VrCore from the system image of your device. If you"
  echo "are trying to replace the existing VrCore on your device, use install"
  echo "instead to preserve permissions."
  echo
  get_approval
  disable_verity
  run_command "$ADB ${ADB_FLAGS[*]} shell rm -rf /system/app/GoogleVrCore"
  run_command "$ADB ${ADB_FLAGS[*]} uninstall com.google.vr.vrcore"
  run_command \
      "$ADB ${ADB_FLAGS[*]} shell rm -rf /data/data/com.google.vr.vrcore"
  run_command "$ADB ${ADB_FLAGS[*]} reboot"
  echo "Done."
}

function do_install() {
  check_adb
  local PACKAGE="$1"
  local FAST_INSTALL="$2"
  if [[ ! -e "$PACKAGE" ]]; then
    echo "*** You must specify a VrCore package to install."
    exit 1
  fi
  echo "This will replace VrCore on the system image of your device. You ONLY"
  echo "need to run this command if you are replacing the default prod version"
  echo "of VrCore with a dev version (e.g., after freshly flashing a device)"
  echo "or if replacing a dev version with a signed prod version."
  echo
  echo "After you have run this command, you can just adb install normally as"
  echo "long as you continue to use the same type (dev or prod) of VrCore."
  echo
  get_approval
  if [[ "$FAST_INSTALL" != "true" ]]; then
    disable_verity
  else
    run_command "$ADB ${ADB_FLAGS[*]} root"
    run_command "$ADB ${ADB_FLAGS[*]} remount"
  fi
  local LOCAL_PACKAGE="/system/app/GoogleVrCore/GoogleVrCore.apk"
  run_command "$ADB ${ADB_FLAGS[*]} push $PACKAGE $LOCAL_PACKAGE"
  # We have to reboot before installing for Android to accept the signature and
  # retain all permissions.
  reboot_and_wait_for_system_ready
  run_command "$ADB ${ADB_FLAGS[*]} shell pm install -r -d $LOCAL_PACKAGE"
  local INSTALLED_SYS_PACKAGES=$("${ADB}" "${ADB_FLAGS[@]}" shell pm list packages -s)
  if [[ "$INSTALLED_SYS_PACKAGES" = *"package:com.google.vr.vrcore"* ]]; then
    echo "Done."
  else
    local INSTALLED_PACKAGES="$("${ADB}" "${ADB_FLAGS[@]}" shell pm list packages)"
    if [[ "$INSTALLED_PACKAGES" = *"package:com.google.vr.vrcore"* ]]; then
      echo "*** VrCore is installed, but not as a system package."
    else
      echo "*** VrCore does not appear to be installed, something went wrong!"
    fi
  fi
}

function do_info() {
  echo "[ VRCORE PACKAGE INFO ]"
  if ! "$ADB" "${ADB_FLAGS[@]}" shell pm dump com.google.vr.vrcore | \
      sed -n '/Package .com.google.vr.vrcore/,/^ *$/p' ; then
    echo "*** Error getting package info."
  fi
  echo
  echo "[ VRCORE PREFS FILE ]"
  if ! "$ADB" "${ADB_FLAGS[@]}" shell cat $PREFS_FILE; then
    echo "*** Error getting prefs file."
  fi
}

function do_sim_nfc() {
  echo "Simulating Bandana NFC scan."
  "$ADB" "${ADB_FLAGS[@]}" shell am start -a \
      com.google.vr.vrcore.SIM_NFC_SCANNED -c android.intent.category.DEFAULT
}

function do_set_oobe() {
  if [ "$1" != "true" -a "$1" != "false" ]; then
    echo "*** Value must be true or false."
    exit 1
  fi
  replace_pref "boolean" "DaydreamSetupComplete" "$1"
}

function do_set_skip_don() {
  if [ "$1" != "true" -a "$1" != "false" ]; then
    echo "*** Value must be true or false."
    exit 1
  fi
  replace_pref "boolean" "VrSkipDon" "$1"
}

function do_set_perf_mon() {
  if [ "$1" != "true" -a "$1" != "false" ]; then
    echo "*** Value must be true or false."
    exit 1
  fi
  replace_pref "boolean" "EnablePerformanceMonitoring" "$1"
}

function do_set_use_gvr_platform_library() {
  if [ "$1" != "true" -a "$1" != "false" ]; then
    echo "*** Value must be true or false."
    exit 1
  fi
  replace_pref "boolean" "EnableGvrPlatformLibrary" "$1"
}

function do_settings() {
  echo "Launching VrCore settings..."
  "$ADB" "${ADB_FLAGS[@]}" shell am start -n com.google.vr.vrcore/com.google.vr.vrcore.settings.VrSettingsActivity
}

function do_metaworld() {
  echo "Launching VrCore metaworld..."
  "$ADB" "${ADB_FLAGS[@]}" shell am start -n com.google.vr.vrcore/com.google.vr.vrcore.daydream.MetaworldActivity
}

function do_unpair() {
  delete_pref PairedControllerAddress
  delete_pref PairedControllerDriver
  delete_pref PairedControllerFirmwareVersion
}

function do_kill() {
  echo "Attempting to kill VrCore."
  "$ADB" "${ADB_FLAGS[@]}" shell am force-stop com.google.vr.vrcore
}

function do_logcat() {
  echo "Showing VrCore logcat."
  local pkg=com.google.vr.vrcore
  echo "Looking for VrCore process..."
  while true; do
    line=$("$ADB" "${ADB_FLAGS[@]}" shell ps | sed "s,\r,," | grep "$pkg$")
    if [ -n "$line" ]; then
      pid=$(echo "$line" | tr -s ' ' ' ' | cut -d ' ' -f2)
      if [ -z "$pid" ]; then
        echo "*** Failed to parse PID from ps line:"
        echo "$line"
        exit 2
      fi
      echo
      echo "Found process: PID = $pid"
      break
    fi
    echo -n "."
    sleep 1
  done

  "$ADB" "${ADB_FLAGS[@]}" logcat -v brief | \
      grep --line-buffered -E "\( *$pid *\)" | while read line; do
    case "$line" in
      I/*)
        echo -ne "\e[2m"
        ;;
      W/*)
        echo -ne "\e[1;33m"
        ;;
      E/*)
        echo -ne "\e[1;31m"
        ;;
      D/*)
        echo -ne "\e[32m"
        ;;
    esac
    echo -e "$line\e[0m";
  done
}

function do_list_prefs() {
  "$ADB" "${ADB_FLAGS[@]}" shell cat "$PREFS_FILE"
}

function do_edit_prefs() {
  ensure_prefs_file_exists_or_die

  local TMPFILE=/tmp/vrcore-tool-$$
  local TMPFILE2=/tmp/vrcore-tool-$$-B

  rm -rf $TMPFILE
  if ! "$ADB" "${ADB_FLAGS[@]}" pull $PREFS_FILE \
      $TMPFILE; then
    echo "*** Failed to adb pull the prefs file."
    rm -f $TMPFILE $TMPFILE2
    exit 1
  fi

  if [ -z "$EDITOR" ]; then
    if type nano; then
      EDITOR=nano
    elif type vim; then
      EDITOR=vim
    elif type vi; then
      EDITOR=vi
    else
      echo "*** No editor found. Set the EDITOR environment variable."
      exit 1
      rm -f $TMPFILE $TMPFILE2
    fi
  fi

  if [ -n "$EDITOR" ]; then
    echo "Invoking editor ($EDITOR)..."
    cp -f $TMPFILE $TMPFILE2
    $EDITOR "$TMPFILE"
    if ! diff -q $TMPFILE $TMPFILE2; then
      echo -n "File changed. Write to device [Y/n]? "
      local ans
      read ans
      if [ "$ans" = "" -o "$ans" = "y" -o "$ans" = "Y" ]; then
        if ! "$ADB" "${ADB_FLAGS[@]}" push $TMPFILE $PREFS_FILE; then
          echo "*** Failed to write prefs file back."
          rm -f $TMPFILE $TMPFILE2
          exit 1
        else
          echo "Killing VrCore to make sure settings take effect."
          do_kill
        fi
      fi
    else
      echo "No changes to the file. Not writing file back to device."
    fi
  fi

  rm -f $TMPFILE $TMPFILE2
}

function do_gconfig() {
  local MODE="$1"
  local KEY="$2"
  local VALUE="$3"

  if [ -z "$KEY" ]; then
    echo "*** You must specify the gconfig key."
    echo "*** Run 'vrcore-tool' without args for help."
    exit 1
  fi
  if [ "$MODE" = "set" -a -z "$VALUE" ]; then
    echo "*** You must specify the gconfig value to set."
    echo "*** Run 'vrcore-tool' without args for help."
    exit 1
  fi

  # As seen in: https://docs.google.com/document/d/19pDo_LjoVyKdO9b7hoFt1BAmlYaFTFGkBER2Yb37FfA/edit#heading=h.twxis96g0g72
  # (go/config-design-doc)

  if [ "$MODE" = "set" ]; then
    echo "Setting GConfig override $KEY => $VALUE"
    "$ADB" "${ADB_FLAGS[@]}" shell am startservice \
      -n com.google.android.gms/.config.ConfigService \
      -a com.google.android.gms.config.OVERRIDE \
      --es __package__ com.google.vr.vrcore \
      --es __namespace__ configns:p4 \
      --es "$KEY" "$VALUE"
  else
    echo "Unsetting GConfig override $KEY."
    # To *unset* an override, we have to do something weird: pass in a
    # boolean extra (with any value).
    #
    # For reference, see:
    # https://cs.corp.google.com/piper///depot/google3/java/com/google/android/gmscore/integ/package/config/src/com/google/android/gms/config/ConfigChimeraService.java
    # (search for handleOverride).
    "$ADB" "${ADB_FLAGS[@]}" shell am startservice \
      -n com.google.android.gms/.config.ConfigService \
      -a com.google.android.gms.config.OVERRIDE \
      --es __package__ com.google.vr.vrcore \
      --es __namespace__ configns:p4 \
      --ez "$KEY" false
  fi

  echo "Killing VrCore to make sure settings take effect."
  do_kill
  echo "Done."
}

function do_gconfig_list() {
  adb_root_or_die
  # Based on:
  # https://wiki.corp.google.com/twiki/bin/view/Main/AndroidGservices#Viewing_Settings_On_Your_Device
  # (except that we use an explicit file name).

  echo "[[ CACHED VALUES ]]"
  run_sqlite3_sql "$GCONFIG_DB_FILE" \
      "select * from main where package = 'com.google.vr.vrcore'"
  echo
  echo "[[ OVERRIDEN VALUES ]]"
  run_sqlite3_sql "$GCONFIG_DB_FILE" \
      "select * from override where package = 'com.google.vr.vrcore'"
  echo
  echo "Done."
}

function do_gconfig_wipe() {
  echo "WARNING: This will WIPE your GmsCore data."
  echo "It's a pretty uncivilized thing to do to your device and may cause"
  echo "some errors. This should only be used for testing, when you want to"
  echo "be sure you are starting from a clean slate."
  echo
  get_approval
  adb_root_or_die
  echo "Wiping GmsCore state (including GConfig state)..."
  "$ADB" "${ADB_FLAGS[@]}" shell "pm clear com.google.android.gms"
  echo "Killing GmsCore to force it to reload its memory cache."
  "$ADB" "${ADB_FLAGS[@]}" shell "am force-stop com.google.android.gms"
  "$ADB" "${ADB_FLAGS[@]}" shell am force-stop com.google.android.gms
  echo "Killing VrCore too."
  do_kill
  echo
  echo "Done. GmsCore data reset to pristine state."
  echo "WARNING: All local gconfig overrides have been wiped as well!"
}

function run_sqlite3_sql() {
  local db_file="$1"
  local sql="$2"
  "$ADB" "${ADB_FLAGS[@]}" shell "sqlite3 $db_file \"$sql\""
}


function adb_root_or_die() {
  if ! "$ADB" "${ADB_FLAGS[@]}" root; then
    echo
    echo "*** 'adb root' failed."
    echo "*** Make sure you are using a userdebug build of Android, and that"
    echo "*** you can run 'adb root'. If you can't become root, you probably"
    echo "*** have a locked-down consumer Android build, which won't work."
    exit 1
  fi
}

function reset_prefs_file() {
  adb_root_or_die

  echo "Populating default (empty) VrCore prefs."
  local TMPFILE=/tmp/vrcore-tool-$$
  rm -rf $TMPFILE
  printf "<?xml version=\'1.0\' encoding=\'utf-8\' standalone=\'yes\' ?>\n<map>\n</map>" > $TMPFILE

  echo "Pushing default (empty) VrCore prefs."
  if ! "$ADB" "${ADB_FLAGS[@]}" push $TMPFILE $PREFS_FILE; then
    echo "*** Failed to push default prefs file."
    rm -rf $TMPFILE
    exit 1
  fi

  rm -rf $TMPFILE
}

function do_reset_prefs() {
  echo "Resetting VrCore prefs file."
  reset_prefs_file
  echo "Killing VrCore too."
  do_kill
}

function ensure_prefs_file_exists_or_die() {
  adb_root_or_die
  if ! "$ADB" "${ADB_FLAGS[@]}" shell ls "$PREFS_FILE"; then
    echo "Could not find VrCore prefs file: $PREFS_FILE"
    echo "Generating default (empty) VrCore prefs file."
    reset_prefs_file
  fi

  if ! "$ADB" "${ADB_FLAGS[@]}" shell ls "$PREFS_FILE"; then
    echo "Could not create VrCore prefs file: $PREFS_FILE"
    echo "Are you running on a rooted device, with VrCore installed?"
    echo "To force it to get created, run:"
    echo
    echo "    vrcore-tool.sh reset-prefs"
    echo
    exit 1
  fi
}

function run_command() {
  echo "Command: $1"
  while ! $1; do
    echo "Oops, command failed."
    echo -n "[R]etry, [S]kip? (default: R): "
    local ans
    read ans
    [ "$ans" = "s" -o "$ans" = "S" ] && break
  done
  sleep 1
}

function delete_pref() {
  replace_pref "whatever" "$1" "__DELETE__"
}

function replace_pref() {
  ensure_prefs_file_exists_or_die

  # Type of value: "string" or "boolean"
  local TYPE="$1"
  # Key to replace in prefs file
  local KEY="$2"
  # Value to replace it by.
  # If this is the special value "__DELETE__", the pref will be removed.
  local VALUE="$3"

  local TMPFILE=/tmp/vrcore-tool-$$
  local TMPFILE2=/tmp/vrcore-tool-$$-B

  rm -rf $TMPFILE
  if ! "$ADB" "${ADB_FLAGS[@]}" pull $PREFS_FILE \
      $TMPFILE; then
    echo "*** Failed to adb pull the prefs file."
    rm -f $TMPFILE $TMPFILE2
    exit 1
  fi

  grep -v $KEY $TMPFILE | grep -v '</map>' >$TMPFILE2

  if [ "$VALUE" != "__DELETE__"  ]; then
    echo "    <$TYPE name=\"$KEY\" value=\"$VALUE\" />" >>$TMPFILE2
  fi

  echo "</map>" >>$TMPFILE2

  if ! "$ADB" "${ADB_FLAGS[@]}" push $TMPFILE2 $PREFS_FILE; then
    echo "*** Failed to write prefs file back."
    rm -f $TMPFILE $TMPFILE2
    exit 1
  fi

  rm -f $TMPFILE

  if ! "$ADB" "${ADB_FLAGS[@]}" pull $PREFS_FILE $TMPFILE; then
    echo "*** Failed to read file back for verification."
    rm -f $TMPFILE $TMPFILE2
    exit 1
  fi

  cat $TMPFILE
  echo
  rm -f $TMPFILE $TMPFILE2
  echo "Pref successfully set."
  echo "Restarting VrCore for prefs to take effect."
  "$ADB" "${ADB_FLAGS[@]}" shell am force-stop com.google.vr.vrcore
}

main_menu "$@"
