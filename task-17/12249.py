with open(r'.\files\17_12249.txt') as file:
    data = [int(i) for i in file]

max3 = max(i for i in data if len(str(abs(i))) == 5 and abs(i) % 10 == 3)
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    cond1 = abs(num1) % 10 == 3
    cond2 = abs(num2) % 10 == 3
    cond3 = abs(num3) % 10 == 3
    if cond1 + cond2 + cond3 >= 1 and num1 + num2 + num3 <= max3:
        ans += [num1 + num2 + num3]
print(len(ans), max(ans))
