num = 4*625**9 - 25**15 + 2*5**11 - 7


def convert(x, q):
    ans = ''
    while x:
        ans += str(x % q)
        x //= q
    return ans[::-1]


print(convert(num, 5).count('4'))

######################################

num = 4*625**9 - 25**15 + 2*5**11 - 7
cnt4 = 0
while num:
    if num % 5 == 4:
        cnt4 += 1
    num //= 5
print(cnt4)
