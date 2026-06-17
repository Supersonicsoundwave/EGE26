with open(r'.\files\17_27629.txt') as file:
    data = [int(i) for i in file]

max43 = max(n for n in data if len(str(abs(n))) == 4 and abs(n) % 100 == 43)
ans = []
for nums in zip(data, data[1:]):
    cond1 = sum(len(str(abs(num))) == 4 for num in nums) >= 1
    cond2 = sum(nums) ** 2 < max43 ** 2
    if cond1 and cond2:
        ans += [sum(nums) ** 2]

print(len(ans), max(ans))
