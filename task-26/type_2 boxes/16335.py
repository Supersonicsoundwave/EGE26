with open(r'.\files\26_16335.txt') as file:
    N = int(file.readline())
    shapes = [int(i) for i in file]

shapes.sort(reverse=True)
order = [shapes[0]]
for shape in shapes[1:]:
    if order[-1] - shape >= 4:
        order += [shape]
print(len(order), min(order))
