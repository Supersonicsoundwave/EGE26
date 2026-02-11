from string import ascii_uppercase, digits
from re import finditer

with open(r'.\files\24_21908.txt') as file:
    data = file.readline()

alph = digits + ascii_uppercase
pattern = r'[1-9ABCD][0-9A-D]*[02468AC]'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

ans = 0
for i in range(len(data)):
    if data[i] in alph[1:14]:
        cnt = 1
        for j in range(i + 1, len(data)):
            if data[j] in alph[:14]:
                cnt += 1
                if data[j] in alph[:14:2]:
                    ans = max(ans, cnt)
            else:
                break
print(ans)

for i in alph[14:]:
    data = data.replace(i, ' ')

data = [s.lstrip('0').rstrip('13579BD') for s in data.split()]
print(len(max(data, key=len)))
