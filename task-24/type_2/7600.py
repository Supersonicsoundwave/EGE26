from re import finditer


with open(r'.\files\24_7600.txt') as file:
    data = file.readline()

# перебор
ans = 0
for i in range(len(data) - 1):
    if not (data[i] in 'QRS' and data[i + 1] in 'QRS'):
        cnt = 1
        for j in range(i + 1, len(data) - 1):
            cnt += 1
            if data[j] in 'QRS' and data[j + 1] in 'QRS':
                break
        ans = max(ans, cnt)
print(ans)


# регулярка
pattern = r'(([^RSQ]+[RSQ])+[^RSQ]*|([RSQ][^RSQ]+)+[RSQ]?)'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# замена
for i in 'RSQ':
    data = data.replace(i, '*')

while '**' in data:
    data = data.replace('**', '* *')
data = data.split()
print(len(max(data, key=len)))
