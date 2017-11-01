## M. Martin
## 10/123/2017

import commands
import time

# ######################### begin getting the device info ########################
# # product name #
# product         = commands.getoutput('adb shell getprop | grep -i ro.product.name')
# print product
# tmp1_product    = product.replace('[','')
# tmp2_product    = tmp1_product.replace(']','')
# tmp3_product    = tmp2_product.split()
# product         = tmp3_product[1]
#
# # device Serial Number #
# serial_num  = commands.getoutput('adb shell getprop | grep -i ro.boot.serialno')
# tmp1_sn    = serial_num.replace('[','')
# tmp2_sn    = tmp1_sn.replace(']','')
# tmp3_sn    = tmp2_sn.split()
# serial_num  = tmp3_sn[1]
#
# # android build #
# android_build   = commands.getoutput('adb shell getprop | grep -i ro.build.description')
# tmp1_a_build    = android_build.split()
# length          = len(tmp1_a_build)
# tmp2_a_build    = tmp1_a_build[1:length]
# tmp3_a_build    = string.join(tmp2_a_build,' ')
# tmp4_a_build    = tmp3_a_build.replace('[','')
# android_build    = tmp4_a_build.replace(']','')
#
# # Vr Home Version #
# vr_home         = commands.getstatusoutput('adb shell dumpsys package com.google.vr.vrcore | grep versionName')
# tmp1_vr_home    = vr_home[1].split()
# tmp2_vr_home    = tmp1_vr_home[0]
# tmp3_vr_home    = tmp2_vr_home.lstrip()
# vr_home         = tmp3_vr_home.lstrip('versionName=')
#
# # Vr Core Version #
# vr_core         = commands.getstatusoutput('adb shell dumpsys package com.google.android.vr.home | grep versionName')
# tmp1_vr_core    = vr_core[1]
# tmp2_vr_core    = tmp1_vr_core.lstrip()
# vr_core         = tmp2_vr_core.lstrip('versionName=')
######################### end getting device info ##############################
######################## begin test ############################################
x_one = commands.getoutput(
    'adb -s 709KPPB0013584 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
if x_one == "error: device '709KPPB0013584' not found":
    print '709KPPB0013584 not found at start'
else:
    print '709KPPB0013584 is okay at start'

x_two = commands.getoutput(
    'adb -s 709KPWQ0017585'
    ' shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
if x_two == "error: device '709KPWQ0017585' not found":
    print '709KPWQ0017585 not found at start'
else:
    print '709KPWQ0017585 is okay at start'

x_three = commands.getoutput(
    'adb -s 709KPWQ0020441 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
if x_three == "error: device '709KPWQ0020441' not found":
    print '709KPWQ0020441 not found at start'
else:
    print '709KPWQ0020441 is okay at start'

x_four = commands.getoutput(
    'adb -s 709KPXV0017490 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
if x_four == "error: device '709KPXV0017490' not found":
    print '709KPXV0017490 not found at start'
else:
    print '709KPXV0017490 is okay at start'

x_five = commands.getoutput(
    'adb -s 709KPAE0020536 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
if x_five == "error: device '709KPAE0020536' not found":
    print '709KPAE0020536 not found at start'
else:
    print '709KPAE0020536 is okay at start'

x_six = commands.getoutput(
    'adb -s 709KPED0017148 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
if x_six == "error: device '709KPED0017148' not found":
    print '709KPED0017148 not found at start'
else:
    print '709KPED0017148 is okay at start'

x_seven = commands.getoutput(
    'adb -s 709KPZK0020621 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
if x_seven == "error: device '709KPZK0020621' not found":
    print '709KPZK0020621 not found at start'
else:
    print '709KPZK0020621 is okay at start'

x_eight = commands.getoutput(
    'adb -s 709KPHG0017569 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
if x_eight == "error: device '709KPHG0017569' not found":
    print '709KPHG0017569 not found at start'
else:
    print '709KPHG0017569 is okay at start'

x_nine = commands.getoutput(
    'adb -s 709KPSL0015150 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
if x_nine == "error: device '709KPSL0015150' not found":
    print '709KPSL0015150 not found at start'
else:
    print '709KPSL0015150 is okay at start'

x_ten = commands.getoutput(
    'adb -s 709KPTM0020457 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
if x_ten == "error: device '709KPTM0020457' not found":
    print '709KPTM0020457 not found at start'
else:
    print '709KPTM0020457 is okay at start'





commands.getoutput('adb -s 709KPPB0013584 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
commands.getoutput('adb -s 709KPWQ0017585 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
commands.getoutput('adb -s 709KPWQ0020441 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
commands.getoutput('adb -s 709KPXV0017490 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
commands.getoutput('adb -s 709KPAE0020536 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
commands.getoutput('adb -s 709KPED0017148 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
commands.getoutput('adb -s 709KPZK0020621 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
commands.getoutput('adb -s 709KPHG0017569 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
commands.getoutput('adb -s 709KPSL0015150 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')
commands.getoutput('adb -s 709KPTM0020457 shell am start -a android.intent.action.VIEW -d "https://youtu.be/95d7tc0FsRI?list=PLX3yFl1H9UMzCKer71XVlX8iYYCtuSigZ" com.google.android.apps.youtube.vr')

length_of_test  = 7200 #seconds
for i in range(length_of_test+1):
    print str(i) + ' seconds since test started. Total test length will be ' + str(length_of_test) + ' seconds.'
    time.sleep(1)
    if i == 10:
        print 'Logging Bug Reports, start of test'
        ds =            time.strftime('%Y%m%d')
        ts =            time.strftime('%H%M%S')
        commands.getoutput(
            'adb -s 709KPPB0013584 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPPB0013584_' + ds + 'T' + ts + '_' + 'bugreport' )
        print 'bug report 1'
        commands.getoutput(
            'adb -s 709KPWQ0017585 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPWQ0017585_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 2'
        commands.getoutput(
            'adb -s 709KPWQ0020441 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPWQ0020441_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 3'
        commands.getoutput(
            'adb -s 709KPXV0017490 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPXV0017490_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 4'
        commands.getoutput(
            'adb -s 709KPAE0020536 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPAE0020536_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 5'
        commands.getoutput(
            'adb -s 709KPED0017148 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPED0017148_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 6'
        commands.getoutput(
            'adb -s 709KPZK0020621 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPZK0020621_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 7'
        commands.getoutput(
            'adb -s 709KPHG0017569 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPHG0017569_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 8'
        commands.getoutput(
            'adb -s 709KPSL0015150 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPSL0015150_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 9'
        commands.getoutput(
            'adb -s 709KPTM0020457 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPTM0020457_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 10'
    elif i == 1800:
        print 'Logging Bug Reports, 0.5 hours'
        ds =            time.strftime('%Y%m%d')
        ts =            time.strftime('%H%M%S')
        commands.getoutput(
            'adb -s 709KPPB0013584 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPPB0013584_' + ds + 'T' + ts + '_' + 'bugreport' )
        print 'bug report 1'
        commands.getoutput(
            'adb -s 709KPWQ0017585 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPWQ0017585_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 2'
        commands.getoutput(
            'adb -s 709KPWQ0020441 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPWQ0020441_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 3'
        commands.getoutput(
            'adb -s 709KPXV0017490 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPXV0017490_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 4'
        commands.getoutput(
            'adb -s 709KPAE0020536 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPAE0020536_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 5'
        commands.getoutput(
            'adb -s 709KPED0017148 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPED0017148_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 6'
        commands.getoutput(
            'adb -s 709KPZK0020621 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPZK0020621_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 7'
        commands.getoutput(
            'adb -s 709KPHG0017569 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPHG0017569_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 8'
        commands.getoutput(
            'adb -s 709KPSL0015150 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPSL0015150_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 9'
        commands.getoutput(
            'adb -s 709KPTM0020457 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPTM0020457_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 10'
    elif i == 3600:
        print 'Logging Bug Report, 1 hour'
        ds =            time.strftime('%Y%m%d')
        ts =            time.strftime('%H%M%S')
        commands.getoutput(
            'adb -s 709KPPB0013584 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPPB0013584_' + ds + 'T' + ts + '_' + 'bugreport' )
        print 'bug report 1'
        commands.getoutput(
            'adb -s 709KPWQ0017585 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPWQ0017585_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 2'
        commands.getoutput(
            'adb -s 709KPWQ0020441 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPWQ0020441_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 3'
        commands.getoutput(
            'adb -s 709KPXV0017490 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPXV0017490_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 4'
        commands.getoutput(
            'adb -s 709KPAE0020536 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPAE0020536_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 5'
        commands.getoutput(
            'adb -s 709KPED0017148 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPED0017148_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 6'
        commands.getoutput(
            'adb -s 709KPZK0020621 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPZK0020621_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 7'
        commands.getoutput(
            'adb -s 709KPHG0017569 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPHG0017569_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 8'
        commands.getoutput(
            'adb -s 709KPSL0015150 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPSL0015150_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 9'
        commands.getoutput(
            'adb -s 709KPTM0020457 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPTM0020457_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 10'
    elif i == 5400:
        print 'Logging Bug Report, 1.5 hours'
        ds =            time.strftime('%Y%m%d')
        ts =            time.strftime('%H%M%S')
        commands.getoutput(
            'adb -s 709KPPB0013584 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPPB0013584_' + ds + 'T' + ts + '_' + 'bugreport' )
        print 'bug report 1'
        commands.getoutput(
            'adb -s 709KPWQ0017585 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPWQ0017585_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 2'
        commands.getoutput(
            'adb -s 709KPWQ0020441 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPWQ0020441_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 3'
        commands.getoutput(
            'adb -s 709KPXV0017490 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPXV0017490_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 4'
        commands.getoutput(
            'adb -s 709KPAE0020536 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPAE0020536_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 5'
        commands.getoutput(
            'adb -s 709KPED0017148 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPED0017148_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 6'
        commands.getoutput(
            'adb -s 709KPZK0020621 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPZK0020621_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 7'
        commands.getoutput(
            'adb -s 709KPHG0017569 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPHG0017569_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 8'
        commands.getoutput(
            'adb -s 709KPSL0015150 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPSL0015150_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 9'
        commands.getoutput(
            'adb -s 709KPTM0020457 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPTM0020457_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 10'
    elif i == 7199:
        print 'Logging Bug Report, two hours (end of test)'
        ds =            time.strftime('%Y%m%d')
        ts =            time.strftime('%H%M%S')
        commands.getoutput(
            'adb -s 709KPPB0013584 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPPB0013584_' + ds + 'T' + ts + '_' + 'bugreport' )
        print 'bug report 1'
        commands.getoutput(
            'adb -s 709KPWQ0017585 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPWQ0017585_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 2'
        commands.getoutput(
            'adb -s 709KPWQ0020441 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPWQ0020441_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 3'
        commands.getoutput(
            'adb -s 709KPXV0017490 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPXV0017490_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 4'
        commands.getoutput(
            'adb -s 709KPAE0020536 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPAE0020536_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 5'
        commands.getoutput(
            'adb -s 709KPED0017148 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPED0017148_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 6'
        commands.getoutput(
            'adb -s 709KPZK0020621 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPZK0020621_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 7'
        commands.getoutput(
            'adb -s 709KPHG0017569 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPHG0017569_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 8'
        commands.getoutput(
            'adb -s 709KPSL0015150 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPSL0015150_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 9'
        commands.getoutput(
            'adb -s 709KPTM0020457 bugreport /Users/mimartin/Documents/GitHub/thermal-scripts/709KPTM0020457_' + ds + 'T' + ts + '_' + 'bugreport')
        print 'bug report 10'