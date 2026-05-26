from re import finditer


with open(r'.\files\24_5171.txt') as file:
    data = file.readline()

pattern = r'(CA)+C?'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
