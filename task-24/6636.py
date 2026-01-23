from re import finditer


with open(r'.\files\24_6636.txt') as file:
    data = file.readline()

# перебор
ans = 0
for i in range(len(data) - 1):
    if data[i] in '24' and data[i + 1] in '135':
        cnt = 1
        for j in range(i + 2, len(data) - 1, 2):
            if data[j] in '24' and data[j + 1] in '135':
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)

# регулярки
pattern = r'([24][135])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)

# замена
for i in '24':
    data = data.replace(i, '*')
for i in '135':
    data = data.replace(i, '!')
data = data.replace('*!', '$')
data = data.replace('*', ' ')
data = data.replace('!', ' ')
data = data.split()
print(len(max(data, key=len)))
