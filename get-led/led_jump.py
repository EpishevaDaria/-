import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
up = 9
down = 10
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
GPIO.output(leds, 0)
light_time = 0.2

while True:
    for led in leds:
        GPIO.output(led, 1)
        time.sleep(light_time)
        GPIO.output(led, 0)



