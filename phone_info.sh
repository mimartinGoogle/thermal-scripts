#!/bin/bash
echo 'Android phone serial#:'
adb devices
echo 'Android Build#:'
adb shell getprop | grep 'ro.build.display.id'
echo 'VrCore:'
adb shell dumpsys package com.google.vr.vrcore | grep versionName
echo 'VrHome:'
adb shell dumpsys package com.google.android.vr.home | grep versionName
