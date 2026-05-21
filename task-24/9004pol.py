with open(r'.\files\24-384.txt') as file:
    data = file.readline()

data = data.split('Z')
ans = 10**20
for i in range(1, len(data) - 267): # 268
    line = 'Z' + 'Z'.join(data[i:i + 269]) + 'Z' # 269
    ans = min(ans, len(line))
print(ans)
