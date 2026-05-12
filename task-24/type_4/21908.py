from re import finditer
from string import printable


with open(r'.\files\24_21908.txt') as file:
    data = file.readline()

# регулярки
pattern = r'[1-9A-D][0-9A-D]*[02468AC]'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=lambda x: (len(x), x))))

# замена
for i in printable[14:36].upper():
    data = data.replace(i, ' ')
data = data.split()
ans = 0
for num in data:
    num = num.lstrip('0').rstrip('13579BD')
    ans = max(ans, len(num))
print(ans)
