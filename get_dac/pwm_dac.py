import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_bits, pwm_freq, dyn_rg, verbose = False):
        self.gpio_bits = gpio_bits
        self.pwm_freq = pwm_freq
        self.dyn_rg = dyn_rg
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
        self.pwm = GPIO.PWM(self.gpio_bits, self.pwm_freq)
        self.pwm.start(0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_volt(self, volt):
        if not (0.0 <= volt <= self.dyn_rg):
            print(f'Напряжение выходит за динамический диапазон ЦАП(0.0 - {self.dyn_rg:.2f} В')
            print('Устанавливаем 0,0 В')
            return 0
        duty = int(volt / self.dyn_rg * 100)
        print(round(volt / self.dyn_rg * 100, 2))
        self.pwm.ChangeDutyCycle(duty)

    '''def set_num(self, num):
        bits = [int(element) for element in bin(num)[2:].zfill(8)]
        GPIO.output(self.gpio_bits, bits)'''
    
if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.293, True)

        while True:
            try:
                volt = float(input("Введите напрядение в Вольтах: "))
                dac.set_volt(volt)
                print(dac.gpio_bits)

            except ValueError:
                print("Вы введи не число.  Попробуйте ещё раз\n")
    finally:
        dac.deinit()

#pwm = GPIO.PWM(led, 200)
#pwm.ChangeDutyCycle(duty)
#print(dac.gpio_bits)






