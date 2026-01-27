from re import finditer
from string import digits, ascii_uppercase


with open(r'.\files\24_10724.txt') as file:
    data = file.readline()

ans = 0
alph = (digits + ascii_uppercase)[:16]
for i in range(len(data)):
    if data[i] in alph[1:]:
        cnt = 1
        for j in range(i + 1, len(data)):
            if data[j] in alph:
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)

pattern = fr'[{alph[1:]}][{alph}]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

for i in alph:
    if i == '0':
        data = data.replace(i, '!')
    else:
        data = data.replace(i, '*')
for i in ascii_uppercase:
    data = data.replace(i, ' ')
while ' !' in data:
    data = data.replace(' !', ' ')
while data[0] == '!':
    data = data[1:]
data = data.split()
print(len(max(data, key=len)))