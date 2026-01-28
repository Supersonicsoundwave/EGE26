from fnmatch import fnmatch


for x in range(5401037 - 5401037 % 18579, 10**10 + 1, 18579):
    if fnmatch(str(x), '54?1?3*7'):
        print(x, x // 18579)
