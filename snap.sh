#!/bin/bash

gphoto2 --get-config /main/status/batterylevel > /var/www/html/cameraBattery.txt
gphoto2 --capture-image-and-download --filename "%Y%m%d%H%M%S.jpg"

FILENAME=$(ls -ltr | tail -n 1 | awk '{print $NF}')
cp $FILENAME /var/www/html/lastImg.jpg
