with open(r'.\files\24_9753.txt') as file:
    data = file.readline()

# перебор

# ans = 0
# for i in range(len(data)):
#     cnt = 0
#     cntY = 0
#     for j in range(i, len(data)):
#         if data[j] == 'Y':
#             cntY += 1
#         if cntY == 151:
#             break
#         cnt += 1
#     ans = max(ans, cnt)
# print(ans)

# перебор
data = data.split('Y')
ans = 0
for i in range(len(data) - 150):
    ans = max(ans, len('Y'.join(data[i:i + 151])))
print(ans)
