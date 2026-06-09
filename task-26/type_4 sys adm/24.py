with open(r'.\files\26_24.txt') as file:
    S, N = list(map(int, file.readline().split()))
    files = [int(i) for i in file]

files.sort()
disk = []
for file in files:
    if sum(disk) + file <= S:
        disk += [file]
disk = disk[:-1]
for file in files[::-1]:
    if sum(disk) + file <= S:
        disk += [file]
        break
print(len(disk), max(disk))
