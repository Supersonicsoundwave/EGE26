with open(r'.\files\26_23570.txt') as file:
    N, K = map(int, file.readline().split())
    plots = []
    machines = dict()
    for i in range(N):
        plots += [int(file.readline())]
    for i in range(K):
        power, price = list(map(int, file.readline().split()))
        if price not in machines:
            machines[price] = [power]
        else:
            machines[price] += [power]
            machines[price].sort(reverse=True)

plots.sort()

good_machines = []
for key, value in machines.items():
    good_machines += [(value[0], key)]

good_machines.sort(key=lambda x: (x[1], -x[0]))

sum_cost = 0
max_power = 0
for plot in plots:
    for machine in good_machines:
        if plot <= machine[0]:
            sum_cost += machine[1]
            max_power = max(max_power, machine[0])
            break
print(sum_cost, max_power)
