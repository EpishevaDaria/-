import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dyn_rg, verbose = False):
        self.gpio_bits = gpio_bits
        self.dyn_rg = dyn_rg
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_volt(self, volt):
        if not (0.0 <= volt <= self.dyn_rg):
            print(f'Напряжение выходит за динамический диапазон ЦАП(0.0 - {self.dyn_rg:.2f} В')
            print('Устанавливаем 0,0 В')
            return 0
        num = int(volt / self.dyn_rg * 255)
        bits = [int(element) for element in bin(num)[2:].zfill(8)]
        print(bits)
        GPIO.output(self.gpio_bits, bits)

    def set_num(self, num):
        bits = [int(element) for element in bin(num)[2:].zfill(8)]
        GPIO.output(self.gpio_bits, bits)
    
if __name__ == "__main__":
    try:
        dac = R2R_DAC([26, 20, 19, 16, 13, 12, 25, 11], 3.217, True)
        print(dac)

        while True:
            try:
                volt = float(input("Введите напрядение в Вольтах: "))
                dac.set_volt(volt)

            except ValueError:
                print("Вы введи не число.  Попробуйте ещё раз\n")
    finally:
        dac.deinit()
            
    
