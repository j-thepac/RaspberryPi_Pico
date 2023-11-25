# Pin1 is GP0

from machine import Pin
import time
led = Pin(0, Pin.OUT)  # Pin 1
for i in range(1, 5):
    print(i)
    led.value(1)
    time.sleep(1)  # Use 1 second instead of 10 seconds for better visibility
    led.value(0)
    time.sleep(1)# LED external
