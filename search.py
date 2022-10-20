import os

def data_search():
    elem = str(input('\n Введите часть фамилии или фамилию целиком: '))
    print ('')
    if elem == '' : print(" Не найдено!")
    else:
        with open('t_book.txt', 'r', encoding="utf-8") as fp:
            count = 0
            for n, line in enumerate(fp, 1):
                dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
                if elem.lower() in dic['famaly'].lower():
                    count += 1
                    print(" {}. ФИО:{:>16} | Тел.:{:>18} | Комм.:{:>9} | Пол:{:>2} | Статус:{:>14}"
                        .format(count, dic['famaly'], dic['telephone'], dic['own'], dic['gender'], dic['status']))            
            if count == 0 : print(" Не найдено!")
    print ('')
    os.system("pause")