from re import finditer


# почти правильно
def evl(f):
    nums = list(map(int, f.split('-')))
    a = nums[0]
    for n in nums[1:]:
        a -= n
    return a


with open(r'.\files\24_18239.txt') as file:
    data = file.readline()

num = r'[1-9]+'
pattern = fr'-?({num}-)+{num}'
matches = [match.group() for match in finditer(pattern, data)]

ans = 0
for match in matches:
    match = match.split('-')[1:]
    nums = list(map(lambda x: - int(x), match))
    l = sm = len_nums = 0
    for r in range(len(nums)):
        sm += nums[r]
        len_nums += len(str(nums[r]))
        while sm - 2 * nums[l] <= -20_000:
            sm -= nums[l]
            len_nums -= len(str(nums[l]))
            l += 1
        ans = max(ans, len_nums)
print(ans)


# ans = 0
# for match in matches:
#     len_match = len(match)
#     if len_match > ans:
#         if evl(match) > -20_000:
#             ans = max(ans, len_match)
#         else:
#             match = match.split('-')
#             len_match = len(match)
#             for l in range(1, len_match - 1):
#                 for r in range(len_match - 1, l, -1):
#                     new_match = '-'.join(match[l:r + 1])
#                     if evl(new_match) > -20_000:
#                         ans = max(ans, len(new_match))
#                         break
#
# print(ans)
