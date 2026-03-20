with open(r'.\files\17_17636.txt') as file:
    data = [int(i) for i in file]

max3 = max(i for i in data if abs(i) % 10 == 3 and len(str(abs(i))) == 3)
ans = []
for nums in zip(data, data[1:], data[2:]):
    cond = sum(abs(num) % 10 == 3 and len(str(abs(num))) == 3 for num in nums)
    if cond >= 1 and sum(nums) < max3:
        ans += [sum(nums)]

print(len(ans), max(ans))
