from re import finditer


with open(r'.\files\24_22356.txt') as file:
    data = file.readline()

pattern = r'[1-9AB][0-9AB]*[13579B]'
matches = [match.group() for match in finditer(pattern, data)]
print(data.find(max(matches, key=lambda x: (len(x), x))))
