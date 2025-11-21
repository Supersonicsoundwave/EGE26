for n in range(40, 0, -1):
    if bin(n)[-4:] == '1011':
        print(n)
        break