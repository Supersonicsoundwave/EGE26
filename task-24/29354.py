with open(r'.\files\24_29354.txt') as file:
    data = file.readline()

data = data.replace('BC', 'B C')
data = data.split()
ans = 0
for i in range(len(data) - 190):
    line = ''.join(data[i:i + 191])
    ans = max(ans, len(line))
print(ans)
