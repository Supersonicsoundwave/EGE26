from math import *


for L in range(1, 10**10):
    N = 17 + 10
    i = ceil(log2(N))
    V = ceil(L * i / 8)
    if 7_564_230 * V > 31 * 2 ** 20:
        print(L)
        break

