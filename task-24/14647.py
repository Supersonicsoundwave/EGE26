with open(r'.\files\24_14647.txt') as file:
    data = file.readline()

data = data.split('X')
ans = 0
res = []
for i in range(len(data) - 1):
    line = 'X'.join(data[i:i + 2])
    cnt_Y = line.count('Y')
    if cnt_Y == 1:
        ans = max(ans, len(line))
    if cnt_Y > 1:
        left_ind = [ind for ind in range(len(data[i])) if data[i][ind] == 'Y']
        left = data[i][left_ind[-2] + 1:] if data[i].count('Y') > 1 else data[i]

        right_ind = [ind for ind in range(len(data[i + 1])) if data[i + 1][ind] == 'Y']
        right = data[i + 1][:right_ind[1]] if data[i + 1].count('Y') > 1 else data[i + 1]
        line = left + 'X' + right
        if line.count('Y') == 1:
            ans = max(ans, len(line))
        else:
            new_line = max(line[line.find('Y') + 1:], line[:line.rfind('Y')], key=len)
            ans = max(ans, len(new_line))

print(ans)


