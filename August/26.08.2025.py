import re


# with open('files\\24-337.txt') as file:
#     data = file.readline()
#
# pattern = r'[1-9ABCD][0-9ABCD]*[02468AC]'
# matches = re.finditer(pattern, data)
# numbers = [match.group() for match in matches]
# correct_numbers = []
# for number in numbers:
#     if int(number, 14) % 98 == 0:
#         correct_numbers.append(number)
#     else:
#         for left in range(len(number)):
#             if number[left:][0] == '0':
#                 continue
#             for right in range(len(number), left, -1):
#                 cur_numb = number[left:right]
#                 if int(cur_numb, 14) % 98 == 0:
#                     correct_numbers.append(cur_numb)
#                     break
# print(len(max(correct_numbers, key=len)))


with open('files\\24-314.txt') as file:
    data = file.readline()

pattern = r'(?<=F)(([1-7][0-7]*|0)[+*])+([1-7][0-7]*|0)'
matches = re.finditer(pattern, data)
res = [match.group() for match in matches]
mx_len = len(max(res, key=len))
res = list(filter(lambda x: len(x) == mx_len, res))
dec_res = []
for exp in res:
    new_exp = ''
    for part in exp.split('+'):
        for numb in part.split('*'):
            new_exp += str(int(numb, 8))
            new_exp += '*'
        new_exp = new_exp[:-1] + '+'
    new_exp = new_exp[:-1]
    dec_res.append(new_exp)
print(eval(max(dec_res, key=lambda x: eval(x))))


