
from machine import Pin, Timer
import utime

pin25 = Pin(25, Pin.OUT)
time = Timer()

while True:
    pin25.value(1)
    utime.sleep(1)
    pin25.value(0)
    utime.sleep(.2)

