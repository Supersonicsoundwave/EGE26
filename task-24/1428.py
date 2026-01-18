from re import finditer


with open(r'.\files\24_1428.txt') as file:
    data = file.readline()

# перебор
ans = 0
cnt = 1
for i in range(len(data) - 1):
    if data[i:i + 2] not in ['XY', 'XZ']:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
ans = max(ans, cnt)
print(ans)

# регулярки
pattern = r'(^|(?<=(XZ|XY))).+?($|(?=(XY|XZ)))'
ans = 0
for match in finditer(pattern, data):
    if match.groups().count('XZ') + match.groups().count('XY') == 2:
        ans = max(ans, len(match.group()) + 2)
    else:
        ans = max(ans, len(match.group()) + 1)
print(ans)

# замена
data = data.replace('XY', 'X Y')
data = data.replace('XZ', 'X Z')
data = data.split()
print(len(max(data, key=len)))
