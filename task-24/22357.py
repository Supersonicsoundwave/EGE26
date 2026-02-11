from re import finditer


with open(r'.\files\24_22357.txt') as file:
    data = file.readline()

pattern = r'[1-9A-D][0-9A-D]*'
matches = [match.group() for match in finditer(pattern, data)]
ans = '0'
for match in matches:
    if match[-1] in '02468AC':
        if int(ans, 14) < int(match, 14):
            ans = match
    else:
        if any(digit in match for digit in '02468AC'):
            while match[-1] not in '02468AC':
                match = match[:-1]
            if int(ans, 14) < int(match, 14):
                ans = match
print(data.find(ans))
