with open(r'.\files\17_28938.txt') as file:
    data = [int(i) for i in file]

max28 = max(n for n in data if abs(n) % 100 == 28)
ans = []
for nums in zip(data, data[1:], data[2:]):
    cond1 = sum(len(str(abs(num))) == 3 for num in nums) >= 1
    cond2 = sum(nums) / 3 > 0
    cond3 = sum(nums) / 3 < max28
    if cond1 and cond2 and cond3:
        ans += [sum(nums)]

print(len(ans), max(ans))
