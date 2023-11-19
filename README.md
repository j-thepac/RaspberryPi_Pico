# Raspberry Pi Pico
## Micro Python:
	1. Open Source
	2. Modules are cheaper 	
## Circuit Python : 
	1. Fork of Micro Python 
	2. Owned by Ada Fruit
	3. Compatible with Only Ada Fruit Modules
	4. Expensive 
	5. No ConCurrency and No State Sharing 
	
## Pre- Req:
1.  Download the below files Micro Python / Circuit Python
	1. Micro Python (**Recommended**) - [MicroPython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython)
	2. Circuit Python UF2 file from - [https://circuitpython.org/board/raspberry_pi_pico/](https://circuitpython.org/board/raspberry_pi_pico/)
2.  Hold  Raspberry Pi Pico on-board BOOTSEL button (Button on the board)
3.  Plug it into USB (or pulling down the RUN/Reset pin to ground)
4.  It will appear as a USB disk drive
5.  you can copy paste the firmware onto drive
6.  the drive will change for Circuit python and no reaction for Micro Python

## Micro  Python :
1. Install and open thonny IDE
2. IDE should automatically detect pico  


## Circuit Python :
Configure Mu Editor so that Code can be seen running in real time., ie as soon as the code is saved , the result reflected in LEDs directly .
1.  sudo apt-get update
2.  sudo apt-get -f upgrade
3.  apt install libfuse2
4.  Download and Install Mu Editor
### Run
1.  Copy paste below program into code.py
2.  Save the file in the device
3. Open Mu Editor
4.  Should automatically recognise PICO and Opens code.py



https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/blinky-and-a-button
https://www.youtube.com/watch?v=nYA4PVljE4Q