from re import *


with open(r'.\files\24_1146.txt') as file:
    data = file.readline()

cnt = 0
lens = []
for i in data:
    if i != 'D':
        lens += [cnt]
        cnt = 0
    else:
        cnt += 1
lens += [cnt]
print(min(filter(lambda x: x > 0, lens)))

pattern = r'D+'
res = [match.group() for match in finditer(pattern, data)]
print(len(min(res, key=len)))

for i in 'ABCEF':
    data = data.replace(i, ' ')
data = data.split()
print(len(min(data, key=len)))
