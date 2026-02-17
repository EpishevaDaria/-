import smbus as sm
import RPi.GPIO as GPIO

class MCP_:
    def __init__(self, dyn_rg, adress = 0x61, verbose = True):
        self.bus = sm.SMBus(1)

        self.adress = adress
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dyn_rg = dyn_rg

    def deinit(self):
        self.bus.close()

    def set_num(self, num):
        if not isinstance(num, int):
            print("На выход ЦАП можно подавать только целые числа")

        if not (0 <= num <= 4095):
            print("Число выходит за разрядность VCP4752 (12 бит)")
        
        byte_1 = self.wm | self.pds | num >> 8 
        byte_2 = num & 0xFF
        self.bus.write_byte_data(0x61, byte_1, byte_2)

        if self.verbose:
            print(f"Число {num}, отправленные по IC2 данные: [0x{(self.adress << 1): 02X}, 0x{byte_1:02X}, 0x{byte_2:02X}]\n ")
    
    def set_volt(self, volt):
        if not (0.0 <= volt <= self.dyn_rg):
            print(f'Напряжение выходит за динамический диапазон ЦАП(0.0 - {self.dyn_rg:.2f} В')
            print('Устанавливаем 0,0 В')
            return 0
        nums = int(volt / self.dyn_rg * 4095)
        self.set_num(nums)

if __name__ == "__main__":
    try:
        dac = MCP_(dyn_rg = 5.1, verbose = True)

        while True:
            try:
                volt = float(input("Введите напрядение в Вольтах: "))
                dac.set_volt(volt)

            except ValueError:
                print("Вы введи не число.  Попробуйте ещё раз\n")
    finally:
        dac.deinit()



