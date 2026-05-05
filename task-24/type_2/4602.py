from re import finditer


with open(r'.\files\24_4602.txt') as file:
    data = file.readline()

# перебор
# ans = 0
# for i in range(len(data) - 1):
#     if data[i] in 'BCD' and data[i + 1] in 'AO':
#         cnt = 1
#         for j in range(i + 2, len(data) - 1, 2):
#             if data[j] in 'BCD' and data[j + 1] in 'AO':
#                 cnt += 1
#             else:
#                 break
#         ans = max(ans, cnt)
# print(ans)


# регулярка
pattern = r'([BCD][AO])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)


# один цикл
i = 0
cnt = 0
ans = 0
while i < len(data):
    if data[i] in 'BCD' and data[i + 1] in 'AO':
        i += 2
        cnt += 1
    else:
        i += 1
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)


# замена
for s1 in 'BCD':
    for s2 in 'AO':
        data = data.replace(s1 + s2, '*')

for i in set(data):
    if i != '*':
        data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))
