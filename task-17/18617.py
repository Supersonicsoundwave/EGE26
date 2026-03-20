with open(r'.\files\17_18617.txt') as file:
    data = [int(i) for i in file]

ans = []
mx = max(data)
mn = min(data)
for nums in zip(data, data[1:]):
    cond1 = sum(num % 3 == mx % 3 for num in nums) >= 1
    cond2 = sum(num % 7 == mn % 7 for num in nums) >= 1
    if cond1 and cond2:
        ans += [sum(nums)]
print(len(ans), max(ans))
