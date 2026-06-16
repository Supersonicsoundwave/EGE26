from math import *


for N in range(1, 10**10) :
    L = 172
    i = ceil(log2(N))
    V = ceil(L * i / 8)
    if 356984 * V >= 54 * 2 ** 20:
        print(N)
        break
