from re import finditer

with open(r'.\files\24_1866.txt') as file:
    data = file.readline()

# перебор
ans = 0
cnt = 1
for i in range(len(data) - 1):
    if data[i] + data[i + 1] not in ['ad', 'da']:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
ans = max(ans, cnt)
print(ans)

# регулярки
pattern = r'(?<=(ad|da)).+?(?=(ad|da))'
res = [match.group() for match in finditer(pattern, data)]
print(len(max(res, key=len)) + 2)

# замена
data = data.replace('ad', 'a d')
data = data.replace('da', 'd a')
data = data.split()
print(len(max(data, key=len)))

