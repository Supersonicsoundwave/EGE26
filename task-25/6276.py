from fnmatch import fnmatch


for num in range(10101011 - 10101011 % 2023, 10**10 + 1, 2023):
    if fnmatch(str(num), '1?1?1?1*1') and sum(int(x) for x in str(num)) == 22:
        print(num)

