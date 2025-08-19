import re


with open('Regexp contest\\regexp-practice-1.txt') as file:
    data1 = file.read()

pattern1 = r'\b[cC][aA][tT]\b'
matches1 = re.finditer(pattern1, data1)
res1 = [match.group() for match in matches1]
# print(*res1)


with open('Regexp contest\\regexp-practice-2.txt') as file:
    data2 = file.readlines()

pattern2 = r'[Aa]'
res2 = []
for line in data2:
    if re.match(pattern2, line):
        res2.append(line)
# print(*res2)


with open('Regexp contest\\regexp-practice-3.txt') as file:
    data3 = file.read()

pattern3 = r'-?\d+(\.\d+|d*)'
matches3 = re.finditer(pattern3, data3)
res3 = [match.group() for match in matches3]
# print(*res3, sep='\n')


with open('Regexp contest\\regexp-practice-4.txt') as file:
    data4 = file.read()

pattern4 = r'\d{1,2}-\d{1,2}-\d{4,4}'
matches4 = re.finditer(pattern4, data4)
res4 = [match.group() for match in matches4]
# print(*res4, sep='\n')


with open('Regexp contest\\regexp-practice-5.txt', encoding='utf-8') as file:
    data5 = file.read()

pattern5 = r'[A-ZА-ЯЁ][a-zа-яё]*?\b'
matches5 = re.finditer(pattern5, data5)
res5 = [match.group() for match in matches5]
# print(*res5, sep='\n')


with open('Regexp contest\\regexp-practice-6.txt', encoding='utf-8') as file:
    data6 = file.read()

pattern6 = r'[a-zA-Zа-яёА-ЯЁ]{2,2}-\d{4,4}'
matches6 = re.finditer(pattern6, data6)
res6 = [match.group() for match in matches6]
# print(*res6, sep='\n')


with open('Regexp contest\\regexp-practice-7.txt', encoding='utf-8') as file:
    data7 = file.read()

pattern7 = r'[\w\-]+@[a-z\d_]{2,}\.[a-z]{2,}'
matches7 = re.finditer(pattern7, data7)
res7 = [match.group() for match in matches7]
print(res7)
