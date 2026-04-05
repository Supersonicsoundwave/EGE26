with open(r'.\files\17.txt') as file:
    data = [int(i) for i in file]


max2 = max(num for num in data if 9 < num < 100)
ans = []
for nums in zip(data, data[1:]):
    cond1 = sum(9 < num < 100 for num in nums) == 1
    cond2 = sum(nums) % max2 == 0
    if cond1 and cond2:
        ans += [sum(nums)]

print(len(ans), max(ans))
