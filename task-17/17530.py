with open(r'.\files\17_17530.txt') as file:
    data = [int(i) for i in file]

mn = min(data)
ans = []
for nums in zip(data, data[1:]):
    if sum(num % 55 == mn for num in nums) >= 1:
        ans += [sum(nums)]

print(len(ans), min(ans))
