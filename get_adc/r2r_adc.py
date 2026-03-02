import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dyn_rg, comp_time = 0.01, verbose = False):
        self.dyn_rg = dyn_rg
        self.comp_time = comp_time
        self.verbose = verbose

        self.gpio_bits = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def num_to_dac(self, num):
        bits = [int(element) for element in bin(num)[2:].zfill(8)]
        GPIO.output(self.gpio_bits, bits)
    
    def seq_count_adc(self):
        num = 0
        while True:
            if num > 255 and not GPIO.input(self.comp_gpio):
                return(255)
                break
            self.num_to_dac(num)
            time.sleep(self.comp_time)
            if GPIO.input(self.comp_gpio):
                return(num)
                break
            num += 1
        
    def get_sc_voltage(self):
        num = self.seq_count_adc()
        volt = round(num/255 * self.dyn_rg, 3)
        return(volt)        


if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.294, verbose = True)

        while True:
            try:
                volt = adc.get_sc_voltage()
                print(volt)

            except ValueError:
                print("Вы введи не число.  Попробуйте ещё раз\n")
    finally:
        adc.deinit()
            
    