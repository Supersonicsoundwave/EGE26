from re import finditer


with open(r'.\files\24_18597.txt') as file:
    data = file.readline()

pattern = r'[1-9][0-9]{3}\.[0-9]+&[1-9][0-9]{3}\.[0-9]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
