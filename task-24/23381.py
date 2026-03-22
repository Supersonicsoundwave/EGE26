with open(r'.\files\24_23381.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data)):
    if data[i] in '02468':
        for j in range(i + 1, len(data)):
            if data[j] in '13579':
                break
            if data[j] in '02468':
                if all(data[i + 1:j].count(s) > 1 for s in set(data[i + 1:j])):
                    ans = max(ans, len(data[i:j + 1]))
                break
print(ans)

for i in '02468':
    data = data.replace(i, '* *')
data = data.split()
ans = 0
for line in data[1:-1]:
    if all(i not in line for i in '13579') and all(line.count(letter) > 1 for letter in set(line[1:-1])):
      ans = max(ans, len(line))
print(ans)
