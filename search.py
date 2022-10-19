

def data_search(flag):
    elem = str(input('\n Введите первые три буквы фамилии или фамилию целиком: '))
    # print (elem)

    # file = open("t_book.txt", "r", encoding="utf-8")

    with open('t_book.txt', 'r', encoding="utf-8") as fp:
        for n, line in enumerate(fp, 1):
            # Обработка строки 'line'
            line = line.rstrip('\n')
            print(f"Вывод строки: {n}) - {line}")

    # count = 0
    # while True:
    #     print(count)
    #     lines = file.readlines()
    #     # print(len(lines))
    #     # print (lines, '\n')
    #     if not lines:
    #         break
    #     count += 1
    # file.close

    # print(count)
    # for item in lines:
        # if elem in item:
        # print(item, '\n')
    # return find_str

# data_search(str)