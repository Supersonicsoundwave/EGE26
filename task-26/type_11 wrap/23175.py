with open(r'files/26_2_23175.txt') as file:
    N, M = map(int, file.readline().split())
    loads = [int(file.readline()) for i in range(N)]
    containers = [int(file.readline()) for j in range(M)]

loads.sort()
containers.sort()
loaded = []
last_container = 0
for load in loads:
    for container in containers:
        if load <= container:
            loaded += [load]
            containers.remove(container)
            last_container = container
            break

loaded = loaded[:-1]
for load in loads[::-1]:
    if load <= last_container:
        loaded += [load]
        break

loaded.sort()

print(len(loaded), loaded[-1] - loaded[-2])

