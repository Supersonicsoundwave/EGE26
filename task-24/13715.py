with open(r'.\files\24_13715.txt') as file:
    data = file.readline()

# замена
data = data.replace('AB', ' ')
data = data.split(' ')
ans = 0
for i in range(len(data) - 50):
    line = 'AB'.join(data[i:i + 51])
    if i in [0, len(data) - 51]:
        ans = max(ans, len(line) + 1)
    else:
        ans = max(ans, len(line) + 2)
print(ans)
