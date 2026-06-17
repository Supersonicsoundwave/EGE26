with open(r'.\files\17_29349.txt') as file:
    data = [int(i) for i in file]

min123 = min(i for i in data if i > 0 and i % 123 == 0)
ans = []
for nums in zip(data, data[1:]):
    cond1 = sum(nums) < min123
    if cond1:
        ans += [sum(nums)]

print(len(ans), abs(max(ans)))
