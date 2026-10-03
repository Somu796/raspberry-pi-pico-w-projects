from time import sleep

from machine import ADC, Pin

# Potentiometer pin
pot_pin = 28

my_pot_pin: ADC = ADC(pot_pin)
my_led: Pin = Pin("LED", Pin.OUT)

while True:
    my_led.toggle()
    pot_reading: int = my_pot_pin.read_u16()
    voltage_cal: float = max(
        0,
        min((3.3 / 65106) * pot_reading - ((430 * 3.3) / 65106), 3.3),
    )
    print(f"Potentiometer Reading: {voltage_cal}")
    sleep(0.5)
