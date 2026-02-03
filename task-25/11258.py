from fnmatch import fnmatch


for num in range(750122 - 750122 % 8387, 10**9, 8387):
    if fnmatch(str(num), '*75?122*'):
        print(num, num // 8387)
