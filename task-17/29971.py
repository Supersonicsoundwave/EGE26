with open(r'.\files\17_29971.txt') as file:
    data = [int(i) for i in file]

max33 = max(n for n in data if abs(n) % 100 == 33)
ans = []
for nums in zip(data, data[1:], data[2:]):
    cond1 = sum(len(str(abs(num))) == 2 for num in nums) == 2
    cond2 = sum(nums) ** 2 < max33
    if cond1 and cond2:
        ans += [sum(nums)]
print(len(ans), max(ans))
