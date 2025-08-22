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

pattern7 = r'([A-Za-z]|-|_)+@([A-Za-z]|-|_){2,}\.[a-z]{2,}'
matches7 = re.finditer(pattern7, data7)
res7 = [match.group() for match in matches7]
# print(*res7, sep='\n')


with open('Regexp contest\\regexp-practice-8.txt', encoding='utf-8') as file:
    data8 = file.read()

pattern8 = r'(\+7|8)\s?(\(\d{3,3}\)|\d{3,3})\s?(\d{3,3}\-\d{2,2}\-\d{2,2}|\d{7,7})'
matches8 = re.finditer(pattern8, data8)
res8 = [match.group() for match in matches8]
# print(*res8, sep='\n')


with open('Regexp contest\\regexp-practice-9.txt', encoding='utf-8') as file:
    data9 = file.read()

pattern9 = r'(http:\//|https:\//).+?(?=")'
matches9 = re.finditer(pattern9, data9)
res9 = [match.group() for match in matches9]
# print(*res9, sep='\n')


with open('Regexp contest\\regexp-practice-10.txt', encoding='utf-8') as file:
    data10 = file.read()

pattern10 = r'\d'
res10 = re.sub(pattern10, '#', data10)
# print(res10)


with open('Regexp contest\\regexp-practice-11.txt', encoding='utf-8') as file:
    data11 = file.read()

pattern11 = r'<.+?>'
res11 = re.sub(pattern11, '', data11)
# print(res11)


with open('Regexp contest\\regexp-practice-12.txt', encoding='utf-8') as file:
    data12 = file.read()

res12 = re.sub('A', 'a', data12)
res12 = re.sub('B', 'b', res12)
res12 = re.sub('C', 'c', res12)
res12 = re.sub('D', 'D', res12)
res12 = re.sub('E', 'e', res12)
res12 = re.sub('F', 'f', res12)
res12 = re.sub('G', 'g', res12)
res12 = re.sub('H', 'h', res12)
res12 = re.sub('I', 'i', res12)
res12 = re.sub('J', 'j', res12)
res12 = re.sub('K', 'k', res12)
res12 = re.sub('L', 'l', res12)
res12 = re.sub('M', 'm', res12)
res12 = re.sub('N', 'n', res12)
res12 = re.sub('O', 'o', res12)
res12 = re.sub('P', 'p', res12)
res12 = re.sub('Q', 'q', res12)
res12 = re.sub('R', 'r', res12)
res12 = re.sub('S', 's', res12)
res12 = re.sub('T', 't', res12)
res12 = re.sub('U', 'u', res12)
res12 = re.sub('V', 'v', res12)
res12 = re.sub('W', 'w', res12)
res12 = re.sub('X', 'x', res12)
res12 = re.sub('Y', 'y', res12)
res12 = re.sub('Z', 'z', res12)
# print(res12)


with open('Regexp contest\\regexp-practice-13.txt', encoding='utf-8') as file:
    data13 = file.read()

data13 = re.sub(',', '', data13)
pattern13 = r'\b([A-Za-zА-ЯЁа-яё]+)(\s|\.|,)+(?=\1)'
matches13 = re.finditer(pattern13, data13)
res13 = [match.group() for match in matches13]
# print(*res13, sep='\n')


with open('Regexp contest\\regexp-practice-14.txt', encoding='utf-8') as file:
    data14 = file.read()

pattern14 = r'\b[A-ZА-ЯЁ][a-zа-яё]+\s[A-ZА-ЯЁ][a-zа-яё]+\s[A-ZА-ЯЁ][a-zа-яё]+\b'
matches14 = re.finditer(pattern14, data14)
res14 = [match.group() for match in matches14]
# print(*res14, sep='\n')


with open('Regexp contest\\regexp-practice-15.txt', encoding='utf-8') as file:
    data15 = file.read()

pattern15 = r''
matches15 = re.finditer(pattern15, data15)
res15 = [match.group() for match in matches15]
print(*res15, sep='\n')
