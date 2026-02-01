from fnmatch import fnmatch


for num in range(1920368 - 1920368 % 154682, 10**11, 154682):
    if fnmatch(str(num), '*192?3*68'):
        print(num, num // 154682)
