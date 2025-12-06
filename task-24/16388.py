from re import *


with open(r'.\files\24_16388.txt') as file:
    data = file.readline()

pattern = r'[LMN|MN|N](KLMN)+[KLM|KL|K]'
res = [match.group() for match in finditer(pattern, data)]
print(len(max(res, key=len)))

# ans = 0
# for i in range(len(data) - 3):
#     four_letters = data[i:i + 4]
#     if four_letters == 'KLMN':
#         cnt = 1
#         for j in range(i + 4, len(data), 4):
#             if data[j:j + 4] == 'KLMN':
#                 cnt += 1
#             else:
#                 break
#         cnt *= 4
#         cnt += data[i - 1] == 'N' + data[i - 2] == 'M' + data[i - 3] == 'L'
#         ans = max(ans, cnt)
# фигня решение


data = data.replace('KLMN', '****')
data = data.replace('LMN*', ' !!!*')
data = data.replace('MN*', ' !!*')
data = data.replace('N*', ' !*')
data = data.replace('*KLM', '*!!! ')
data = data.replace('*KL', '*!! ')
data = data.replace('*K', '*! ')
for i in 'KLMN':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))

