# import re
#
#
# with open('reg_exp_task_1.txt') as file:
#     text = file.readline()
#
#
# pattern = r'\d+'
# res = re.findall(pattern, text)
# print(res)


# import re
#
#
# with open('reg_exp_task_2.txt') as file:
#     text = file.readline()
#
# pattern = r'-?\d+\.?\d*'
# res = re.findall(pattern, text)
# print(res)


# import re
#
#
# text = input()
# pattern = r'a+b{2,}c+'
# res = re.sub(pattern, 'HELLO', text)
# print(res)


# import re
#
#
# with open('reg_exp_task_4.txt') as file:
#     text = file.readline()
#
# pattern = r'\w+@\w+\.[a-z]{2,}'
# res = re.findall(pattern, text)
# print(res)


import re
from timeit import timeit


def regexp(data):
    pattern = r'(NPO|PNO)+'
    res = [match.group() for match in re.finditer(pattern, data)]
    res = max(res, key=len)
    # print(len(res) // 3)


def iterate(data):
    counts = []
    cnt = 0
    triple_wf = 3
    for i in range(len(data) - 2):
        if triple_wf in [1, 2]:
            triple_wf += 1
            continue
        if triple_wf == 3:
            if data[i:i+3] in ['NPO', 'PNO']:
                cnt += 1
                triple_wf = 1
            else:
                counts.append(cnt)
                cnt = 0
    # print(max(counts))


def standart(data):
    line = data.replace('NPO', '1').replace('PNO', '1')
    pattern = r'[NPO]'
    res = re.sub(pattern, ' ', line)
    res = res.split()
    # print(len(max(res, key=len)))


def standart2(data):
    line = data.replace('NPO', '1').replace('PNO', '1')
    for i in 'NPO':
        line = line.replace(i, ' ')
    res = line.split()
    # print(len(max(res, key=len)))


with open('files\\2400.txt') as file:
    text = file.readline()

time1 = timeit('regexp(text)', globals=globals(), number=10)
time2 = timeit('iterate(text)', globals=globals(), number=10)
time3 = timeit('standart(text)', globals=globals(), number=10)
time4 = timeit('standart2(text)', globals=globals(), number=10)
print(time1)
print(time2)
print(time3)
print(time4)