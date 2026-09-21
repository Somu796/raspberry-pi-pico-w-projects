from machine import Pin
from time import sleep

myLED=Pin('LED', Pin.OUT)
myLED.value(0)
time=0.01
while True:
    sleep(time)
    myLED.value(1)
    sleep(time)
    myLED.value(0)