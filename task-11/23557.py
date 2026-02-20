from math import *


for L in range(1, 10**20):
    N = 10 + 52 + 500
    i = ceil(log2(N))
    I = ceil(L * i / 8) # byte
    if 45877 * I > 49 * 2 ** 20:
        print(L)
        break