from math import *


for L in range(1, 1000):
    N = 10 + 17
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 7_564_230 * I > 31 * 2 ** 20:
        print(L)
        break
