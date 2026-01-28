from fnmatch import fnmatch


for x in range(1004513 - 1004513 % 451, 10**9 + 1, 451):
    if fnmatch(str(x), '10?451*3'):
        print(x, x // 451)