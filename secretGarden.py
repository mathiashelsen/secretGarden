#!/usr/bin/python

import sys
import os
import glob
import time
import serial
import datetime
import Adafruit_DHT
import RPi.GPIO as gpio

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

def read_soilhumidity():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # open serial port
    time.sleep(2)
    soilHumidity = 0.0
    ser.write('r')     # write a string
    soilHumidity = float(ser.readline())
    ser.write('r')     # write a string
    soilHumidity = soilHumidity + float(ser.readline())
    ser.write('r')     # write a string
    soilHumidity = soilHumidity + float(ser.readline())
    ser.close()             # close port
    return (400.0 - soilHumidity/3.0)/1.4
	
airHumidity, airTemperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 17)
soilTemperature = read_temp()
soilHumidity = read_soilhumidity()


heaterPin = 18

gpio.setmode(gpio.BCM)
gpio.setup(heaterPin, gpio.OUT)

pinStatus   = gpio.input(heaterPin)
currentTemp = soilTemperature

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

timeStr = now.strftime("%d/%m/%Y %H:%M")
logStr  = timeStr + '\t' + str(soilTemperature) + '\t' + str(soilHumidity) + '\t' + str(airTemperature) + '\t' + str(airHumidity) + '\t' + str(pinStatus*80 + 10) + '\n'
fp = open('secretGardenLog.txt', 'a')
fp.write(logStr)
fp.close()
