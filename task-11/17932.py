from math import *


for N in range(100000, 0, -1):
    i = ceil(log2(N))
    I = ceil(211 * i / 8)
    if 23_654 * I <= 3_241 * 2 ** 10:
        print(N)
        break



