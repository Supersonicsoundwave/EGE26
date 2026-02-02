from re import finditer
from string import ascii_uppercase


with open(r'.\files\24_11813.txt') as file:
    data = file.readline()

pattern = r'[^EYUIOA]?([EYUIOA][^EYUIOA])+[EYUIOA]?'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

for i in ascii_uppercase:
    if i in 'EYUIOA':
        data = data.replace(i, '*')
    else:
        data = data.replace(i, '!')
data = data.replace('**', '* *')
data = data.replace('!!', '! !')
data = data.split()
print(len(max(data, key=len)))

