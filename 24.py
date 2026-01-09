from re import *


with open('24 (1).txt') as file:
    data = file.readline()

number = r'[789][0789]*'
pattern = fr'{number}([-*]{number})+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
