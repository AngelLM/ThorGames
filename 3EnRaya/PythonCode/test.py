import math
import time

import sys
import serial
import glob


puerto0='/dev/ttyACM0'

time.sleep(2)

s0=serial.Serial(puerto0,9600)
s0.close()
s0.open()
while True:
    print list(s0.readline())

s0.close()

# s0.write(('M17 \n').encode('UTF-8'))
# s1.write(('M17 \n').encode('UTF-8'))
