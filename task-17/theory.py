with open('путь до файла') as file:
    # весь файл с \n
    data = file.read()
    # одна строчка
    data = file.readline()
    # список строчек lst[str]
    data = file.readlines()
