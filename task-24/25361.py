from string import printable


with open(r'.\files\24_25361.txt') as file:
    data = file.readline()


F_count = 0
cnt = 0
max_len = 0

for i in range(len(data)):
    if data[i] in printable[:10] and int(data[i]) % 2 == 0:
        cnt += 1
        for j in range(i + 1, len(data)):
            if data[j] == 'F' and F_count == 76 or data[j] in printable[:10] and int(data[j]) % 2 == 0:
                if F_count == 76:
                    max_len = max(cnt, max_len)
                ans = ''
                cnt = 0
                F_count = 0
                break
            if data[j] == 'F':
                F_count += 1
            cnt += 1

max_len = max(cnt, max_len)
print(max_len)

