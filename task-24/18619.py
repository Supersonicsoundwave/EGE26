from re import finditer


with open(r'.\files\24_18619.txt') as file:
    data = file.readline()

num = r'[123456][0123456]*'
pattern = fr'B+{num}([-*]{num})+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
