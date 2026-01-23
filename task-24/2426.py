from re import finditer


with open(r'.\files\24_2426.txt') as file:
    data = file.readline()

# перебор
cnt = 0
ans = 0
for i in range(len(data)):
    if data[i].isdigit():
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)

# регулярки
pattern = r'[123]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# замена
for i in 'ABC':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))