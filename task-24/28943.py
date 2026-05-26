from re import finditer


with open(r'.\files\24_28943.txt') as file:
    data = file.readline()

data = data.replace('20', '&')
pattern = r'(&[^AEIOUY&]*){26}[AEIOUY]'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key=len)) + 26)
