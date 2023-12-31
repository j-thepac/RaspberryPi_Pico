from machine import Pin
from time import sleep

pico_led = Pin("LED", Pin.OUT)
pico_led.value(1)
sleep(2)
pico_led.value(0)

led = Pin(15, Pin.OUT)
button = Pin(16, Pin.IN, Pin.PULL_UP)

while True:
    if button.value()==0:
        led.value(1)
    else:
        led.value(0)