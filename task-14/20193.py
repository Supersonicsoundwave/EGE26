from string import printable


for x in printable[:18]:
    a = int(f'11h{x}05', 18)
    b = int(f'3f{x}54{x}8', 18)
    c = int(f'g{x}{x}{x}9', 18)
    f = a + b + c
    if f % 14 == 0:
        print(f // 14)
