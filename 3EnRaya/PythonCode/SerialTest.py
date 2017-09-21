import math
import time

import sys
import serial
import glob


puerto0='/dev/ttyUSB0'
puerto1='/dev/ttyACM0'

s0=serial.Serial(puerto1,9600)
s0.close()
s0.open()
time.sleep(2)
s0.write(("p").encode('UTF-8'))
print s0.readline()
print "Ya lo he impreso."


s0.close()
