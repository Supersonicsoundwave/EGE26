from re import finditer


with open(r'.\files\24_3792.txt') as file:
    data = file.readline()

pattern = r'[ABC]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

ans = 0
cnt = 0
for i in data:
    if i in 'ABC':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)

data = data.replace('D', ' ')
data = data.replace('E', ' ')
data = data.split()
print(len(max(data, key=len)))
