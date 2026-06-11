with open(r'.\files\26_4712.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes.sort(reverse=True)
order = [boxes[0]]
for box in boxes[1:]:
    if order[-1] - box >= 3:
        order += [box]
print(len(order), min(order))
