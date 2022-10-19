import UI as UI
import r_txt as r_txt
import search as search

def button_click():
    item = UI.select_main_item()
    print(item)
    if item == 1:
        item = UI.data_input()
        r_txt.write_txt(item)
    # elif item == 2:
    #     item = search.data_search(item)
    # else : print(item)

    print(item) 

button_click()