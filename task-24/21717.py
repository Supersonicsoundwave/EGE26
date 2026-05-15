with open(r'.\files\24_21717.txt') as file:
    data = file.readline()

# data = data.split('RSQ')
# ans = 10**20
# for i in range(1, len(data) - 130):
#     line = 'RSQ' + 'RSQ'.join(data[i:i + 129]) + 'RSQ'
#     dop = data[i + 129] + 'RSQ'
#     for j in 'RSFGW':
#         dop = dop.replace(j, '*')
#     line += dop[:dop.find('*') + 1]
#     ans = min(ans, len(line))
# print(ans)


##########################################

with open(r'..\..\files\24_21717.txt') as file:
    data = file.readline()

data = data.replace('RSQ', 'Rsq rsQ')
data = data.split()

ans = 10 ** 10
for i in range(len(data) - 128 - 1):
    line = ''.join(data[i:i + 129]).replace('sqrs', 'S')
    cnt = 0
    for j in data[i + 129][3:]:
        cnt += 1
        if j not in 'Qq':
            break
    ans = min(ans, len(line) + cnt)
print(ans)
