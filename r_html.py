def save_html():    
    # print ('')
    # count = 0
    with open('t_book.txt', 'r', encoding="utf-8") as fp:
        for n, line in enumerate(fp, 1):
            dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
            save_file(dic)
            # print(" {}. ФИО:{:>16} | Тел.:{:>18} | Комм.:{:>9} | Пол:{:>2} | Статус:{:>14}"
            #         .format(count, dic['famaly'], dic['telephone'], dic['own'], dic['gender'], dic['status']))            
    # if count == 0: print(" Никого нет!")
    # print ('')
def save_file(line):
    str = '''
    
    '''
    f = open('t_book.html', 'w', encoding = 'utf-8')