from re import *


with open(r'.\files\24_1205.txt') as file:
    data = file.readline()

# перебор
ans = 0
cnt = 0
for i in data:
    if i not in 'GWP':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)

# регулярки
pattern = r'[^GWP]+'
res = [match.group() for match in finditer(pattern, data)]
print(len(max(res, key=len)))


# замена
for i in 'GWP':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))