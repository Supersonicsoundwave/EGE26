with open(r'.\files\17_5758.txt') as file:
    data = [int(i) for i in file]

moda = max((data.count(num), num) for num in data)[-1]
ans = []
for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        nums = data[i], data[j]
        if min(nums) < moda < max(nums) and (j - i - 1) % 2 != 0:
            ans += [abs(moda - min(nums))]

print(len(ans), max(ans))
