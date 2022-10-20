import os

def save_html():    
    # print ('')
    # count = 0
    str_html = '<html><body><table border = 1><tr><td>ID</td><td>ФИО</td><td>Телефон</td><td>Комм</td><td>Пол</td><td>Статус</td></tr><tr>'
    with open('t_book.txt', 'r', encoding="utf-8") as fp:
        for n, line in enumerate(fp, 1):
            dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
            str_html = str_html + form_line(dic)
            # print(form_line(dic))
            # print(" {}. ФИО:{:>16} | Тел.:{:>18} | Комм.:{:>9} | Пол:{:>2} | Статус:{:>14}"
            #         .format(count, dic['famaly'], dic['telephone'], dic['own'], dic['gender'], dic['status']))            
    str_html = str_html + '</tr></table></body></html>'
    save_file_html(str_html)
    # if count == 0: print(" Никого нет!")
    # print ('')
    # print ('key')

def form_line(line):
    # print ('key')
    str = '<tr>'
    for key in line:
        # print (line[key][0])
        str = str + '<td>' + line[key] + '</td>'
    return str + '</tr>'
    # f = open('t_book.html', 'w', encoding = 'utf-8')

def save_file_html(html_str):
    if os.path.isfile('t_book.html'):
        os.remove('t_book.html')
    f = open("t_book.html", 'w', encoding = 'utf-8')
    f.write(html_str)
    f.close()