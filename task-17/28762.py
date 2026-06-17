with open(r'.\files\17_28762.txt') as file:
    data = [int(i) for i in file]

min23 = min(n for n in data if n % 23 == 0)
ans = []
for nums in zip(data, data[1:]):
    if any(num % min23 == 0 for num in nums):
        ans += [sum(nums)]
print(len(ans), max(ans))
