from re import *


with open(r'.\files\24_1975.txt') as file:
    data = file.readline()

# перебор
ans = 0
cnt = 1
for i in range(len(data) - 1):
    if data[i] + data[i + 1] != 'PP':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
ans = max(ans, cnt)
print(ans)

# регулярки

pattern = r'[^P]*(P[^P]+)+P?'
matches = finditer(pattern, data)
res = [match.group() for match in matches]
print(len(max(res, key=len)))

# замена
while 'PP' in data:
    data = data.replace('PP', 'P P')

data = data.split()
print(len(max(data, key=len)))

