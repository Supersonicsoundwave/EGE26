with open(r'.\files\17_23201.txt') as file:
    data = [int(i) for i in file]

min7 = min(num for num in data if num % 10 == 7 and len(str(num)) == 3)
ans = []
for nums in zip(data, data[1:]):
    cond1 = sum(len(str(num)) == 3 for num in nums) == 1
    cond2 = sum(nums) % min7 == 0
    if cond1 and cond2:
        ans += [sum(nums)]

print(len(ans), min(ans))
