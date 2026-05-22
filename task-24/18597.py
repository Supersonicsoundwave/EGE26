from re import finditer


with open(r'.\files\24_18597.txt') as file:
    data = file.readline()

pattern = r'[1-9][0-9]{3}\.[0-9]+&[1-9][0-9]{3}\.[0-9]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

#######################################################################

data = data.split('&')
ans = 0
for num1, num2 in zip(data, data[1:]):
    if '.'  not in num1 or '.' not in num2:
        continue
    dot1 = num1.rfind('.')
    if dot1 < 4 or dot1 == len(num1) - 1 or '.' in num1[dot1 - 4:dot1]:
        continue
    num1 = num1[dot1 - 4:]

    dot2 = num2.find('.')
    if dot2 != 4 or dot2 == len(num2) - 1 or num2[dot2 + 1] == '.':
        continue
    dot22 = num2.find('.', dot2 + 1)
    num2 = num2[:dot22]

    ans = max(ans, len(num1 + '&' + num2))

print(ans)
