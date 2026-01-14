from re import finditer
from string import ascii_uppercase, digits


with open(r'.\files\24_4642.txt') as file:
    data = file.readline()

# перебор
ans = 0
for i in range(0, len(data) - 1):
    if data[i].isalpha() and data[i  + 1].isdigit():
        cnt = 1
        for j in range(i + 2, len(data) - 1, 2):
            if data[j].isalpha() and data[j  + 1].isdigit():
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)

# регулярки
pattern = r'([AB][12])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)

# замена
for i in ascii_uppercase:
    data = data.replace(i, '*')
for i in '12':
    data = data.replace(i, '!')

data = data.replace('*!', '&')
data = data.replace('!', ' ')
data = data.replace('*', ' ')
data = data.split()
print(len(max(data, key=len)))
