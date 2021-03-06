import time
import RPi.GPIO as GPIO
PIN_PWM = 21

def get_co2():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_PWM,GPIO.IN)
    time.sleep(0.2)
    while GPIO.input(PIN_PWM) == 1:
        last_high = time.time()
    while GPIO.input(PIN_PWM) == 0:
        last_low = time.time()
    while GPIO.input(PIN_PWM) == 1:
        last_high = time.time()
    span_high = (last_high - last_low) * 1000
    while GPIO.input(PIN_PWM) == 0:
        last_low = time.time()
    while GPIO.input(PIN_PWM) == 1:
        last_high = time.time()
    while GPIO.input(PIN_PWM) == 0:
        last_low = time.time()
    span_low = (last_low - last_high) * 1000
    CO2 = 5000 * ( span_high - 2 ) / ( span_high + span_low - 4 )
    AQ = "%.0f" % CO2
    GPIO.cleanup()
    return AQ
