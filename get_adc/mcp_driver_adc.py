import smbus as sm
import time
import RPi.GPIO as GPIO

class MCP_ADC:
    def __init__ (self, dyn_rg, verbose = False):
        self.bus = sm.SMBus(1)
        self.dyn_rg = dyn_rg
        self.adress = 0x4D
        self.verbose = verbose

    def deinit(self):
        self.bus.close()

    def get_num(self):
        data = self.bus.read_word_data(self.adress, 0)
        lower_byte = data >> 8
        upper_byte = data & 0xFF
        num = (upper_byte << 6) | (lower_byte >> 2)
        if self.verbose:
            print(f'принятые данные: {data}, Старшй байт: {upper_byte: x}, Младший байт: {lower_byte: x}, Число: {num} ')
        return(num)

    def get_volt(self):
        num = self.get_num()
        volt = round(num/(2**10 -1) * self.dyn_rg, 3)
        return(volt)

try:
    mcp = MCP_ADC(2.787)
    while True:
        volt = mcp.get_volt()
        print(volt)
        time.sleep(1)
finally:
    mcp.deinit()
# Remote I/o error, before that - connection timed out error
