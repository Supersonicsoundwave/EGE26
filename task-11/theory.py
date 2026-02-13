from math import *


# 1855
L = 101
N = 10 + 4090
i = ceil(log2(N)) # bite
I = ceil(L * i / 8) # byte
print(ceil(2048 * I / 2 ** 10))

# 23270
for L in range(1, 10**9):
    N = 10 + 27
    i = ceil(log2(N)) # bite
    I = ceil(L * i / 8) # byte
    if 3548 * I > 12 * 2 ** 10:
        print(L)
        break

# 23195
for N in range(1, 10**10):
    L = 172
    i = ceil(log2(N)) # bit
    I = ceil(L * i / 8) # byte
    if 356_984 * I >= 54 * 2 ** 20:
        print(N)
        break

