from fnmatch import fnmatch


for num in range(1021394 - 1021394 % 3052, 10**10, 3052):
    if fnmatch(str(num), '1?2139*4'):
        print(num, num // 3052)
