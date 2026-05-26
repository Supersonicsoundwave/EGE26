with open(r'.\files\24_14510.txt') as file:
    data = file.readline()

for i in set(data):
    if i in 'AEIOUY':
        data = data.replace(i, 'A')
    else:
        data = data.replace(i, 'B')

data = data.replace('BBA', 'Bba bbA')
data = data.split()
ans = 10**10
for i in range(len(data) - 498):
    line = ''.join(data[i:i + 499]).replace('babb', 'B')
    ans = min(ans, len(line))
print(ans)
