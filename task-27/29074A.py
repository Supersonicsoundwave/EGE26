with open(r'.\files\27_A_29074.txt') as file:
    dots = []
    stars = []
    for line in file:
        x, y, data = line.replace(',', '.').split()
        dots += [list(map(float, (x, y)))]
        if data[0] == 'Z':
            stars += [list(map(float, (x, y)))]

cl1 = [star for star in stars if star[1] > 10]

cl2 = [star for star in stars if star[1] < 10]

cls = [cl1, cl2]

A1 = len(min(cls, key=len))
A2 = len(max(cls, key=len))
print(A1, A2)
