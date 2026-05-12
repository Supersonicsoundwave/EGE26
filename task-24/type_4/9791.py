from re import finditer
from string import printable


with open(r'.\files\24_9791.txt') as file:
    data = file.readline()

# регулярка
pattern = fr'[1-9A-F][0-9A-F]*|0'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# перебор
ans = 0
checkpoint = 0
for i in range(len(data)):
    if i < checkpoint:
        continue
    if data[i] in printable[1:16].upper():
        cnt = 1
        for j in range(i + 1, len(data)):
            if data[j] in printable[:16].upper():
                cnt += 1
            else:
                checkpoint = j
                break
        ans = max(ans, cnt)
print(ans)

# замена 1
for i in printable[16:36].upper():
    data = data.replace(i, ' ')

data = data.split()

ans = 0
for num in data:
    if num != '0':
        num = num.lstrip('0')
    ans = max(ans, len(num))

print(ans)

# замена 2
for i in printable[16:36].upper():
    data = data.replace(i, ' ')

data = ' ' + data
while ' 0' in data:
    data = data.replace(' 0', ' ')
data = data.split()
print(len(max(data, key=len)))

