with open(r'.\files\17_2997.txt') as file:
    data = [int(i) for i in file]


nums_3 = [int(str(abs(i))[1]) for i in data if len(str(abs(i))) == 3]
moda = max(range(10), key=lambda x: nums_3.count(x))
ans = []
for nums in zip(data, data[1:]):
    cond = sum(abs(num) % 10 == moda for num in nums)
    if cond:
        ans += [sum(nums)]
print(len(ans), max(ans))
