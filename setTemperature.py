#!/usr/bin/python

import RPi.GPIO as gpio
import os
import glob
import time
import datetime

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

heaterPin = 18

gpio.setmode(gpio.BCM)
gpio.setup(heaterPin, gpio.OUT)

pinStatus   = gpio.input(heaterPin)
currentTemp = read_temp()

now = datetime.datetime.now()

startTime = now.replace(hour=14, minute=0)
stopTime  = now.replace(hour=7, minute=15)

targetTemp = 17.0
if(now > startTime or now < stopTime):
    targetTemp = 22.0

# Heater is on...
if pinStatus:
    # and we have reached target, so switch off
    if(currentTemp > targetTemp):
        gpio.output(heaterPin, gpio.LOW)
# Heat is off...
else:
    # and we are below target, so switch on
    if(currentTemp < targetTemp):
        gpio.output(heaterPin, gpio.HIGH)

pinStatus = gpio.input(heaterPin)

fp = open('/var/www/html/heaterPin.txt', 'w')
fp.write(str(pinStatus) + '\n' + str(targetTemp)+ '\n' + str(currentTemp) + '\n' )
fp.close()
