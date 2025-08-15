import re


# with open(r'files\2405.txt') as file:
#     data = file.readline()
#
# pattern = r'(LMN|MN|N)?(KLMN)+(KLM|KL|K)?'
# matches = re.finditer(pattern, data)
# res = [match.group() for match in matches]
# print(len(max(res, key=len)))  # 182


# with open(r'files\2416.txt') as file:
#     data = file.readline()
#
# pattern = r'([AE][BCD])+'
# matches = re.finditer(pattern, data)
# res = [match.group() for match in matches]
# print(len(max(res, key=len)) // 2)  # 202


# with open(r'files\2402.txt') as file:
#     data = file.readline()
#
# number = r'(([789][0789]*)|0)'
# pattern = fr'({number}[\*-])+{number}'
# matches = re.finditer(pattern, data)
# res = [match.group() for match in matches]
# print(len(max(res, key=len)))  # 111


# with open(r'files\2418.txt') as file:
#     data = file.readline()
#
# number = r'([1-9][0-9]*[02468]|[02468])'
# pattern = fr'({number}[\*+])+{number}'
# matches = re.finditer(pattern, data)
# res = [match.group() for match in matches]
# print(len(max(res, key=len)))  # 127


with open(r'files\2415.txt') as file:
    data = file.readline()

number = r'([1-9][0-9]*|0)'
pattern = fr'({number}[\*+])+{number}'
matches = re.finditer(pattern, data)
res =  [match.group() for match in matches]
res.sort(key=len, reverse=True)
for exp in res:
    if eval(exp) == 0:
        cnt = len(exp)
        break
    else:
        ...
print(cnt)

