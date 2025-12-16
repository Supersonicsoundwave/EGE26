from re import *


with open(r'.\files\24_25361.txt') as file:
    data = file.readline()


# F_count = 0
# cnt = 0
# max_len = 0
#
# for i in range(len(data)):
#     if data[i] in '02468':
#         cnt += 1
#         for j in range(i + 1, len(data)):
#             if data[j] == 'F' and F_count == 76 or data[j] in '02468':
#                 if F_count == 76:
#                     max_len = max(cnt, max_len)
#                 cnt = 0
#                 F_count = 0
#                 break
#             if data[j] == 'F':
#                 F_count += 1
#             cnt += 1
#
# max_len = max(cnt, max_len)
# print(max_len)

# способ 1
# with open(r'.\files\24_25361.txt') as file:
#     data = file.readline()
#
#
# ans = 0
# for i in range(len(data)):
#     if data[i] in '02468':
#         cnt = 1
#         cnt_F = 0
#         for j in range(i + 1, len(data)):
#             if data[j] == 'F' and cnt_F == 76 or data[j] in '02468':
#                 break
#             if data[j] == 'F':
#                 cnt_F += 1
#             cnt += 1
#
#         if cnt_F == 76:
#             ans = max(cnt, ans)
#
# max_len = max(cnt, ans)
# print(max_len)

# способ 2
# for i in '02468':
#     data = data.replace(i, ' 0')
# data = data.split()
#
# ans = 0
# for i in data:
#     if i[0] == '0' and i.count('F') == 76:  # 1 строка может не начинаться на чет число
#         ans = max(ans, len(i))
#         if i[0] == '0' and i.count('F') > 76:
#             while i.count('F') > 76:
#                 pos_F = i.rfind('F')
#                 i = i[:pos_F]
#             ans = max(ans, len(i))
# print(ans)


# способ 3
pattern = r'[02468]([^02468F]*F){76}[^02468F]*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
