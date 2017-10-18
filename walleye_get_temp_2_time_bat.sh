echo "time, thermal_zone[0-30, 33-35], cpu freq[0-7], gpu freq, bus freq"
SECONDS=0
while [ $SECONDS -le $1 ]
do
  ts="$(date +"%T")"

  thermal_zone0="$(cat /sys/devices/virtual/thermal/thermal_zone0/temp)"
  thermal_zone1="$(cat /sys/devices/virtual/thermal/thermal_zone1/temp)"
  thermal_zone2="$(cat /sys/devices/virtual/thermal/thermal_zone2/temp)"
  thermal_zone3="$(cat /sys/devices/virtual/thermal/thermal_zone3/temp)"
  thermal_zone4="$(cat /sys/devices/virtual/thermal/thermal_zone4/temp)"
  thermal_zone5="$(cat /sys/devices/virtual/thermal/thermal_zone5/temp)"
  thermal_zone6="$(cat /sys/devices/virtual/thermal/thermal_zone6/temp)"
  thermal_zone7="$(cat /sys/devices/virtual/thermal/thermal_zone7/temp)"
  thermal_zone8="$(cat /sys/devices/virtual/thermal/thermal_zone8/temp)"
  thermal_zone9="$(cat /sys/devices/virtual/thermal/thermal_zone9/temp)"
  thermal_zone10="$(cat /sys/devices/virtual/thermal/thermal_zone10/temp)"
  thermal_zone11="$(cat /sys/devices/virtual/thermal/thermal_zone11/temp)"
  thermal_zone12="$(cat /sys/devices/virtual/thermal/thermal_zone12/temp)"
  thermal_zone13="$(cat /sys/devices/virtual/thermal/thermal_zone13/temp)"
  thermal_zone14="$(cat /sys/devices/virtual/thermal/thermal_zone14/temp)"
  thermal_zone15="$(cat /sys/devices/virtual/thermal/thermal_zone15/temp)"
  thermal_zone16="$(cat /sys/devices/virtual/thermal/thermal_zone16/temp)"
  thermal_zone17="$(cat /sys/devices/virtual/thermal/thermal_zone17/temp)"
  thermal_zone18="$(cat /sys/devices/virtual/thermal/thermal_zone18/temp)"
  thermal_zone19="$(cat /sys/devices/virtual/thermal/thermal_zone19/temp)"
  thermal_zone20="$(cat /sys/devices/virtual/thermal/thermal_zone20/temp)"
  thermal_zone21="$(cat /sys/devices/virtual/thermal/thermal_zone21/temp)"
  thermal_zone22="$(cat /sys/devices/virtual/thermal/thermal_zone22/temp)"
  thermal_zone23="$(cat /sys/devices/virtual/thermal/thermal_zone23/temp)"
  thermal_zone24="$(cat /sys/devices/virtual/thermal/thermal_zone24/temp)"
  thermal_zone25="$(cat /sys/devices/virtual/thermal/thermal_zone25/temp)"
  thermal_zone26="$(cat /sys/devices/virtual/thermal/thermal_zone26/temp)"
  thermal_zone27="$(cat /sys/devices/virtual/thermal/thermal_zone27/temp)"
  thermal_zone28="$(cat /sys/devices/virtual/thermal/thermal_zone28/temp)"
  thermal_zone29="$(cat /sys/devices/virtual/thermal/thermal_zone29/temp)"
  thermal_zone30="$(cat /sys/devices/virtual/thermal/thermal_zone30/temp)"

  thermal_zone33="$(cat /sys/devices/virtual/thermal/thermal_zone33/temp)"
  thermal_zone34="$(cat /sys/devices/virtual/thermal/thermal_zone34/temp)"
  thermal_zone35="$(cat /sys/devices/virtual/thermal/thermal_zone35/temp)"


  cpu0_freq="$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq)"
  cpu1_freq="$(cat /sys/devices/system/cpu/cpu1/cpufreq/scaling_cur_freq)"
  cpu2_freq="$(cat /sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq)"
  cpu3_freq="$(cat /sys/devices/system/cpu/cpu3/cpufreq/scaling_cur_freq)"
  cpu4_freq="$(cat /sys/devices/system/cpu/cpu4/cpufreq/scaling_cur_freq)"
  cpu5_freq="$(cat /sys/devices/system/cpu/cpu5/cpufreq/scaling_cur_freq)"
  cpu6_freq="$(cat /sys/devices/system/cpu/cpu6/cpufreq/scaling_cur_freq)"
  cpu7_freq="$(cat /sys/devices/system/cpu/cpu7/cpufreq/scaling_cur_freq)"

  gpu_freq="$(cat /sys/class/kgsl/kgsl-3d0/devfreq/cur_freq)"
  bus_freq="$(cat /sys/class/devfreq/soc:qcom,gpubw/cur_freq)"

  bat_level="$(dumpsys battery | grep level)"

  echo $ts \
       $((thermal_zone0 / 1000)).$((thermal_zone0 % 1000)) \
       $((thermal_zone1 / 10)).$((thermal_zone1 % 10)) \
       $((thermal_zone2 / 1000)).$((thermal_zone2 % 1000)) \
       $((thermal_zone3 / 1000)).$((thermal_zone3 % 1000)) \
       $((thermal_zone4 / 1000)).$((thermal_zone4 % 1000)) \
       $((thermal_zone5 / 1)).$((thermal_zone5 % 1)) \
       $((thermal_zone6 / 1)).$((thermal_zone6 % 1)) \
       $((thermal_zone7 / 1)).$((thermal_zone7 % 1)) \
       $((thermal_zone8 / 1)).$((thermal_zone8 % 1)) \
       $((thermal_zone9 / 1)).$((thermal_zone9 % 1)) \
       $((thermal_zone10 / 1)).$((thermal_zone10 % 1)) \
       $((thermal_zone11 / 10)).$((thermal_zone11 % 10)) \
       $((thermal_zone12 / 10)).$((thermal_zone12 % 10)) \
       $((thermal_zone13 / 10)).$((thermal_zone13 % 10)) \
       $((thermal_zone14 / 10)).$((thermal_zone14 % 10)) \
       $((thermal_zone15 / 10)).$((thermal_zone15 % 10)) \
       $((thermal_zone16 / 10)).$((thermal_zone16 % 10)) \
       $((thermal_zone17 / 10)).$((thermal_zone17 % 10)) \
       $((thermal_zone18 / 10)).$((thermal_zone18 % 10)) \
       $((thermal_zone19 / 10)).$((thermal_zone19 % 10)) \
       $((thermal_zone20 / 10)).$((thermal_zone20 % 10)) \
       $((thermal_zone21 / 10)).$((thermal_zone21 % 10)) \
       $((thermal_zone22 / 10)).$((thermal_zone22 % 10)) \
       $((thermal_zone23 / 10)).$((thermal_zone23 % 10)) \
       $((thermal_zone24 / 10)).$((thermal_zone24 % 10)) \
       $((thermal_zone25 / 10)).$((thermal_zone25 % 10)) \
       $((thermal_zone26 / 10)).$((thermal_zone26 % 10)) \
       $((thermal_zone27 / 10)).$((thermal_zone27 % 10)) \
       $((thermal_zone28 / 10)).$((thermal_zone28 % 10)) \
       $((thermal_zone29 / 10)).$((thermal_zone29 % 10)) \
       $((thermal_zone30 / 10)).$((thermal_zone30 % 10)) \
       $((thermal_zone33 / 1000)).$((thermal_zone33 % 1000)) \
       $((thermal_zone34 / 1)).$((thermal_zone34 % 1)) \
       $((thermal_zone35 / 1)).$((thermal_zone35 % 1)) \
       $cpu0_freq \
       $cpu1_freq \
       $cpu2_freq \
       $cpu3_freq \
       $cpu4_freq \
       $cpu5_freq \
       $cpu6_freq \
       $cpu7_freq \
       $gpu_freq \
       $bus_freq \
       $bat_level

  sleep 10
done
