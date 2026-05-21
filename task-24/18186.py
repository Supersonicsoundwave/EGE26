with open(r'.\files\24_18186.txt') as file:
    data = file.readline()

for i in 'AE':
    data = data.replace(i, '*')
for i in 'BCDFGH':
    data = data.replace(i, '!')
data = data.replace('!!*', '!!* !!*')
data = data.split()
print(len(max(data, key=len)))
