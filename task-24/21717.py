with open(r'.\files\24_21717.txt') as file:
    data = file.readline()

data = data.split('RSQ')
ans = 10**20
for i in range(1, len(data) - 128):
    line = 'RSQ' + 'RSQ'.join(data[i:i + 130]) + 'RSQ'
    dop = 'RSQ'.join(data[i + 130:])
    for j in 'RSFGW':
        dop = dop.replace(j, '*')
    line += dop[:dop.find('*')]
    ans = min(ans, len(line))
print(ans)
