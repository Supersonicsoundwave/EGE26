from re import finditer


with open(r'.\files\24_4627.txt') as file:
    data = file.readline()

# перебор
ans = 0
for i in range(len(data) - 2):
    if data[i:i + 3] in 'NPO PNO':
        cnt = 1
        for j in range(i + 3, len(data) - 2, 3):
            if data[j:j + 3] in 'NPO PNO':
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)


# регулярка
pattern = r'(PNO|NPO)+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 3)


# один цикл
i = 0
cnt = 0
ans = 0
while i < len(data):
    if data[i:i + 3] in 'NPO PNO':
        i += 3
        cnt += 1
    else:
        i += 1
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)


# замена
data = data.replace('PNO', '*')
data = data.replace('NPO', '*')
for i in set(data):
    if i != '*':
        data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))


