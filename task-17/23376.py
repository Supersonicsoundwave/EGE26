with open(r'.\files\17_23376.txt') as file:
    data = [int(i) for i in file]


max37 = max(num for num in data if len(str(abs(num))) == 5 and abs(num) % 100 == 37)
ans = []
for nums in zip(data, data[1:]):
    cond1 = sum(len(str(abs(num))) == 5 for num in nums) == 1
    cond2 = sum(nums) ** 2 > max37 ** 2
    if cond1 and cond2:
        ans += [sum(nums)]
print(len(ans), max(ans))
