from fnmatch import fnmatch


for num in range(9874, 10**10, 9874):
    if fnmatch(str(num), '89*6?7?9?'):
        print(num, num // 9874)
