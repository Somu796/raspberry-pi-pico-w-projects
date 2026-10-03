from time import sleep

from machine import ADC, Pin

# Potentiometer pin
pot_pin = 28

# Voltage scale
volt_read_scale = 100  # 3.3, we can read between 3.3-0, 100-0 or any y-0

# GPIO pin
green_led_pin = 13
yellow_led_pin = 14
red_led_pin = 9

my_pot_pin: ADC = ADC(pot_pin)
green_led: Pin = Pin(green_led_pin, Pin.OUT)
yellow_led: Pin = Pin(yellow_led_pin, Pin.OUT)
red_led: Pin = Pin(red_led_pin, Pin.OUT)

safe_limit = 79
warning_limit = 95

try:
    while True:
        pot_reading: int = my_pot_pin.read_u16()
        voltage_cal: float = max(
            0,
            min((100 / 65106) * pot_reading - ((430 * 100) / 65106), 100),
        )
        print(f"Potentiometer Reading: {voltage_cal}")

        # Turn off all LEDs
        green_led.value(0)
        yellow_led.value(0)
        red_led.value(0)

        # safe
        if voltage_cal <= safe_limit:
            green_led.value(1)
        # warning
        elif safe_limit < voltage_cal < warning_limit:
            yellow_led.value(1)
        # danger
        elif voltage_cal >= warning_limit:
            red_led.value(1)
        else:
            raise ValueError("There is a issue with reading volts")

        sleep(0.5)
except KeyboardInterrupt:
    # Turn off all LEDs
    green_led.value(0)
    yellow_led.value(0)
    red_led.value(0)
    print("\nStopped. All LEDs off.")
