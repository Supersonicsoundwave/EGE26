print('w x y z')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = (x <= y) and z and not w
                if f:
                    print(w, x, y, z)