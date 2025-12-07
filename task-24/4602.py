from re import *


with open(r'.\files\24_4602.txt')as file:
    data = file.readline()

pattern = r'([BCD][AO])+'
res = [match.group() for match in finditer(pattern, data)]
print(len(max(res, key=len)) // 2)

ans = 0
for i in range(len(data) - 1):
    if data[i] in 'BCD' and data[i + 1] in 'AO':
        cnt = 1
        for j in range(i + 2, len(data) - 1, 2):
            if data[j] in 'BCD' and data[j + 1] in 'AO':
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)

for i in 'BCD':
    for j in 'AO':
        data = data.replace(f'{i}{j}', '*')
for i in 'ABCDO':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))