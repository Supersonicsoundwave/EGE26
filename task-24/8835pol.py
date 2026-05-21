from re import finditer


with open(r'.\files\24-371.txt') as file:
    data = file.readline()

# регулярка
pattern = r'([^M\.]*M){112}[^M\.]*\.'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# замена
data = data.replace('.', '.*')
data = data.split('*')[:-1]

ans = 0
for line in data:
    cnt_M = line.count('M')
    if cnt_M == 112:
        ans = max(ans, len(line))
    elif cnt_M > 112:
        while cnt_M > 112:
            if line[0] == 'M':
                cnt_M -= 1
            line = line[1:]
        ans = max(ans, len(line))
    # elif cnt_M > 112:
    #     pos_M = [i for i in range(len(line)) if line[i] == 'M']
    #     line = line[pos_M[cnt_M - 112 - 1] + 1:]
    #     ans = max(ans, len(line))
print(ans)
