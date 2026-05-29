from string import printable


for x in printable[:29]:
    f = int(f'463{x}7921', 29) + int(f'8241{x}153', 29)
    if f % 28 == 0:
        print(f // 28)
        break
