with open(r'.\files\24-293.txt') as file:
    data = file.readline()

for i in '0123456789':
    data = data.replace(i, '*')
data = data.replace('DS', 'D*S')
data = data.replace('SD', 'S*D')
data = data.split('*')
ans = 0
for line in data:
    cnt_D = line.count('D')
    if cnt_D == 100:
        ans = max(ans, cnt_D)
    if cnt_D > 100:
        line = line.split('D')
        for j in range(len(line) - 100):
            new_line = 'D'.join(line[j:j + 101])
            ans = max(ans, len(new_line))
print(ans)
