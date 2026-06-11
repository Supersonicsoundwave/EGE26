with open(r'.\files\26_17565.txt') as file:
    N, S = map(int, file.readline().split())
    data = []
    for line in file:
        idd, ex1, ex2, ex3, interview = map(int, line.split())
        data += [(ex1 + ex2 + ex3, interview, idd)]

data.sort(key=lambda x: (-x[0], -x[1], x[2]))

full_score_id = [pers[2] for pers in data if pers[0] > data[S:][0][0]][-1]
cnt_half_score = sum(person[0] == data[S:][0][0] for person in data)
print(full_score_id, cnt_half_score)
