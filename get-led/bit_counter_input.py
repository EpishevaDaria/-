def dec2bin(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]

print(type(dec2bin(45)), dec2bin(45))

