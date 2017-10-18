import time
import logging

ds = time.strftime('%Y%m%d')
ts = time.strftime('%H%M%S')
log_filename = ds + '_T_' + ts + '.log'
print log_filename
logging.basicConfig(format='%(levelname)s:%(message)s',filename=log_filename,level=logging.DEBUG)
log_info = 'battery_%','battery_voltage','battery_current','tz0','tz1','tz2','tz3','tz4','tz5','tz6','tz7','tz8','tz9','tz10','tz11','tz12','tz13','tz14','tz15','tz16','tz17','tz18','tz19','tz20','tz21','tz22','tz23','tz24','tz25','tz26','tz27','tz28','tz29','tz30','tz33','tz34','tz35','tz36','cpu0','cpu1','cpu2','cpu3','cpu4','cpu5','cpu6','cpu7','bus','gpu'
#log_info = '(DATE, TIME, INTERVAL)'
logging.info(log_info)



test_length     = 60                #minutes
test_length_s   = test_length*60    #seconds
interval_time   = 6                 #seconds
num_intervals   = 4# test_length_s / interval_time


for i in range(num_intervals):
    print i #+ ': ' + interval_time*int(i)
    log_info = time.strftime('%x, %X'),i
    print log_info
    logging.info(log_info)
