#!/bin/bash

# Add this script to your crontab to make it run every 5 minutes:
# */5 * * * * /home/pi/secretGarden/getMeasurents.sh
#


date +"%d/%m/%Y %H:%M" > tmp
read timeOfDay < tmp
echo ${timeOfDay} | tr -s '\n' '\t' >> temperature.txt

wget 192.168.1.191 -O soilHumidity.tmp
echo ${timeOfDay} | tr -s '\n' '\t' >> humidity.txt
cat soilHumidity.tmp >> humidity.txt

#wget 192.168.1.191 -O tmptemperature.txt
./readTemp.py >> temperature.txt

wc -l temperature.txt > tmp
read lines filename < tmp

awk "NR>($lines-12)" temperature.txt > lastHourTemp.txt
awk "NR>($lines-12)" humidity.txt > lastHourHum.txt

if [ $lines -gt 288 ]
then
	awk "NR>($lines-288)" temperature.txt > lastDayTemp.txt
	awk "NR>($lines-288)" humidity.txt > lastDayHum.txt
else
	cat temperature.txt > lastDayTemp.txt
	cat humidity.txt > lastDayHum.txt
fi

gnuplot /home/pi/plotData.gplt
