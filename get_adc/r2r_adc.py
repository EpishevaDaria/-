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
        while num < 256:
            self.num_to_dac(num)
            time.sleep(self.comp_time)
            if GPIO.input(self.comp_gpio):
                return(num)
            num += 1
        return(255)
        
    def get_sc_volt(self):
        num = self.seq_count_adc()
        volt = round(num/255 * self.dyn_rg, 3)
        return(volt)

    def succ_appr_volt(self):
        bits = [0] * 8
        k = 0
        while k < 8:
            #print(bits)
            bits[k] = 1
            bits_st = ''.join(map(str, bits))
            num = int(bits_st, 2)
            #print(num)
            self.num_to_dac(num)
            time.sleep(self.comp_time)
            if GPIO.input(self.comp_gpio):
                bits[k] = 0
                k += 1
                continue
            else:
                bits[k] = 1
            k += 1
        #print(bits)
        bits = ''.join(map(str, bits))
        return(int(bits, 2))

    def get_sar_volt(self):
        num = self.succ_appr_volt()
        volt = round(num/255 * self.dyn_rg, 3)
        return(volt)


if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.294, verbose = True)

        while True:
            try:
                volt = adc.get_sar_volt()
                print(volt)

            except ValueError:
                print("Вы введи не число.  Попробуйте ещё раз\n")
    finally:
        adc.deinit()
            
    