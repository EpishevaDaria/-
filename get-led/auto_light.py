import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)
div = 6
GPIO.setup(div, GPIO.IN)
state = 1
while True:
    GPIO.output(led,not GPIO.input(div))
        