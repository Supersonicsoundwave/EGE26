from re import finditer
from string import printable, ascii_lowercase


with open(r'.\files\24_9791.txt') as file:
    data = file.readline()

# перебор
data = data.lower()
ans = 0
for i in range(len(data)):
    if data[i] in printable[1:16]:
        cnt = 1
        for j in range(i + 1, len(data)):
            if data[j] in printable[:16]:
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)

# регулярки
pattern = fr'[{printable[1:16]}][{printable[:16]}]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# замена
data = data.replace('0', '!')
for i in printable[1:16]:
    data = data.replace(i, '*')

for i in ascii_lowercase:
    data = data.replace(i, ' ')

data = data.split()
data = [x[1:] if x[0] == '!' else x for x in data]
print(len(max(data, key=len)))
