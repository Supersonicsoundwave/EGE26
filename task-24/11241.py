from re import finditer


with open(r'.\files\24_11241.txt') as file:
    data = file.readline()

pattern = r'[^ABCD]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))


ans = 0
cnt = 0
for i in range(len(data)):
    if data[i] not in 'ABCD':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)


for i in 'ABCD':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))
