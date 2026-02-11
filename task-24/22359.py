from re import finditer


with open(r'.\files\24_22359.txt') as file:
    data = file.readline()

pattern = r'[1-9A-E][0-9A-E]+'
matches = [match.group() for match in finditer(pattern, data)]
ans = '0'
for match in matches:
    if match[-1] in '05A':
        if int(match, 15) > int(ans, 15):
            ans = match
    else:
        if '0' in match or '5' in match or 'A' in match:
            while match[-1] not in '05A':
                match = match[:-1]
            if int(match, 15) > int(ans, 15):
                ans = match
print(data.find(ans) + len(ans) - 1)
