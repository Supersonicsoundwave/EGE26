from re import finditer


with open(r'.\files\24_1230.txt') as file:
    data = file.readline()

# перебор
ans = 0
cnt = 0
for i in range(len(data)):
    if data[i] not in 'WRQ':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)

# регулярки
pattern = r'[^QWR]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# замена
for i in 'WRQ':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))
