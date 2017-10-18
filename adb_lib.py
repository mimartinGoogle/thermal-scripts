import subprocess
import time

ADB_RETRIES = 5


def run_command(cmd):
    if cmd.find("adb logcat -t") >= 0:
        cmd_arg_list = cmd.split(" ", 3)
    else:
        cmd_arg_list = cmd.split(" ")
    print cmd_arg_list
    # start activity
    proc = subprocess.Popen(cmd_arg_list, \
                            stdout=subprocess.PIPE, \
                            stderr=subprocess.PIPE)
    # wait for end of process and return output
    out, err = proc.communicate()
    return out


def root():
    proc = subprocess.Popen(['adb', 'root'], \
                            stdout=subprocess.PIPE, \
                            stderr=subprocess.PIPE)
    # wait for end of process and return output
    out, err = proc.communicate()
    return out


def shell(cmd, blocking=True):
    cmd_arg_list = ["adb", "shell"]
    cmd_arg_list_post = cmd.split(" ")
    cmd_arg_list.extend(cmd_arg_list_post)

    print cmd_arg_list
    retry = ADB_RETRIES

    # start activity
    proc = subprocess.Popen(cmd_arg_list, \
                            stdout=subprocess.PIPE, \
                            stderr=subprocess.PIPE)
    # wait for end of process and return output
    if blocking:
        while retry > 0:
            out, err = proc.communicate()
            print "shell result: %s" % (out + err)
            if err.lower().find("no devices") >= 0:
                retry = retry - 1
                time.sleep(5)
                if retry == 0:
                    raise RuntimeError("Shell command failed after %d retries: %s" % (ADB_RETRIES, (out + err)))
            else:
                retry = 0

        if err.lower().find("error") >= 0:
            raise RuntimeError("ERROR adb shell: %s" % err)
    else:
        out = None

    return out


def push(local_file, remote_file):
    cmd_arg_list = ["adb", "push"]
    cmd_arg_list_post = [local_file, remote_file]
    cmd_arg_list.extend(cmd_arg_list_post)

    # start activity
    proc = subprocess.Popen(cmd_arg_list, \
                            stdout=subprocess.PIPE, \
                            stderr=subprocess.PIPE)
    # wait for end of process and return output
    out, err = proc.communicate()
    return out


def pull(remote_file, local_file):
    cmd_arg_list = ["adb", "pull"]
    cmd_arg_list_post = [remote_file, local_file]
    cmd_arg_list.extend(cmd_arg_list_post)

    # start activity
    proc = subprocess.Popen(cmd_arg_list, \
                            stdout=subprocess.PIPE, \
                            stderr=subprocess.PIPE)
    # wait for end of process and return output
    out, err = proc.communicate()
    print "adb pull: " + out
    return out
