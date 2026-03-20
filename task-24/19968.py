from string import printable
from re import finditer


with open(r'.\files\24_19968.txt') as file:
    data = file.readline()

num = fr'(0|[{printable[1:6]}][{printable[:6]}]*)'
pattern = fr'({num}[\+\*])+{num}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
