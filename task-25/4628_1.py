from fnmatch import fnmatch


for n in range(161, 10**8 + 1, 161):
    if fnmatch(str(n), '12*4?65'):
        print(n, n // 161)
