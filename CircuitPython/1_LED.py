import board
import time
from digitalio import DigitalInOut, Direction,Pull


led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value= True
time.sleep(0.5)
led.value= False


# #Connect LED between Pin1 ie GP0 and Pin 2
# op = DigitalInOut(board.GP0)
# op.direction = Direction.OUTPUT


# if led.value==0: led.value= True
# time.sleep(0.5)
# elif led.value==1:led.value = False
    
