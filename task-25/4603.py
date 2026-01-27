from fnmatch import fnmatch

for n in range(12347 - 12347 % 141, 10 ** 8 + 1, 141):
    if fnmatch(str(n), '1234*7'):
        print(n, n // 141)
