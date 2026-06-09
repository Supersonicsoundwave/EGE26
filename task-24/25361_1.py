from re import finditer


with open(r'.\files\24_25361.txt') as file:
    data = file.readline()

pattern = r'[02468]([^02468F]*F){76}[^02468F]*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))


for i in '02468':
    data = data.replace(i, ' *')
data = data.split()

ans= 0
for line in data[1:]:
    cnt_F = line.count('F')
    if cnt_F == 76:
        ans = max(ans, len(line))
    elif cnt_F > 76:
        while cnt_F > 76:
            if line[-1] == 'F':
                cnt_F -= 1
            line = line[:-1]
        ans = max(ans, len(line))
print(ans)
