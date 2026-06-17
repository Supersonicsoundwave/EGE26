from re import finditer


with open(r'.\files\24_17685.txt') as file:
    data = file.readline()

num = r'(0|[1-9][0-9]*)'
pattern = fr'({num}[+*])+{num}'
matches = [match.group() for match in finditer(pattern, data)]
ans = 0
for match in matches:
    if eval(match) == 0:
        ans = max(ans, len(match))
    else:
        for l in range(len(match)):
            for r in range(len(match) - 1, l, -1):
                new_match = match[l:r + 1]
                if len(new_match) < ans:
                    break
                if new_match[0] in '+*' or new_match[-1] in '+*' or (new_match[0] == '0' and new_match[1] not in '+*'):
                    continue
                if eval(new_match) == 0:
                    ans = max(ans, len(new_match))
print(ans)

