with open(r'.\files\26_20815.txt') as file:
    N, K = map(int, file.readline().split())
    students = []
    for line in file:
        ID, ex1, ex2, ex3, inter = map(int, line.split())
        students += [(ex1 + ex2 + ex3 + inter, inter, ID)]
students.sort(key=lambda x: (-x[0], -x[1], x[2]))
passed = students[:K]
points = sorted(set(s[0] for s in passed), reverse=True)
passing_score = points[-2]
half_passing_score = points[-1]
print([s[-1] for s in passed if s[0] == passing_score][-1], sum(1 for s in students if s[0] == half_passing_score))
