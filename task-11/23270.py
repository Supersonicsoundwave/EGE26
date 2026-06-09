from math import *


for L in range(1, 10000):
    N = 10 + 27
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 3548 * I > 12 * 1024:
        print(L)
        break