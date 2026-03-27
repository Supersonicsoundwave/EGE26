from math import *


for N in range(1, 10000):
    i = ceil(log2(N))
    I = ceil(i * 172 / 8)
    if 356_984 * I >= 54 * 2 ** 20:
        print(N)
        break
