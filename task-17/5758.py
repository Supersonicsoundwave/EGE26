with open(r'.\files\17_5758.txt') as file:
    data = [int(i) for i in file]

moda = max(data, key=lambda x: data.count(x))
ans = []
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        nums = data[i], data[j]
        cond1 = min(nums) < moda < max(nums)
        cond2 = (j - i - 1) % 2 != 0
        if cond1 and cond2:
            ans += [max(abs(data[i] - moda), abs(data[j] - moda))]
print(len(ans), max(ans))
