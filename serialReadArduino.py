#!/usr/bin/python

import serial
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # open serial port
ser.write(b'r')     # write a string
retVal = ser.readline()
print(retVal)
ser.close()             # close port
