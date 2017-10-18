# This is a library to call thermal zones on a device


class ThermalZones(object):
    ZONE_PATH0 = 'adb shell cat /sys/class/thermal/thermal_zone0'
    ZONE_PATH1 = 'adb shell cat /sys/class/thermal/thermal_zone1'
    ZONE_PATH2 = 'adb shell cat /sys/class/thermal/thermal_zone2'
    ZONE_PATH3 = 'adb shell cat /sys/class/thermal/thermal_zone3'
    ZONE_PATH4 = 'adb shell cat /sys/class/thermal/thermal_zone4'
    ZONE_PATH5 = 'adb shell cat /sys/class/thermal/thermal_zone5'
    ZONE_PATH6 = 'adb shell cat /sys/class/thermal/thermal_zone6'
    ZONE_PATH7 = 'adb shell cat /sys/class/thermal/thermal_zone7'
    ZONE_PATH8 = 'adb shell cat /sys/class/thermal/thermal_zone8'
    ZONE_PATH9 = 'adb shell cat /sys/class/thermal/thermal_zone9'
    ZONE_PATH10 = 'adb shell cat /sys/class/thermal/thermal_zone10'
    ZONE_PATH11 = 'adb shell cat /sys/class/thermal/thermal_zone11'
    ZONE_PATH12 = 'adb shell cat /sys/class/thermal/thermal_zone12'
    ZONE_PATH13 = 'adb shell cat /sys/class/thermal/thermal_zone13'
    ZONE_PATH14 = 'adb shell cat /sys/class/thermal/thermal_zone14'
    ZONE_PATH15 = 'adb shell cat /sys/class/thermal/thermal_zone15'
    ZONE_PATH16 = 'adb shell cat /sys/class/thermal/thermal_zone16'
    ZONE_PATH17 = 'adb shell cat /sys/class/thermal/thermal_zone17'
    ZONE_PATH18 = 'adb shell cat /sys/class/thermal/thermal_zone18'
    ZONE_PATH19 = 'adb shell cat /sys/class/thermal/thermal_zone19'
    ZONE_PATH20 = 'adb shell cat /sys/class/thermal/thermal_zone20'
    ZONE_PATH21 = 'adb shell cat /sys/class/thermal/thermal_zone21'
    ZONE_PATH22 = 'adb shell cat /sys/class/thermal/thermal_zone22'
    ZONE_PATH23 = 'adb shell cat /sys/class/thermal/thermal_zone23'
    ZONE_PATH24 = 'adb shell cat /sys/class/thermal/thermal_zone24'
    ZONE_PATH25 = 'adb shell cat /sys/class/thermal/thermal_zone25'
    ZONE_PATH26 = 'adb shell cat /sys/class/thermal/thermal_zone26'
    ZONE_PATH27 = 'adb shell cat /sys/class/thermal/thermal_zone27'
    ZONE_PATH28 = 'adb shell cat /sys/class/thermal/thermal_zone28'
    ZONE_PATH29 = 'adb shell cat /sys/class/thermal/thermal_zone29'
    ZONE_PATH30 = 'adb shell cat /sys/class/thermal/thermal_zone30'
    ZONE_PATH31 = 'adb shell cat /sys/class/thermal/thermal_zone31'
    ZONE_PATH32 = 'adb shell cat /sys/class/thermal/thermal_zone32'
    ZONE_PATH33 = 'adb shell cat /sys/class/thermal/thermal_zone33'
    ZONE_PATH34 = 'adb shell cat /sys/class/thermal/thermal_zone34'
    ZONE_PATH35 = 'adb shell cat /sys/class/thermal/thermal_zone35'
    ZONE_PATH36 = 'adb shell cat /sys/class/thermal/thermal_zone35'

    def __init__(self, t_zone):
        self.t_zone = t_zone

    def get_thermal_zone(self,zone=ZONE_PATH0):
        return self.get_thermal_zone0(zone)
