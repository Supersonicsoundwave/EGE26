with open(r'.\files\24_8510.txt') as file:
    data = file.readline()

for i in 'NOP':
    data = data.replace(i, '&')

while '&&' in data:
    data = data.replace('&&', '& &')
    
data = data.split()
print(len(max(data, key=len)))
