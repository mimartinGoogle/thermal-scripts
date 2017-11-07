import commands
import time
import os

current_working_directory   = os.getcwd()
logging_directory           = '/_logcat_files'
app_name                    = 'mekorama'
ds                          = time.strftime('%Y%m%d')
ts                          = time.strftime('%H%M%S')
chamber_temperature         = '30C'
logcat_data_directory          = current_working_directory + logging_directory + '/' + chamber_temperature + '/' + app_name
if not os.path.exists(logcat_data_directory):
    os.makedirs(logcat_data_directory)

print "If you didn't Enable Performance Monitoring Setting using 'vrcore-tools.sh', stop this test and do so now."
print "Clearing the logcat"
logcat_clear = commands.getoutput('adb logcat -b all -c')
print 'Logcat is Cleared'
print 'Recording the logcat to file. Stop the script manually to stop recording. The logcat file be saved automatically.'

ds = time.strftime('%Y%m%d')
ts = time.strftime('%H%M%S')
logcat_save = commands.getoutput('adb logcat > ' + logcat_data_directory + '/' + ds + 'T' + ts + '_' + app_name + '_logcat.txt')