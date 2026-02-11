with open(r'.\files\24_19254.txt') as file:
    data = file.readline()

data = data.split('FSRQ')
ans = 0
for i in range(len(data) - 80):
    if i in [0, len(data) - 81]:
        ans = max(ans, len('FSRQ'.join(data[i:i + 81])) + 3)
    else:
        ans = max(ans, len('FSRQ'.join(data[i:i + 81])) + 6)
print(ans)

