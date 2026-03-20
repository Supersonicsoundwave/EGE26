from re import finditer


with open(r'.\files\24_19970.txt') as file:
    data = file.readline()

num = r'(0|5|[1-9][0-9]*[05])'
pattern = fr'({num}[\+\*])+{num}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
