from string import printable


for x in printable[:20][::-1]:
    a = int(f'627{x}j8', 20)
    b = int(f'h45i{x}5hij', 20)
    c = int(f'4idb49j{x}7', 20)
    f = a + b + c
    if f % 19 == 0:
        print(f // 19)