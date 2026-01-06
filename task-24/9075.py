from string import printable


with open(r'.\files\24_9075.txt') as file:
    data = file.readline()

for i in range(len(printable[:36])):
    if i % 2 == 0:
        data = data.replace(printable[i], '*')
    else:
        data = data.replace(printable[i], '!')

data = data.replace('*!', "* !")
data = data.replace('!*', "! *")
data = data.split()
print(len(max(data, key=len)))
