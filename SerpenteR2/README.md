# Using a Serpene R2 for data collection
This folder contains references for using a Serpente R2
https://www.solder.party/docs/serpente/r2/

This is a different approach to the original suggestion using a smartphone.

### Motivation
This simple embedded hardware allows offline-first data collection.

* The smartphone app is commercial and needs to be purchased
* Google Drive to store data on the internet
* Using Google Colab also requires a fee for extended use 

### Rational
I chose this hardware because:
1. Compact size
2. Relatively low cost
3. Ease of use
4. Low power consumption
...and its just what I had available. 
 
## Hardware
Using a Serpente R2 microcontroller simply attach a IMU (Intertial Measurement Unit) sensor to the I2C bus and add power

* https://www.tindie.com/products/arturo182/serpente-a-tiny-circuitpython-prototyping-board/ ~ $20.99 AUD
* https://core-electronics.com.au/mpu-6050-module-3-axis-gyroscope-acce-lerometer.html ~ $12.05 AUD
* https://core-electronics.com.au/lipo-polymer-lithium-ion-battery-120mah.html $9.85 AUD
* http://www.3dprintingshop.com.au/3d-printing-shops-3d-printing-service/ $4.65 AUD

Estimated Total Cost ~ $57.71 AUD based on local suppliers

> **Note** getting the case printed incurred setup costs, shop around or use your own printer.

![hardware steup](../images/SerpenteR2-Front.jpg)

In this example I used a MPU9250 based IMU (9DoF) sensor, and a CR2032 3v coin/button battery.
This was later updated to use a rechargeable LiPo battery and a cheaper MPU6050 (6DoF)

Later updates also simplified the switch to control write access to the file-system and used a simple jumper instead.

### Hardware Assembly
Simply solder the SDL, SCA pins together and use the 3v OUT and GND pins between the R2 and the sensor.

![hardware steup](../images/SerpenteR2-Back.jpg)

Attach the LiPo battery via a surface mount JST-PH 2-wire connector 

## Software
The Serpente R2 supported CircuitPython which is simple and easy to use.

### Software Assembly
Plugging the Serpente R2 into the USB port should present a disk that can be mounted much like any USB storage device.
Simply copy this folder to the toplevel directory of that storage and reset 

## Using
To use the board, simply install the battery and attach to your bike.

In normal operation:
* Green blinking LED indicates it is capturing and recording movement on the device
* Red blinking LED indicates a problem
* Blue blinking LED indicates it is writing the data on the controller

Plugging the device back into your computers USB port should give you:
1. measurements.csv - This contains the measurements
2. syslog.txt - This contains any error/issues that were encountered

## Testing
Attach the USB cable and use a terminal (eg Seaial on OSX or Putty on Windows or Screen on Linux) to access the serial console on the device
This will display the readings rather than writing them to the CSV file 

## Notes
* When the Serpente R2 is plugged into the USB port, it will not be able to write to the file system. You will see these warnings in the console whilst testing.

## TODO
1. Test run times to get a better indication of current draw / battery life
2. Add piezo buzzer to give realtime feedback (eg. pitch=elevation, final chime to indicate total time relative to best effort)
3. Add GPS or other sensors to correlate wheelie success with location
4. Update case to carry battery with re-charge port
5. Add on/off switch when on battery