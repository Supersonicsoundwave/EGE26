with open(r'.\files\17968.txt') as file:
    data = [list(map(int, line.split())) for line in file]

cnt = 0
for line in data:
    line = sorted(line)
    if line[-1] < sum(line[:-1]):
        chet = [num for num in line if num % 2 == 0]
        ne_chet = [num for num in line if num % 2 != 0]
        if sum(chet) == sum(ne_chet):
            cnt +=1
print(cnt)
