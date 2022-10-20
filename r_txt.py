import r_html

def write_txt(dic):
    for key, value in dic.items():
        if key == 'own' : dic[key] = finding_own(value)
        elif key == 'gender' : dic[key] = finding_gender(value)
        elif key == 'status' : dic[key] = finding_status(value)
    with open('t_book.txt', 'a', encoding = 'UTF_8') as file:
        file.write('{}\n'
            .format(', '.join('{}: {}'.format(key, val) for key, val in dic.items())))
    file.close()
    r_html.save_html()

def finding_own(owns):
    if owns == 1: return 'Личный'
    elif owns == 2: return 'Рабочий'
    else: return 'Домашний'

def finding_gender(gender):
    if gender == 1: return 'м'
    elif gender == 2: return 'ж'
    
def finding_status(status):
    if status == 1: return 'Женат\\Замужем'
    elif status == 2: return 'Холост'
    else: return 'В разводе'    