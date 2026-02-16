import RPi.GPIO as GPIO

def volt_to_num(voltage):
    if not (0.0 <= voltage <= dyn_rg):
        print(f'Напряжение выходит за динамический диапазон ЦАП(0.0 - {dyn_rg:.2f} В')
        print('Устанавливаем 0,0 В')
        return 0
    return int(voltage / dyn_rg * 255)

def num_to_dac(num):
    bits = [int(element) for element in bin(num)[2:].zfill(8)]
    print(bits)
    GPIO.output(pins, bits)


pins = [16, 20, 21, 25, 26, 17, 27, 22]
#pins = pins[::-1]
dyn_rg = 3.146

GPIO.setmode(GPIO.BCM)

GPIO.setup(pins, GPIO.OUT)

try:
    while True:
        try:
            voltage = float(input("Введите напрядение в Вольтах: "))
            num = volt_to_num(voltage)
            num_to_dac(num)
        except ValueError:
            print("Вы введи не число.  Попробуйте ещё раз\n")
finally:
    GPIO.output(pins, 0)
    GPIO.cleanup()







