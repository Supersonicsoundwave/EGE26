with open(r'.\files\17_2473.txt') as file:
    data = [int(i) for i in file]

ans = []
for num1, num2 in zip(data, data[1:]):
    cond11 = abs(num1) % 7 == 0
    cond12 = abs(num2) % 7 == 0
    cond21 = abs(num1) % 10 == 3
    cond22 = abs(num2) % 10 == 3
    if cond11 + cond12 >= 1 and cond21 + cond22 >= 1:
        ans += [num1 + num2]

print(len(ans), min(ans))
