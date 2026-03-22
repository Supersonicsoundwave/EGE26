from re import finditer


with open(r'.\files\24_18937.txt') as file:
    data = file.readline()

number = r'(0|[2-5][0-5]*)'
pattern = fr'{number}([\+\*]{number})+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
