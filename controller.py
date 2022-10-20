import UI as UI
import r_txt as r_txt
import print as data_print
import search as search
import remove as rem


def button_click():
    item = UI.select_main_item()
    # print(item)
    if item == 1:
        item = UI.data_input()
        r_txt.write_txt(item)
    elif item == 2:
        item = data_print.data_fam()
    elif item == 3:
        item = data_print.data_all()
    elif item == 4:
        item = search.data_search()    
    elif item == 5:
        item = rem.data_delete()    

    # else : print(item)

    # print(item) 

button_click()