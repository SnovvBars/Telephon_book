import UI as UI
import r_txt as r_txt
import search as search

def button_click():
    item = UI.select_main_item()
    if item == 1:
        item = UI.data_input()
        r_txt.write_txt(item)
    if item == 2:
        item = search.data_search()

    print(item) 

button_click()