import board
import time
from digitalio import DigitalInOut, Direction,Pull

op = DigitalInOut(board.GP0)
op.direction = Direction.OUTPUT

while 1:
    if op.value==0: op.value= True
    elif op.value==1:op.value = False
    time.sleep(0.5)