with open(r'.\files\24_9753.txt') as file:
    data = file.readline()

# метод двух указателей
ans = cnt = r = l = 0
while r < len(data):
    if cnt <= 150:
        if data[r] == 'Y':
            cnt += 1
        r += 1
    else:
        if data[l] == 'Y':
            cnt -= 1
        l += 1
    ans = max(ans, r - l - 1)
print(ans)


# замена
data = data.split('Y')
ans = 0
for i in range(len(data) - 150):
    line = 'Y'.join(data[i:i + 151])
    ans = max(ans, len(line))
print(ans)
