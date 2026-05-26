from re import finditer


with open(r'.\files\24_19751.txt') as file:
    data = file.readline()

num = r'([1-9][0-9]*|0)'
pattern = fr'(?<=A)({num}\+)*{num}'
matches = [match.group() for match in finditer(pattern, data)]
print(eval(max(matches, key=eval)))
