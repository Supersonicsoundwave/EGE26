from math import *


for N in range(1, 100000):
    i = ceil(log2(N))
    I = ceil(377 * i / 8)
    if 23155 * I > 5536 * 1024:
        print(N)
        break
