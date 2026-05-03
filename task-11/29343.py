from math import *


i = ceil(log2(17+4080))
I = ceil(257 * i / 8)
print(8_388_608 * I / 2 ** 20)
