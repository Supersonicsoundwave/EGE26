with open(r'.\files\9832.txt') as file:
    data = [[int(j) for j in i.split()] for i in file]

for nums in data:
    dubs = [nums.count(num) for num in set(nums)]
    cond1 = sorted(dubs) == [1, 1, 1, 2, 2]
    cond2 = nums.count(max(nums)) == 1
    if cond1 and cond2:
        print(sum(nums))
        break
