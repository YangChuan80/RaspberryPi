import sys
import Adafruit_DHT
import lcddriver
import time

display = lcddriver.lcd()

while(True):
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).

    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 17)

    # Un-comment the line below to convert the temperature to Fahrenheit.
    # temperature = temperature * 9/5.0 + 32

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!


    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        
        display.lcd_display_string("Temp: " + str(temperature), 1) # Write line of text to first line of display
        display.lcd_display_string("Humidity: " + str(humidity) +'% ', 2) # Write line of text to second line of display
        #time.sleep(1)                                     # Give time for the message to be read
        #display.lcd_clear()                
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)