with open(r'.\files\17_1970.txt') as file:
    data = [int(i) for i in file]

ans = []
for num1, num2 in zip(data, data[1:]):
    cond1 = abs(num1) % 3 == 0
    cond2 = abs(num2) % 3 == 0
    if cond1 + cond2 >= 1:
        ans += [num1 + num2]
print(len(ans), max(ans))
