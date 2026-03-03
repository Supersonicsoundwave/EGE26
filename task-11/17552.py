from math import *


for N in range(1, 1000):
    i = ceil(log2(N))
    I = ceil(261 * i / 8)
    if 252_500 * I > 31 * 2 ** 20:
        print(N)
        break
        