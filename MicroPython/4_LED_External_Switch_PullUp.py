# LED External With Switch

from machine import Pin
from time import sleep

pico_led = Pin("LED", Pin.OUT)
pico_led.value(1)
sleep(2)
pico_led.value(0)

led = Pin(15, Pin.OUT)
button = Pin(16, Pin.IN, Pin.PULL_UP)

while True:
    if button.value():
        led.toggle()
        time.sleep(0.5)
        print("1")