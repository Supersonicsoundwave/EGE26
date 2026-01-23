from math import log


for x in range(1, 8):
    a = int(f'{x}1{x}', 16)
    b = int(f'{x}3{x}3', 8)
    f = a + b
    if log(f, 2) % 1 == 0:
        print(x)