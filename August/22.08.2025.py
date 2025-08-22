import re


# with open('files\\24-334.txt') as file:
#     data = file.readline()
#
# pattern = r'[1-9AB][0-9AB]*[02468A]'
# matches = re.finditer(pattern, data)
# res = [match.group() for match in matches]
# print(len(max(res, key=len)))


with open('files\\24-347.txt') as file:
    data = file.readline()

pattern = r'[1-7][0-7]*'
matches = re.finditer(pattern, data)
oct_numbers = [match.group() for match in matches]
multof13 = []
for oct_number in oct_numbers:
    if int(oct_number, 8) % 13 == 0:
        multof13.append(oct_number)
    else:
        test_number = oct_number
        for i in range(len(oct_number)):
            test_numberi = test_number[i:]
            for j in range(len(test_numberi)):
                test_numberj = test_numberi[:len(test_numberi)-j]
                if int(test_numberj, 8) % 13 == 0:
                    multof13.append(test_numberj.lstrip('0'))
                    break
mxln = len(max(multof13, key=len))
res = list(filter(lambda x: len(x) == mxln, multof13))
minnumb = min(res, key=int)
print(data.find(minnumb))