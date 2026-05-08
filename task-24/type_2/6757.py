from re import finditer


with open(r'.\files\24_6757.txt') as file:
    data = file.readline()

# перебор
ans = 0
for i in range(len(data) - 2):
    if data[i:i + 3] in 'CFE FCE':
        cnt = 1
        for j in range(i + 3, len(data) - 1, 3):
            if data[j:j + 3] in 'CFE FCE':
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)


# регулярка
pattern = r'(CFE|FCE)+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 3)

# замена
data = data.replace('CFE', '*')
data = data.replace('FCE', '*')
for i in set(data):
    if i != '*':
        data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))
