from re import finditer


with open(r'.\files\24_1975.txt') as file:
    data = file.readline()

# перебор
ans = 0
cnt = 1
for i in range(len(data) - 1):
    if data[i] + data[i + 1] == 'PP':
        ans = max(ans, cnt)
        cnt = 1
    else:
        cnt += 1
ans = max(ans, cnt)
print(ans)

# регулярка
pattern = r'P?([^P]+P)*[^P]*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# замена
while 'PP' in data:
    data = data.replace('PP', 'P P')
data = data.split()
print(len(max(data, key=len)))


