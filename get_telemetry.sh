./adb root > /dev/null
sleep 5
echo "time_stamp  battery current voltage"

while true
do
  ts="$(date +"%T")"
  battery_life="$(./adb shell cat /sys/class/power_supply/battery/capacity)"
  current="$(./adb shell cat /sys/class/power_supply/battery/current_now)"
  voltage="$(./adb shell cat /sys/class/power_supply/battery/voltage_now)"
  
  echo $ts $((battery_life)).0 $((current)).0 $((voltage)).0
  sleep 6
done
