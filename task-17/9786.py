with open(r'.\files\17_9786.txt') as file:
    data = [int(i) for i in file]

max25 = max(i for i in data if abs(i) % 100 == 25)
ans = []
for nums in zip(data, data[1:], data[2:]):
    cond = sum(len(str(abs(num))) == 4 for num in nums)
    if cond <= 2 and sum(nums) <= max25:
        ans += [sum(nums)]

print(len(ans), max(ans))
