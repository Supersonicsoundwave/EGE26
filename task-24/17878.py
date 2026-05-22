from re import finditer


with open(r'.\files\24_17878.txt') as file:
    data = file.readline()

num = r'([6-9][0-9]*|0)'
pattern = fr'({num}[-*])+{num}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
