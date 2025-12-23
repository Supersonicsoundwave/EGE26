print('a b c d')
for a in 0, 1:
    for b in range(2):
        for c in [0, 1]:
            for d in (0, 1):
                f = (not a and not b) or (b == c) or d
                if not f:
                    print(a, b, c, d)
