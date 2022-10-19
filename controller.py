import UI as UI
import r_txt as r_txt

def button_click():
    item = UI.select_main_item()
    if item == 1:
        item = UI.data_input()
        r_txt.write_txt(item)
    print(item) 

button_click()