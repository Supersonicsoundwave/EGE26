with open(r'.\files\17_23905.txt') as file:
    data = [int(i) for i in file]

max37 = max(num for num in data if num % 100 == 37)
ans = []
for nums in zip(data, data[1:], data[2:], data[3:]):
    cond1 = sum(num > max37 for num in nums) == 2
    cond2 = sum(str(num)[-1] == str(num)[-2] for num in nums if len(str(num)) >= 2) == 1
    if cond1 and cond2:
        ans += [num for num in nums if len(str(num)) >= 2 and str(num)[-1] == str(num)[-2]]
print(len(ans), sum(ans))
