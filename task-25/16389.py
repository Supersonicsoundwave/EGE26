from fnmatch import fnmatch


for num in range(5023030 - 5023030 % 98591, 10**10, 98591):
    if fnmatch(str(num), '5?2*3?3?'):
        print(num, num // 98591)
