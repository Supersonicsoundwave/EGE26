with open(r'.\files\17_23902.txt') as file:
    data = [int(i) for i in file]

ans = []
for nums in zip(data, data[1:], data[2:]):
    cond1 = sum(str(abs(num))[0] == str(abs(num))[-1] for num in nums)
    cond2 = sum(len(str(abs(num))) == 4 and str(abs(num))[-3] == '2' for num in nums)
    if cond1 == 1 and cond2 == 2:
        ans += [max(nums)]

print(len(ans), sum(ans))
