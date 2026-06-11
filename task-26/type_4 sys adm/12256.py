with open(r'.\files\26_12256.txt') as file:
    S, N = map(int, file.readline().split())
    parcels = [int(i) for i in file]

parcels.sort()
order = [parcels[0]]
for parcel in parcels[1:]:
    if sum(order) + parcel <= S:
        order += [parcel]

order = order[:-1]
for parcel in parcels[::-1]:
    if sum(order) + parcel <= S:
        order += [parcel]
        break

print(len(order), max(order))
