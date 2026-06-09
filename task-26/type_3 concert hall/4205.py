with open(r'.\files\26_4205.txt') as file:
    N = int(file.readline())
    seedlings = [list(map(int, line.split())) for line in file]

seedlings.sort(key=lambda x: (-x[0], x[1]))
for seedling1, seedling2 in zip(seedlings, seedlings[1:]):
    if seedling1[0] == seedling2[0]:
        if seedling2[1] - seedling1[1] == 14:
            print(seedling1[0], seedling1[1] + 1)
            break

