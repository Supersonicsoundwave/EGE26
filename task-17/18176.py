with open(r'.\files\17_18176.txt') as file:
    data = [int(i) for i in file]

min4 = min(num for num in data if num > 0 and num % 10 == 4)
ans = []
for nums in zip(data, data[1:], data[2:]):
    line = ''.join(map(lambda x: str(abs(x)), nums))
    if sum(int(i) for i in line) == min4:
        ans += [sum(nums)]
print(len(ans), max(ans))
