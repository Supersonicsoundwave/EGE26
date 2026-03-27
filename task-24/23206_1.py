with open(r'.\files\24_23206 (1).txt') as file:
    data = file.readline()

for i in '02468':
    data = data.replace(i, '*')

data = data.replace('*', ' *')
data = data.split()
ans = 0
for line in data[1:]:
    if line.count('S') == 35:
        ans = max(ans, len(line))
    if line.count('S') > 35:
        line = line.split('S')
        line = 'S'.join(line[:36])
        ans = max(ans, len(line))
print(ans)
