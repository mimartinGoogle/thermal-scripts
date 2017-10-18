import matplotlib.pyplot as plt

# this section of the code reads in the header information of the data
# file expecting the Device Name, Device SN, Device SW Build Type, and
# Device SW Build Number. If your data file did not collect that
# information, it may affect the subsequent sections of this script.
file = open('./dev.txt','r')
lines = file.readlines()
device_info = lines[1:5]
device_name =           device_info[0].split()[1]
device_sn   =           device_info[1].split()[1]
device_sw_build_type =  device_info[2].split()[1]
device_sw_build_num =   device_info[3].split()[1]
print 'device_name =            ', device_name
print 'device_sn =              ', device_sn
print 'device_sw_build_type =   ', device_sw_build_type
print 'device_sw_build_num =    ', device_sw_build_num

# Now, for the fun part
time_stamps =       []
battery_charge =    []
t_zone1 =           []
data_header =       lines[6]
data =              lines[7:]
print data_header
time_stamp =    [] # HH:MM:SS
battery =       [] # %
current =       [] # micro-amps
voltage =       [] # micro-volts
tz1 =           [] # Celsius
for i in range(0,len(data),1):
    tmp =           data[i].split()
    time_stamp =    time_stamp + [tmp[0]]
    battery =       battery + [tmp[1]]
    current =       current + [tmp[2]]
    voltage =       voltage + [tmp[3]]
    tz1 =           tz1 + [tmp[4]]



file.close()

x_plot_vals = []
y_plot_vals = []
for i in range(1,len(time_stamp),1):
    tmp = [float(current[i])/1000000]
    print tmp
    x_plot_vals = x_plot_vals + [str((i*10)/float(3600))]
    y_plot_vals = y_plot_vals + [float(current[i])/1000000]

x_plot_vals = map(float,x_plot_vals)
y_plot_vals = map(float,y_plot_vals)

plt.plot(x_plot_vals,y_plot_vals)
plt.ylabel('battery charge (%)')
plt.xlabel('time (hours)')
plt.show()

