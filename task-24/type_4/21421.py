from re import finditer
from string import printable


with open(r'.\files\24_21421.txt') as file:
    data = file.readline()

# регулярка
pattern = r'[1-9AB][0-9AB]*[02468A]'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# замена
for i in printable[12:36].upper():
    data = data.replace(i, ' ')

data = data.split()
ans = 0
for num in data:
    num = num.lstrip('0').rstrip('13579B')
    ans = max(ans, len(num))
print(ans)
