with open(r'.\files\26_21910.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes.sort(reverse=True)
order = [boxes[0]]
for box in boxes[1:]:
    if order[-1] - box >= 9:
        order += [box]
print(len(order), order[-1])
