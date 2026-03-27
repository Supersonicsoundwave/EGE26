with open(r'.\files\17_15333.txt') as file:
    data = [int(i) for i in file]

max19 = max(num for num in data if num % 19 == 0)
ans = []
for nums in zip(data, data[1:]):
    if sum(num > max19 for num in nums):
        ans += [sum(nums)]
print(len(ans), max(ans))
