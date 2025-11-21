num = 283**382 + 9**15 + 2**3
cntB = 0
cntC = 0
while num:
    if num % 14 == 11:
        cntB += 1
    if num % 14 == 12:
        cntC += 1
    num //= 14
print(abs(cntB - cntC))