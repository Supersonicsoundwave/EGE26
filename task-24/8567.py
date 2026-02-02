from itertools import product


with open(r'.\files\24_8567.txt') as file:
    data = file.readline()

for val in product('ABCD', repeat=3):
    val = ''.join(val)
    data = data.replace(val, f'{val[:-1]} {val[1:]}')
data = data.split()
print(len(max(data, key=len)))

