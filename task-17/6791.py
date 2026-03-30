with open(r'.\files\17_6791.txt') as file:
    data = [int(i) for i in file]

min68 = min(num for num in data if abs(num) % 100 == 68)
ans = []
for nums in zip(data, data[1:]):
    cond1 = sum(abs(num) % 100 == 68 for num in nums) == 1
    cond2 = nums[0] ** 2 + nums[1] ** 2 >= min68 ** 2
    if cond1 and cond2:
        ans += [nums[0] ** 2 + nums[1] ** 2]
print(len(ans), max(ans))
