Python DHT Sensor & LCD 1602 Display
==================================

Python library to read the DHT series of humidity and temperature sensors on a
Raspberry Pi or Beaglebone Black.

Currently the library is tested with Python 2.6, 2.7, 3.3 and 3.4. It should
work with Python greater than 3.4, too.

Installing
----------

### LCD 1602 Driver

On Raspbian or Beaglebone Black's Debian/Ubuntu image you can ensure your
system is ready by running one or two of the following sets of commands:

````sh
git clone https://github.com/the-raspberry-pi-guy/lcd
````
Change the directory to lcd:

```sh
cd lcd 
```

Install sh:

```sh
sudo sh install.sh
```
Then you'll get **reboot**.

### Install DHT11 or DHT22 Drivers

Run pip command:

```sh
sudo pip3 install Adafruit_DHT
```

You may also git clone the repository if you want to test an unreleased
version:

```sh
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
```

Usage
-----

See example of usage in the examples folder.

Author
------

Adafruit invests time and resources providing this open source code, please
support Adafruit and open-source hardware by purchasing products from Adafruit!

Written by Tony DiCola for Adafruit Industries.

MIT license, all text above must be included in any redistribution
