from fnmatch import fnmatch


for n in range(37, 10**8 + 1, 37):
    if fnmatch(str(n), '2*1234?6'):
        print(n, n // 37)
