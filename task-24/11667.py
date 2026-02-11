with open(r'.\files\24_11667.txt') as file:
    data = file.readline()

data = data.replace('INFINITY', ' ')
data = data.split(' ')
ans = 0
for i in range(len(data) - 1000):
    if i in [0, len(data) - 1001]:
        ans = max(ans, len('INFINITY'.join(data[i:i + 1001])) + 7)
    else:
        ans = max(ans, len('INFINITY'.join(data[i:i + 1001])) + 14)
print(ans)
