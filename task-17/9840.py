with open(r'.\files\17_9840.txt') as file:
    data = [int(i) for i in file]

max39 = max(i for i in data if len(str(abs(i))) == 4 and abs(i) % 100 == 39)
ans = []
for nums in zip(data, data[1:]):
    cond = sum(len(str(abs(num))) == 4 for num in nums)
    if cond == 1 and sum(nums) ** 2 <= max39 ** 2:
        ans += [sum(nums)]

print(len(ans), max(ans))
