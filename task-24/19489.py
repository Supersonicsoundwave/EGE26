with open(r'.\files\24_19489.txt') as file:
    data = file.readline()

data = data.split('WWF')
ans = 0
for i in range(len(data) - 120):
    line = 'WWF'.join(data[i:i + 121])
    if 'WSFWW' in line:
        line = line.replace('WSFWW', 'WSFW SFWW')
        line = line.split()
        line = max(line, key=len)
    ans = max(ans, len(line))
print(ans)
