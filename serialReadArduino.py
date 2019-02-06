#!/usr/bin/python

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # open serial port
time.sleep(2)
retVal = 0.0
ser.write('r')     # write a string
retVal = float(ser.readline())
ser.write('r')     # write a string
retVal = retVal + float(ser.readline())
ser.write('r')     # write a string
retVal = retVal + float(ser.readline())
print(retVal/3.0)

ser.close()             # close port
