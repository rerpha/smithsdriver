import machine


pin = machine.Pin(1)
pwm = machine.PWM(pin)

# todo: need to determine this
pwm.freq(1000)

while True:
    value = int(input("Enter PWM duty (0-255): "))
    pwm.duty_u16((value << 8) | value)
