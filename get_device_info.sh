#!/bin/bash
./adb root > /dev/null
sleep 1

device="$(./adb shell getprop | grep -i ro.product.name)"
device_id="$(./adb shell getprop | grep -i ro.serialno)"
sw_build="$(./adb shell getprop | grep -i ro.build.type)"
sw_build_num="$(./adb shell getprop | grep -i ro.build.version.incremental)"

echo $ts
echo $device
echo $device_id
echo $sw_build
echo $sw_build_num
echo 
echo "timestamp battery current voltage tz1 tz2 tz3 tz4 tz5 tz6 tz7 tz8 tz9 tz10 tz11 tz12 tz13 tz14 tz15 tz16 tz17 tz18 tz19 tz20 tz21 tz22 tz23 tz24 tz25 tz26 tz29 tz30 tz31 tz32 current voltage"
while true
do
  # print timestamp
  ts="$(date +"%T")"
  # print battery life
  battery_life="$(./adb shell cat /sys/class/power_supply/battery/capacity)"
  # print voltage and current
  current="$(./adb shell cat /sys/class/power_supply/battery/current_now)"
  voltage="$(./adb shell cat /sys/class/power_supply/battery/voltage_now)"
  # print thermal zones (a "thermal zone" is a temperature sensor reading on the hardware)
  thermal_zone1="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone1/temp)"
  thermal_zone2="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone2/temp)"
  thermal_zone3="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone3/temp)"
  thermal_zone4="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone4/temp)"
  thermal_zone5="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone5/temp)"
  thermal_zone6="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone6/temp)"
  thermal_zone7="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone7/temp)"
  thermal_zone8="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone8/temp)"
  thermal_zone9="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone9/temp)"
  thermal_zone10="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone10/temp)"
  thermal_zone11="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone11/temp)"
  thermal_zone12="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone12/temp)"
  thermal_zone13="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone13/temp)"
  thermal_zone14="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone14/temp)"
  thermal_zone15="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone15/temp)"
  thermal_zone16="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone16/temp)"
  thermal_zone17="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone17/temp)"
  thermal_zone18="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone18/temp)"
  thermal_zone19="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone19/temp)"
  thermal_zone20="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone20/temp)"
  thermal_zone21="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone21/temp)"
  thermal_zone22="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone22/temp)"
  thermal_zone23="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone23/temp)"
  thermal_zone24="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone24/temp)"
  thermal_zone25="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone25/temp)"
  thermal_zone26="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone26/temp)"
  thermal_zone29="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone29/temp)"
  thermal_zone30="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone30/temp)"
  thermal_zone31="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone31/temp)"
  thermal_zone32="$(./adb shell cat /sys/devices/virtual/thermal/thermal_zone32/temp)"
  

  echo $ts $((battery_life)).0 $((current)).0 $((voltage)).0 $((thermal_zone1 / 10)).$((thermal_zone1 % 10)) $((thermal_zone2 / 10)).$((thermal_zone2 % 10)) $((thermal_zone3 / 10)).$((thermal_zone3 % 10)) $((thermal_zone4 / 10)).$((thermal_zone4 % 10)) $((thermal_zone5 / 10)).$((thermal_zone5 % 10)) $((thermal_zone6 / 10)).$((thermal_zone6 % 10)) $((thermal_zone7 / 10)).$((thermal_zone7 % 10)) $((thermal_zone8 / 10)).$((thermal_zone8 % 10)) $((thermal_zone9 / 10)).$((thermal_zone9 % 10)) $((thermal_zone10 / 10)).$((thermal_zone10 % 10)) $((thermal_zone11 / 10)).$((thermal_zone11 % 10)) $((thermal_zone12 / 10)).$((thermal_zone12 % 10)) $((thermal_zone6 / 13)).$((thermal_zone6 % 13)) $((thermal_zone14 / 10)).$((thermal_zone14 % 10)) $((thermal_zone15 / 10)).$((thermal_zone15 % 10)) $((thermal_zone16 / 10)).$((thermal_zone16 % 10)) $((thermal_zone17 / 10)).$((thermal_zone17 % 10)) $((thermal_zone18 / 10)).$((thermal_zone18 % 10)) $((thermal_zone19 / 10)).$((thermal_zone19 % 10)) $((thermal_zone20 / 10)).$((thermal_zone20 % 10)) $((thermal_zone21 / 10)).$((thermal_zone21 % 10)) $((thermal_zone22 / 10)).$((thermal_zone22 % 10)) $((thermal_zone23 / 10)).$((thermal_zone23 % 10)) $((thermal_zone24 / 10)).$((thermal_zone24 % 10)) $((thermal_zone25 / 10)).$((thermal_zone25 % 10)) $((thermal_zone26 / 10)).$((thermal_zone26 % 10))   $((thermal_zone29 / 10)).$((thermal_zone29 % 10)) $((thermal_zone30 / 10)).$((thermal_zone30 % 10)) $((thermal_zone31 / 10)).$((thermal_zone31 % 10)) $((thermal_zone32 / 10)).$((thermal_zone32 % 10)) 
  sleep 10
done
