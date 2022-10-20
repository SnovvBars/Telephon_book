import os

def data_delete():
    elem = str(input('''
     Кого будем удалять?
     Введите часть фамилии или фамилию целиком: '''))
    print ('')
    count = 0
    if elem == '' : print(" Не найдено!")
    else:
        with open('t_book.txt', 'r', encoding="utf-8") as fp:
            for n, line in enumerate(fp, 1):
                dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
                if elem.lower() in dic['famaly'].lower():
                    count += 1
                    print(" id:{} | ФИО:{:>16} | Тел.:{:>18} | Комм.:{:>9} | Пол:{:>2} | Статус:{:>14}"
                        .format(dic['id'], dic['famaly'], dic['telephone'], dic['own'], dic['gender'], dic['status']))                                    
            if count == 0 :
                print(" Не найдено!")
                return False
        nun_del = input('\n Выберите id удаляемого: ')
        del_person(nun_del)

def del_person(num):
    if os.path.isfile('t_book.tmp'):
        os.remove('t_book.tmp')
    with open('t_book.txt', 'r', encoding="utf-8") as fp:
        for n, line in enumerate(fp, 1):
            dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
            if int(dic['id']) != int(num):
                with open('t_book.tmp', 'a', encoding = 'UTF_8') as fp_tmp:
                    fp_tmp.write(line)
                fp_tmp.close()
    fp.close()

    if os.path.isfile('t_book.txt'):
        os.remove('t_book.txt')
    else: print("File doesn't exists!")

    os.rename('t_book.tmp', 't_book.txt')
    print(" Сделано!\n")

def del_all():
    if os.path.isfile('t_book.tmp'):
        os.remove('t_book.tmp')
    if input('\n Вы уверены? Откат будет невозможен!!! (y/n): ') == 'y':
        if os.path.isfile('t_book.txt'):
            os.remove('t_book.txt')
        else: print("File doesn't exists!")
        
        f = open("t_book.txt", 'w', encoding="utf-8")
        f.close()
        print(" Сделано!\n")