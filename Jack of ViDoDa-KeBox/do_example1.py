
def main():
    greet = 'Hello! This is '+viewtype+' interface for storing great one liners'
    view.greeting(greet)

    main_menu_items = [('Add new one liner', lambda: print('1')),
                       ('View stored one liners', lambda: print('2')),
                       ('Exit', lambda: (print('3'),))]

    view.vertical_menu(main_menu_items, '0 one liners stored',
                       'new one liners currently cannot be added due to unwritten code')



    try:    view.loop()
    except:    pass
