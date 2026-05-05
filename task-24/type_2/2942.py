from re import finditer


with open(r'.\files\24_2942.txt') as file:
    data = file.readline()

# перебор
ans = 0
checkpoint = 0
for i in range(len(data) - 1):
    if checkpoint > i:
        continue
    if data[i:i + 2] in ['AB', 'AC']:
        cnt = 1
        for j in range(i + 2, len(data) - 1, 2):
            if data[j:j + 2] in 'AB AC':
                cnt += 1
            else:
                checkpoint = j
                break
        ans = max(ans, cnt)
print(ans)

# один цикл
ans = 0
cnt = 0
i = 0
while i < len(data):
    if data[i:i + 2] in 'AB AC':
        cnt += 1
        i += 2
    else:
        i += 1
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)

# регулярки
pattern = r'(AB|AC)+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)

# замена
data = data.replace('AB', '#')
data = data.replace('AC', '#')
for i in 'ABC':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))
