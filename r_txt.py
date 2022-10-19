from datetime import datetime as dt
from time import time

# 17:26;data;{'famaly': 'dfaf', 'telephone': '13435', 'own': 2, 'gender': 1, 'st�tus': 2}

def write_txt(str):
    time = dt.now().strftime('%H:%M')
    with open('t_book.txt', 'a') as file:
        file.write('{};data;{}\n'
            .format(time, str))