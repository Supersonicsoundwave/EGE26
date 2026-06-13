with open(r'.\files\26_17881.txt') as file:
    N = int(file.readline())
    no_2 = []
    more_two_2 = []
    for line in file:
        ID, *exs = list(map(int, line.split()))
        if exs.count(2) == 0:
            no_2 += [(sum(exs) / 4, ID)]
        if exs.count(2) > 2:
            more_two_2 += [(exs.count(2), ID)]


no_2.sort(key=lambda x: (-x[0], x[1]))
more_two_2.sort()
print(no_2[N // 4 - 1][1], more_two_2[0][1])

