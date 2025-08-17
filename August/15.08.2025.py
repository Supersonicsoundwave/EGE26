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


def split_in_half(line):
    half1 = []
    half2 = []
    length = 0
    modules = line.split('+')
    mid = len(''.join(modules)) // 2
    for i in range(len(modules)):
        if abs(length - mid) < abs(length + len(modules[i]) - mid):
            half2 += modules[i:]
            break
        half1.append(modules[i])
        length += len(modules[i])
    return half1, half2


with open(r'files\2415.txt') as file:
    data = file.readline()

number = r'([1-9][0-9]*|0)'
pattern = fr'({number}[\*+])+{number}'
matches = re.finditer(pattern, data)
res = [match.group() for match in matches]
res.sort(key=len, reverse=True)
match_exp = []
final_res = []
for exp in res:
    match_exp.append(exp)
    if eval(exp) == 0:
        break
# самая длинная строчка 189 самая короткая 130 всего строчек 51
for exp in match_exp:
    s1half, s2half = split_in_half(exp)

    conclusion1 = None
    for i in range(len(s1half) - 1, -1, -1):  # прогоняем первую половину с конца, так мы быстро найдем ближаюшую
        # к центру руину
        if eval(s1half[i]) != 0:  # находим руину
            if s1half[i][-1] == '0':
                conclusion1 = (i, True)  # True т.е. 0 есть
            else:
                conclusion1 = (i, False)
            break
    if conclusion1 is not None:
        if conclusion1[1]:
            s1half = s1half[conclusion1[0]:]  # оставляем все от руины вкл до середины всего выражения
            s1half[0] = '0'  # заменяем руину на 0, т.к. на ее конце он был
        else:
            s1half = s1half[conclusion1[0] + 1:]  # удаляем все до руины включительно

    conclusion2 = None
    for i in range(len(s2half)):
        if eval(s2half[i]) != 0:
            conclusion2 = i
            break
    if conclusion2 is not None:
        s2half = s2half[:conclusion2]
    all_again = '+'.join(s1half + s2half)
    final_res.append(all_again)
print(len(max(final_res, key=len)))
