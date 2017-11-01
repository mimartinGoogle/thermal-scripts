## M. Martin
## 10/10/2017
## This code is meant to collect temperature, GPU, CPU, and Bus performance telemetry from an Android Device.
## It also writes data to file in regular intervals and collects a screen shot of the device during each data point.
##
## TO DO: get rid of the "INFO:" text in the log file
## TO DO: figure out how to calculate frame rate (FPS)
## TO DO: add text to include the software build name next to the build number in the log header
## TO DO: note the temperature zones of interest for each device; i.e., which one is referenced for throttling
## TO DO: write a separate script that processes the log data and makes plots
## TO DO: add bugreport to final step of code (outside of loop)

import commands
import time
import string
import logging

######################### begin getting the device info ########################
# product name #
product         = commands.getoutput('adb shell getprop | grep -i ro.product.name')
tmp1_product    = product.replace('[','')
tmp2_product    = tmp1_product.replace(']','')
tmp3_product    = tmp2_product.split()
product         = tmp3_product[1]

# device Serial Number #
serial_num  = commands.getoutput('adb shell getprop | grep -i ro.boot.serialno')
tmp1_sn    = serial_num.replace('[','')
tmp2_sn    = tmp1_sn.replace(']','')
tmp3_sn    = tmp2_sn.split()
serial_num  = tmp3_sn[1]

# android build #
android_build   = commands.getoutput('adb shell getprop | grep -i ro.build.description')
tmp1_a_build    = android_build.split()
length          = len(tmp1_a_build)
tmp2_a_build    = tmp1_a_build[1:length]
tmp3_a_build    = string.join(tmp2_a_build,' ')
tmp4_a_build    = tmp3_a_build.replace('[','')
android_build    = tmp4_a_build.replace(']','')

# Vr Home Version #
vr_home         = commands.getstatusoutput('adb shell dumpsys package com.google.vr.vrcore | grep versionName')
tmp1_vr_home    = vr_home[1].split()
tmp2_vr_home    = tmp1_vr_home[0]
tmp3_vr_home    = tmp2_vr_home.lstrip()
vr_home         = tmp3_vr_home.lstrip('versionName=')

# Vr Core Version #
vr_core         = commands.getstatusoutput('adb shell dumpsys package com.google.android.vr.home | grep versionName')
tmp1_vr_core    = vr_core[1]
tmp2_vr_core    = tmp1_vr_core.lstrip()
vr_core         = tmp2_vr_core.lstrip('versionName=')
######################### end getting device info ##############################

## run an app on the device
# dreambench = 'adb -s '+ serial_num + ' ' + 'shell am start -n "com.google.vr.apps.dreambench/.MainActivity"'
# print dreambench
# v = commands.getoutput(dreambench)
# print v

