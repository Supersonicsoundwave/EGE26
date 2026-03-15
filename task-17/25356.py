with open(r'.\files\17_25356.txt') as file:
    data = [int(i) for i in file]

max30 = max(i for i in data if abs(i) % 100 == 30)
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    cond1 = len(str(abs(num1))) == 4
    cond2 = len(str(abs(num2))) == 4
    cond3 = len(str(abs(num3))) == 4
    if cond1 + cond2 + cond3 == 0 and num1 + num2 + num3 > max30:
        ans += [num1 + num2 + num3]
print(len(ans), max(ans))
