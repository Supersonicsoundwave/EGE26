num = 16**820 - 2**761 + 14
cnt0 = 0
while num:
    if num % 4 == 0:
        cnt0 += 1
    num //= 4

print(cnt0)
