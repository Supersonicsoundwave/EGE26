from math import prod


with open(r'.\files\17_3749.txt') as file:
    data = [int(i) for i in file]

squares = [i ** 2 for i in range(1, 1000)]
max3 = max(i for i in data if i in squares) * 3
ans = []
for nums in zip(data, data[1:]):
    cond1 = prod(nums) ** 0.5 % 1 == 0
    cond2 = sum(num <= max3 for num in nums)
    if cond1 and cond2 >= 1:
        ans += [prod(nums) ** 0.5]
print(len(ans), max(ans) + min(ans))
