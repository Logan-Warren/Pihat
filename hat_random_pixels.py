#!/usr/bin/env python
#this script will generate a random number for the x and y axis for a single pixle
# and turn the pixel on and off using random colors
from sense_hat import SenseHat
import time
import random
sense = SenseHat()

r = random.radint(0, 7)

sense.set_pixel(5, 5 (r, r, r))
time.sleep(1)
sense.set_pixel(5, 5 (0, 0, 0))
time.sleep(1)
sense.clear()
