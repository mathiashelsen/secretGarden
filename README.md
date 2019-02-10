# secretGarden
Indoor growing with the Raspberry Pi

Scripts for monitoring your plants and indoor growing. These script use the ESP8266 as a remote node, but can also use the Pi's I2C/SPI/1-wire/... interface to measure soil humidity, room humidity, temperature, ...

Currently using:
 - ESP8266 using nodemcu (Lua framework, compiled with the ADC feature)
 - DS18B20
 - Capacitive soil sensors (eBay)
 
Dependencies:
 - pySerial (soil humidity)
 - adafruit DHT22 library
 - 1-wire support (config file)
 - nginx + php
