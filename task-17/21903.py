with open(r'.\files\17_21903.txt') as file:
    data = [int(i) for i in file]

min15 = min(i for i in data if abs(i) % 100 == 15 and len(str(abs(i))) == 3)
ans = []
for nums in zip(data, data[1:], data[2:]):
    cond1 = sum(num > 0 for num in nums) in [0, 3]
    cond2 = min(nums) * max(nums) > min15 ** 2
    if cond1 and cond2:
        ans += [min(nums) * max(nums)]

print(len(ans), min(ans))
