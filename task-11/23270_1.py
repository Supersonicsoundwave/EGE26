from math import *


for L in range(1, 10**10):
    N = 27
    i = ceil(log2(N))
    V = ceil(L * i / 8)
    if 3548 * V > 12 * 2 ** 10:
        print(L)
        break
