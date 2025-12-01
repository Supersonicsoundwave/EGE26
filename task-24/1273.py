from re import *


with open(r'.\files\24_1273.txt') as file:
    data = file.readline()

# перебор
cnt = 2
ans = 0
for i in range(len(data) - 2):
    if data[i:i + 3] != 'XYZ':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 2
ans = max(ans, cnt)
print(ans)

# регулярки
pattern = r'(?<=XYZ).+?(?=XYZ)'
res = [match.group() for match in finditer(pattern, data)]
print(len(max(res, key=len)) + 4)

# замена
data = data.replace('XYZ', 'XY YZ')
data = data.split()
print(len(max(data, key=len)))
