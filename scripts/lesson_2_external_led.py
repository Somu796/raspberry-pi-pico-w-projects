from time import sleep, sleep_ms

from machine import Pin

red_led = Pin(15, Pin.OUT)  # type:ignore  # noqa: PGH003

# Run to switch off
red_led.value(0)

# Run to blink
# while True:
#     red_led.value(1)
#     sleep(0.5)
#     red_led.value(0)
#     sleep(0.05)


#  Run to SOS
def dot() -> None:
    red_led.on()
    sleep_ms(200)
    red_led.off()
    sleep_ms(100)


def dash() -> None:
    red_led.on()
    sleep_ms(600)
    red_led.off()
    sleep_ms(100)


while True:
    # S: three dots
    for _ in range(3):
        dot()
    sleep_ms(300)  # letter gap

    # O: three dashes
    for _ in range(3):
        dash()
    sleep_ms(300)  # letter gap

    # S: three dots
    for _ in range(3):
        dot()
    sleep_ms(1000)  # pause before repeating
