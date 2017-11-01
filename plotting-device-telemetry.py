# import matplotlib.pyplot as plt

# this section of the code reads in the header information of the data
# file expecting the Device Name, Device SN, Device SW Build Type, and
# Device SW Build Number. If your data file did not collect that
# information, it may affect the subsequent sections of this script.
file            = open('./20171024T141931_walleye_HT7841A00732.log','r')
lines           = file.readlines()
device          = lines[0].rstrip('\n')
device_sn       = lines[1].rstrip('\n')
android_build   = lines[2].rstrip('\n')
vr_home         = lines[3].rstrip('\n')
vr_core         = lines[4].rstrip('\n')

# # Now, for the fun part
data_header     = lines[5]
timestamp       = []
battery_charge  = []
tz0             = []
data            = lines[6:]
print data
#print data
#print data[0]
print list(data)

for i in range(0,len(data),1):
    tmp             = ([s.replace('\n','') for s in data])
    #timestamp       = timestamp + [tmp[0]]
    #battery_charge  = battery_charge + [tmp[1]]
    #battery_voltage = current + [tmp[2]]
    #voltage         = voltage + [tmp[3]]
    #tz0             = tz0 + [tmp[6]]



#print float(tz0[0])
# x_plot_vals = []
# y_plot_vals = []
# for i in range(1,len(timestamp),1):
#     tmp = [float(tz0[i])/100]
#     print tmp
#     x_plot_vals = x_plot_vals + [str((i*10)/float(3600))]
#     y_plot_vals = y_plot_vals + [float(tz0[i])/100]
#
# x_plot_vals = map(float,x_plot_vals)
# y_plot_vals = map(float,y_plot_vals)
#
# plt.plot(x_plot_vals,y_plot_vals)
# plt.ylabel('battery charge (%)')
# plt.xlabel('time (hours)')
# plt.show()
#
