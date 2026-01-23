from re import finditer


with open(r'.\files\24_1273.txt') as file:
    data = file.readline()

# перебор
cnt = 2
ans = 0
for i in range(len(data) - 2):
    if data[i:i + 3] != 'XYZ':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 2
ans = max(ans, cnt)
print(ans)

# регулярки
pattern = r'(^|(?<=(XYZ))).+?($|(?=(XYZ)))'
ans = 0
for match in finditer(pattern, data):
    res = match.group()
    if match.groups().count('XYZ') == 2:
        ans = max(ans, len(res) + 4)
    elif match.groups().count('XYZ') == 1:
        ans = max(ans, len(res) + 2)
print(ans)

# замена
data = data.replace('XYZ', 'XY YZ')
data = data.split()
print(len(max(data, key=len)))

