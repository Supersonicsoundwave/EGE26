from typing import dataclass_transform

with open(r'.\files\24_17535.txt') as file:
    data = file.readline()

# метод двух указателей
ans = cnt = l = r = 0
len_data = len(data)
while r < len_data - 1:
    if cnt <= 160:
        if data[r:r + 2] == 'CD':
            cnt += 1
        r += 1
    else:
        if data[l:l + 2] == 'CD':
            cnt -= 1
        l += 1
    ans = max(ans, r - l)
print(ans)


# замена
data = data.replace('CD', 'C D')
data = data.split()

ans = 0
for i in range(len(data) - 160):
    line = ''.join(data[i:i + 161])
    ans = max(ans, len(line))
print(ans)

