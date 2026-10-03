from time import sleep

from machine import Pin

pin12 = Pin(12, Pin.OUT)
pin13 = Pin(13, Pin.OUT)
pin14 = Pin(14, Pin.OUT)
pin15 = Pin(15, Pin.OUT)

pin12.value(0)
pin13.value(0)
pin14.value(0)
pin15.value(0)

# wait_time = 1

# while True:
#     pin12.value(0)
#     pin13.value(0)
#     pin14.value(0)
#     pin15.value(0)
#     sleep(wait_time)

#     pin12.value(1)
#     pin13.value(0)
#     pin14.value(0)
#     pin15.value(0)
#     sleep(wait_time)

#     pin12.value(0)
#     pin13.value(1)
#     pin14.value(0)
#     pin15.value(0)
#     sleep(wait_time)

#     pin12.value(1)
#     pin13.value(1)
#     pin14.value(0)
#     pin15.value(0)
#     sleep(wait_time)

#     pin12.value(0)
#     pin13.value(0)
#     pin14.value(1)
#     pin15.value(0)
#     sleep(wait_time)

#     pin12.value(1)
#     pin13.value(0)
#     pin14.value(1)
#     pin15.value(0)
#     sleep(wait_time)

#     pin12.value(0)
#     pin13.value(1)
#     pin14.value(1)
#     pin15.value(0)
#     sleep(wait_time)

#     pin12.value(1)
#     pin13.value(1)
#     pin14.value(1)
#     pin15.value(0)
#     sleep(wait_time)

#     pin12.value(0)
#     pin13.value(0)
#     pin14.value(0)
#     pin15.value(1)
#     sleep(wait_time)

#     pin12.value(1)
#     pin13.value(0)
#     pin14.value(0)
#     pin15.value(1)
#     sleep(wait_time)

#     pin12.value(0)
#     pin13.value(1)
#     pin14.value(0)
#     pin15.value(1)
#     sleep(wait_time)

#     pin12.value(1)
#     pin13.value(1)
#     pin14.value(0)
#     pin15.value(1)
#     sleep(wait_time)

#     pin12.value(0)
#     pin13.value(0)
#     pin14.value(1)
#     pin15.value(1)
#     sleep(wait_time)

#     pin12.value(1)
#     pin13.value(0)
#     pin14.value(1)
#     pin15.value(1)
#     sleep(wait_time)

#     pin12.value(0)
#     pin13.value(1)
#     pin14.value(1)
#     pin15.value(1)
#     sleep(wait_time)

#     pin12.value(1)
#     pin13.value(1)
#     pin14.value(1)
#     pin15.value(1)
#     sleep(wait_time)
