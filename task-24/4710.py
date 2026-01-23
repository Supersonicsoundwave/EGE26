from re import finditer


with open(r'.\files\24_4710.txt') as file:
    data = file.readline()

# перебор
ans = 0
for i in range(len(data) - 1):
    if data[i] in 'CDF' and data[i + 1] in 'AO':
        cnt = 1
        for j in range(i + 2, len(data) - 1, 2):
            if data[j] in 'CDF' and data[j + 1] in 'AO':
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)

# регулярки
pattern = r'([CDF][AO])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)

# замена
for i in 'CDF':
    data = data.replace(i, '!')
for i in 'AO':
    data = data.replace(i, '*')
data = data.replace('!*', '$')
for i in '!*':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))
