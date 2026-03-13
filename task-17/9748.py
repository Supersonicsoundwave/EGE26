with open(r'.\files\17_9748.txt') as file:
    data = [int(i) for i in file]

max15 = max(i for i in data if i % 100 == 15)
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    cond1 = 1000 <= num1 <= 9999
    cond2 = 1000 <= num2 <= 9999
    cond3 = 1000 <= num3 <= 9999
    cond4 = sum((num1, num2, num3)) >= max15
    if cond1 + cond2 + cond3 == 1 and cond4:
        ans += [sum((num1, num2, num3))]
print(len(ans), max(ans))
