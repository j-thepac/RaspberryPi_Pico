from machine import Pin
import time
led = Pin("LED", Pin.OUT)  # Pin(25, Pin.OUT)
for i in range(1, 5):
    print(i)
    led.value(1)
    time.sleep(1)  # Use 1 second instead of 10 seconds for better visibility
    led.value(0)
    time.sleep(1)