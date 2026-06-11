with open(r'.\files\26_15341.txt') as file:
    N = int(file.readline())
    layers = [int(i) for i in file]

layers.sort(reverse=True)
order = [layers[0]]
for layer in layers[1:]:
    if order[-1] - layer >= 8:
        order += [layer]
print(len(order), min(order))
