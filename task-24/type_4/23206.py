from re import finditer


with open(r'.\files\24_23206.txt') as file:
    data = file.readline()

# регулярки
pattern = r'[02468]([^02468S]*S){35}[^02468S]*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# замена
for i in '02468':
    data = data.replace(i, ' *')
data = data.split()
ans = 0
for line in data:
    if line.count('S') >= 35:
        while line.count('S') > 35:
            line = line[:line.rfind('S')]
        ans = max(ans, len(line))
print(ans)
