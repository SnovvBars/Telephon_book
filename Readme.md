MAIN - запускает программу через вызов метода модуля CONTROLLER
файл main.ru

CONTROLLER - обеспечивает взаимодействие модулей:
1. через UI взаимодействует с пользователем
2. ищет абонента через модуль SEARCH
3. удаляет абонента через DEL_DATA
4. выводит данные на терминал через PRINT_DATA
файл controller.py

Пункты главного меню (UI):
1. Ввести нового абонента:         
2. Вывести фамилии всех абонентов  
3. Вывести фамилии всех абонентов и их телефоны                   
4. Найти по фамилии                
5. Удалить абонента 
6. Очистить телефонную книгу               
7. Выход

Поля телефонной книги:
1. ID
2. ФИО
3. Телефон
4. Комментарий
5. Пол
6. Статус

Программа сохраняет данные в формате txt и html

