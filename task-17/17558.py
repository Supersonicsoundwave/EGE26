with open(r'.\files\17_17558.txt') as file:
    data = [int(i) for i in file]

cnt32 = sum(i % 32 == 0 for i in data)
ans = []
for nums in zip(data, data[1:]):
    cond = sum(num < 0 for num in nums)
    if cond >= 1 and sum(nums) < cnt32:
        ans += [sum(nums)]

print(len(ans), max(ans))
