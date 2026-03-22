from re import finditer


with open(r'.\files\24_23206.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data)):
    if data[i] in '02468':
        cnt = 0
        cnt_s = 0
        for j in range(i + 1, len(data)):
            if data[j] == 'S':
                cnt_s += 1
            if data[j] in '02468':
                if cnt_s == 35:
                    ans = max(ans, j - i)
                else:
                    break
            if cnt_s == 36:
                ans = max(ans, j - i)
                break
print(ans)

pattern = '[02468]([^S02468]*S){35}[^02468S]*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

for i in '02468':
    data = data.replace(i, ' *')

data = data.split()
ans = 0
for line in data:
    if line.count('S') >= 35:
        line = 'S'.join(line.split('S')[:36])
        ans = max(ans, len(line))
print(ans)
