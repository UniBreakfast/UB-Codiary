

def add_item_dialog(master=None):
    view.add_entry_dialog('Type or paste new '+objecttype+' below and press Enter',
                          'Enter', data, master)



def main():
    greet = 'Hello! This is '+viewtype+' interface for storing great '+objecttype+'s'
    view.greeting(greet)

    data.itemlist = data.CustomList()

    main_menu_items = [('Add new '+objecttype, add_item_dialog),
                       ('View stored '+objecttype+'s', lambda x: print('2')),
                       ('Exit', lambda x: print('3'))]

    view.vertical_menu(main_menu_items, lambda data: str(len(data.itemlist))+' '+
                       objecttype+'s stored', 'new '+objecttype+
                       's currently cannot be added due to unwritten code', data)



    try:    view.loop()
    except:    pass
