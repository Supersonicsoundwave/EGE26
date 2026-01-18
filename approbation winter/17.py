with open('17 (2).txt') as file:
    data = list(map(lambda x: int(x.rstrip()), file.readlines()))

dls = []
for num in data:
    if num > 0 and num % 41 == 0:
        dls += [num]
dl = min(dls)

sm = []
for i in range(len(data) - 1):
    a, b = data[i], data[i + 1]
    if a != b and abs(a - b) % dl == 0:
        sm += [a + b]
print(len(sm))
print(max(sm))
