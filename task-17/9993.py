from math import prod


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True


with open(r'.\files\17_9993.txt') as file:
    data = [int(i) for i in file]

max17 = max(i for i in data if abs(i) % 100 == 17)
ans = []
for nums in zip(data, data[1:]):
    cond1 = sum(is_prime(num) for num in nums)
    cond2 = abs(sum(nums)) % max17 == 0
    if cond1 == 1 and cond2:
        ans += [prod(nums)]
print(len(ans), max(ans))
