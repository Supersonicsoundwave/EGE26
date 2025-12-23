print('w x y z')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = ((x <= z) <= y) or not w
                if not f:
                    print(w, x, y, z)