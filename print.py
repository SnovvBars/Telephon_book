import os

def data_fam():    
    print ('')
    count = 0
    with open('t_book.txt', 'r', encoding="utf-8") as fp:
        for n, line in enumerate(fp, 1):
# Составили словарь для одной записи
            dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
            if dic : count += 1
# Вывели фамилмю
            print(" {}. ФИО: {}".format(count, dic['famaly']))
# Не нашлизапись
    if count == 0: print(" Никого нет!")
    print ('')
    os.system("pause")

# Выводим все поля и все записи из текстового файла
def data_all():    
    print ('')
    count = 0
    with open('t_book.txt', 'r', encoding="utf-8") as fp:
        for n, line in enumerate(fp, 1):
            dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
            if dic : count += 1
            print(" {}. ФИО:{:>16} | Тел.:{:>18} | Комм.:{:>9} | Пол:{:>2} | Статус:{:>14}"
                    .format(count, dic['famaly'], dic['telephone'], dic['own'], dic['gender'], dic['status']))            
    if count == 0: print(" Никого нет!")
    print ('')
    os.system("pause")