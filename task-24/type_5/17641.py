from re import finditer


with open(r'.\files\24_17641.txt') as file:
    data = file.readline()

# регулярка + перебор
num = r'([1-9][0-9]*|0)'
pattern = fr'({num}[+*])+{num}'
matches = [match.group() for match in finditer(pattern, data)]
ans = 0
for match in matches:
    len_match = len(match)
    if eval(match) == 0:
        ans = max(ans, len_match)
    elif len_match > ans:
        for l in range(len_match - 1):
            if match[l] in '+*':
                continue
            if match[l] == '0' and match[l + 1] in '0123456789':
                continue
            for r in range(len_match - 1, l, -1):
                if match[r] in '*+':
                    continue
                new_match = match[l:r + 1]
                if eval(new_match) == 0:
                    ans = max(ans, len(new_match))
                    break

# регулярка
num = r'([1-9][0-9]*|0)'
prod = fr'({num}\*)*0(\*{num})*'
pattern = fr'({prod}\+)*{prod}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# регулярка + замена
num = r'([1-9][0-9]*|0)'
pattern = fr'({num}[+*])+{num}'
matches = [match.group() for match in finditer(pattern, data)]

ans = 0
for match in matches:
    if eval(match) == 0:
        ans = max(ans, len(match))
    else:
        match = match.split('+')
        new_match = ''
        for m in match:
            if eval(m) == 0:
                new_match += m + '+'
            else:
                new_match = ''
            ans = max(ans, len(new_match) - 1)
print(ans)
