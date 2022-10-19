

# def data_search(flag):
#     if flag != 'fam' : elem = str(input('\n Введите часть фамилии или фамилию целиком: '))

#     print ('')
    
#     with open('t_book.txt', 'r', encoding="utf-8") as fp:
#         count = 0
#         for n, line in enumerate(fp, 1):
#             dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
#             if flag == 'fam':
#                 if elem.lower() in dic['famaly'].lower():
#                     print(dic['famaly'])
#                     count += 1
#             elif flag == 'all':
#                 if elem.lower() in dic['famaly'].lower():
#                     count += 1
#                     print(" ФИО:{:15}, | Телефон:{:>17}, | Комментарий:{:>9}, | Пол:{:>2}, | Соцстатус:{:>14}"
#                     .format(dic['famaly'], dic['telephone'], dic['own'], dic['gender'], dic['status']))            
#         if count == 0 or elem == '' : print(" Не найдено!")
#     print ('')


def data_fam():    
    print ('')
    count = 0
    with open('t_book.txt', 'r', encoding="utf-8") as fp:
        for n, line in enumerate(fp, 1):
            dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
            if dic : count += 1
            print(" ФИО: {}".format(dic['famaly']))
    if count == 0: print(" Никого нет!")
    print ('')

def data_all():    
    print ('')
    count = 0
    with open('t_book.txt', 'r', encoding="utf-8") as fp:
        for n, line in enumerate(fp, 1):
            dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
            if dic : count += 1
            print(" {} ФИО:{:>12}, | Тел.:{:>17}, | Комментарий:{:>9}, | Пол:{:>2}, | Соцстатус:{:>14}"
                    .format(dic['id'], dic['famaly'], dic['telephone'], dic['own'], dic['gender'], dic['status']))            
    if count == 0: print(" Никого нет!")
    print ('')

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
                    print(" {:>4} ФИО:{:>12}, | Телефон:{:>17}, | Комментарий:{:>9}, | Пол:{:>2}, | Соцстатус:{:>14}"
                        .format(dic['famaly'], dic['telephone'], dic['own'], dic['gender'], dic['status']))            
            if count == 0 : print(" Не найдено!")
    print ('')