########################### Initialize Logfile #################################
ds = time.strftime('%Y%m%d')
ts = time.strftime('%H%M%S')
log_filename = ds + 'T' + ts + '_' + product + '_' + serial_num + '.log'
logging.basicConfig(format='%(message)s',filename=log_filename,level=logging.DEBUG)
logging.info(product)
logging.info(serial_num)
logging.info(android_build)
logging.info(vr_home)
logging.info(vr_core)
log_info = ['timestamp','battery_%','battery_voltage','battery_current','tz0','tz1','tz2','tz3','tz4','tz5','tz6','tz7','tz8','tz9','tz10','tz11','tz12','tz13','tz14','tz15','tz16','tz17','tz18','tz19','tz20','tz21','tz22','tz23','tz24','tz25','tz26','tz27','tz28','tz29','tz30','tz33','tz34','tz35','tz36','cpu0','cpu1','cpu2','cpu3','cpu4','cpu5','cpu6','cpu7','bus','gpu']
logging.info(log_info)
########################### End Logfile Initialization #########################
############################# Begin Collecting Data ############################
loops = 90
for i in range(loops):
    print str(i) +' ' + time.strftime('%X')

    # apply timestamp to data point
    timestamp = time.strftime('%X')
    ds = time.strftime('%Y%m%d')
    ts = time.strftime('%H%M%S')

    # get device temperatures #
    tz0 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone0/temp')
    tz1 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone1/temp')
    tz2 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone2/temp')
    tz3 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone3/temp')
    tz4 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone4/temp')
    tz5 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone5/temp')
    tz6 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone6/temp')
    tz7 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone7/temp')
    tz8 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone8/temp')
    tz9 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone9/temp')
    tz10 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone10/temp')
    tz11 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone11/temp')
    tz12 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone12/temp')
    tz13 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone13/temp')
    tz14 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone14/temp')
    tz15 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone15/temp')
    tz16 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone16/temp')
    tz17 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone17/temp')
    tz18 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone18/temp')
    tz19 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone19/temp')
    tz20 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone20/temp')
    tz21 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone21/temp')
    tz22 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone22/temp')
    tz23 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone23/temp')
    tz24 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone24/temp')
    tz25 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone25/temp')
    tz26 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone26/temp')
    tz27 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone27/temp')
    tz28 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone28/temp')
    tz29 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone29/temp')
    tz30 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone30/temp')
    ## not on Vega ## tz31 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone31/temp')
    ## not on Vega ## tz32 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone32/temp')
    tz33 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone33/temp')
    tz34 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone34/temp')
    tz35 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone35/temp')
    tz36 = commands.getoutput('adb shell cat /sys/class/thermal/thermal_zone36/temp')

    # get battery info
    battery = commands.getoutput('adb shell cat /sys/class/power_supply/battery/capacity')
    voltage = commands.getoutput('adb shell cat /sys/class/power_supply/battery/voltage_now')
    current = commands.getoutput('adb shell cat /sys/class/power_supply/battery/current_now')

    # get CPU, GPU, and Bus info
    cpu0 = commands.getoutput('adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq')
    cpu1 = commands.getoutput('adb shell cat /sys/devices/system/cpu/cpu1/cpufreq/scaling_cur_freq')
    cpu2 = commands.getoutput('adb shell cat /sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq')
    cpu3 = commands.getoutput('adb shell cat /sys/devices/system/cpu/cpu3/cpufreq/scaling_cur_freq')
    cpu4 = commands.getoutput('adb shell cat /sys/devices/system/cpu/cpu4/cpufreq/scaling_cur_freq')
    cpu5 = commands.getoutput('adb shell cat /sys/devices/system/cpu/cpu5/cpufreq/scaling_cur_freq')
    cpu6 = commands.getoutput('adb shell cat /sys/devices/system/cpu/cpu6/cpufreq/scaling_cur_freq')
    cpu7 = commands.getoutput('adb shell cat /sys/devices/system/cpu/cpu7/cpufreq/scaling_cur_freq')
    bus = commands.getoutput('adb shell cat /sys/class/devfreq/soc:qcom,gpubw/cur_freq')
    gpu = commands.getoutput('adb shell cat /sys/class/kgsl/kgsl-3d0/devfreq/cur_freq')
    # take and save a screen shit
    screencap           = commands.getoutput('adb shell screencap -p /sdcard/test-img.png')
    transfer_capture = 'adb pull /sdcard/test-img.png /Users/mimartin/Documents/GitHub/thermal_scripts/vega/screen_caps/' + ds + 'T' + ts + '_' + product + '_' + serial_num + '.png'
    transfer_screencap  = commands.getoutput(transfer_capture)
    ############################## End Collecting Data #############################
    ########################## Begin Logging Data to file ##########################
    log_info = timestamp,battery,voltage,current,tz0,tz1,tz2,tz3,tz4,tz5,tz6,tz7,tz8,tz9,tz10,tz11,tz12,tz13,tz14,tz15,tz16,tz17,tz18,tz19,tz20,tz21,tz22,tz23,tz24,tz25,tz26,tz27,tz28,tz29,tz30,tz33,tz34,tz35,tz36,cpu0,cpu1,cpu2,cpu3,cpu4,cpu5,cpu6,cpu7,bus,gpu
    logging.info(log_info)
    time.sleep(1)