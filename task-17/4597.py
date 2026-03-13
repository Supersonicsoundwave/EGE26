with open(r'.\files\17_4597.txt') as file:
    data = [int(i) for i in file]

minn = min(data)

ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i:i + 2]
    cond1 = num1 % 117 == minn
    cond2 = num2 % 117 == minn
    if cond1 + cond2 >= 1:
        ans += [num1 + num2]
print(len(ans), max(ans))

################################################

with open(r'.\files\17_4597.txt') as file:
    data = [int(i) for i in file]

minn = min(data)

ans = []
for num1, num2 in zip(data, data[1:]):
    cond1 = num1 % 117 == minn
    cond2 = num2 % 117 == minn
    if cond1 + cond2 >= 1:
        ans += [num1 + num2]
print(len(ans), max(ans))

