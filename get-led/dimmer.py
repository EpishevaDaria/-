import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 12
GPIO.setup(led, GPIO.OUT)
pwm = GPIO.PWM(led, 200)
duty = 0.0
pwm.start(duty)
step = 0.05

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(step)

    duty+=1.0
    if duty > 100.0:
        duty = 0



