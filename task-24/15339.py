from re import finditer


with open(r'.\files\24_15339.txt') as file:
    data = file.readline()

# регулярки
pattern = r'[ABC]?([6789][ABC])*[6789]?'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# перебор
for i in '6789':
    data = data.replace(i, '*')
for i in 'ABC':
    data = data.replace(i, '!')

ans = 0
checkpoint = 0
for i in range(len(data) - 1):
    if i < checkpoint:
        continue
    if data[i:i + 2] not in '** !!':
        cnt = 1
        for j in range(i + 1, len(data) - 1):
            if data[j:j + 2] not in '** !!':
                cnt += 1
            else:
                cnt += 1
                checkpoint = j
                break
        ans = max(ans, cnt)
print(ans)

# замена
while '**' in data:
    data = data.replace('**', '* *')
while '!!' in data:
    data = data.replace('!!', '! !')

data = data.split()
print(len(max(data, key=len)))

