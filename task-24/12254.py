from re import finditer


with open(r'.\files\24_12254.txt') as file:
    data = file.readline()

pattern = r'(SQ|Q)?(RSQ)+(RS|R)?'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

data = data.replace('RSQ', '***')

data = data.replace('SQ*', ' !!*')
data = data.replace('Q*', ' !*')
data = data.replace('*RS', '*!! ')
data = data.replace('*R', '*! ')

for i in 'RSQ':
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))
