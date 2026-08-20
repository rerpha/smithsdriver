import machine
from neopixel import NeoPixel
from time import sleep

p1 = machine.Pin(1)
gauge_pwm = machine.PWM(p1)
# todo: need to work out PWM freq

relay_output_pin = machine.Pin(0, machine.Pin.OUT)

sensor_input_pin = machine.Pin(26)
sensor = machine.ADC(sensor_input_pin)

FAN_ON_TEMP = 90
FAN_OFF_TEMP = 86

# measurements for the two-wire temperature sensor
OHM_TO_CELSIUS = [
    (2031, 20),
    (1286, 30),
    (843.9, 40),
    (569.9, 50),
    (388, 60),
    (277.8, 70),
    (200, 80),
    (146.7, 90),
    (108, 100),
    (82.7, 110),
    (63.5, 120),
]


def interp(r: float) -> float:
    if r > OHM_TO_CELSIUS[0][0]:
        return float(OHM_TO_CELSIUS[0][1])
    if r < OHM_TO_CELSIUS[-1][0]:
        return float(OHM_TO_CELSIUS[-1][1])

    for (x1, y1), (x2, y2) in zip(OHM_TO_CELSIUS, OHM_TO_CELSIUS[1:]):
        if x1 >= r >= x2:
            return y1 + (r - x1) * (y2 - y1) / (x2 - x1)


SENSOR_VCC = 3.3
DIVIDER_OHM = 10000

def main():
    while True:
        
        # read uv
        adc_raw = sensor.read_u16()
        
        if adc_raw == 0:
            print("adc not reading any voltage. continuing...")
            continue
        print(f"adc value: {adc_raw}")
        
        # convert to volts
        adc_v = adc_raw * SENSOR_VCC / 65535
        
        print(f"volts: {adc_v}")
        # convert to resistance
        res = DIVIDER_OHM * adc_v / (SENSOR_VCC - adc_v)
        print(f"resistance: {res}")
        # interpolate it to get degrees C
        temp_c = interp(res)
        print(temp_c)
        
        if temp_c > FAN_ON_TEMP:
            # switch relay on here
            print("switching fan relay on")
            relay_output_pin.on()
        elif temp_c < FAN_OFF_TEMP:
            # switch relay off here
            print("switching fan relay off")
            relay_output_pin.off()
        
        # output PWM to gauge mosfet.
        # todo: need to work out pwm -> gauge needle.
        ...

        # sleep for 0.1s
        sleep(0.1)


main()


