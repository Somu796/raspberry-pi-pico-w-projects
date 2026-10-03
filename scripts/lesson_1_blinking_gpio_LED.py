from time import sleep

from machine import Pin  # type:ignore  # noqa: PGH003

my_led = Pin("LED", Pin.OUT)
my_led.value(0)

time = 1
while True:
    sleep(time)
    my_led.value(1)
    sleep(time)
    my_led.value(0)
