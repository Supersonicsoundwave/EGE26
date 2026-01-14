from re import finditer


with open(r'.\files\24_5139.txt') as file:
    data = file.readline()

# перебор
ans = 0
for i in range(0, len(data) - 2):
    if data[i] in 'BCDF' and data[i + 1] in 'AEU' and data[i + 2] in 'BCDF':
        cnt = 1
        for j in range(i + 3, len(data) - 2, 3):
            if data[j] in 'BCDF' and data[j + 1] in 'AEU' and data[j + 2] in 'BCDF':
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)

# регулярки
pattern = r'([BCDF][AEU][BCDF])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 3)

# замена
for i in 'BCDF':
    data = data.replace(i, '!')
for i in 'AEU':
    data = data.replace(i, '*')

while '!*!*!' in data:
    data = data.replace('!*!*!', '!*! !*!')

data = data.replace('!*!', '&')
data = data.replace('!', ' ')
data = data.replace('*', ' ')
data = data.split()
print(len(max(data, key=len)))
