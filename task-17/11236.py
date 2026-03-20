from math import prod


with open(r'.\files\17_11236.txt') as file:
    data = [int(i) for i in file]

min2 = min(i for i in data if len(str(abs(i))) == 2)
max41 = max(i for i in data if len(str(abs(i))) == 4 and abs(i) % 10 == 1)
ans = []
for nums in zip(data, data[1:], data[2:]):
    cond1 = sum(num > min2 ** 2 for num in nums)
    cond2 = abs(prod(nums)) % max41 == 0
    if cond1 == 2 and cond2:
        ans += [sum(abs(i) for i in nums)]
print(len(ans), max(ans))
