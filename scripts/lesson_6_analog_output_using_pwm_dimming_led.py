from time import sleep

from machine import PWM, Pin

pwm_out_pin = 9

analog_out = PWM(Pin(pwm_out_pin))

analog_out.freq(1000)
analog_out.duty_u16(0)

max_volt = 3.3
min_volt = 0

try:
    while True:
        voltage_required = float(input("What voltage you want (between 0-3.3V)? "))
        if min_volt <= voltage_required <= max_volt:
            pwm_val_required: int = int((65535 / 3.3) * voltage_required)
            analog_out.duty_u16(pwm_val_required)
        else:
            print("Value out of range")
        sleep(0.1)
except KeyboardInterrupt:
    analog_out.duty_u16(0)
    print("\nSwitched dimmable LED off.")
