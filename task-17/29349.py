with open(r'.\files\17_29349.txt') as file:
    data = [int(i) for i in file]

min123 = min(n for n in data if n > 0 and n % 123 == 0)
ans = []
for nums in zip(data, data[1:]):
    if sum(nums) < min123:
        ans += [sum(nums)]

print(len(ans), abs(max(ans)))
