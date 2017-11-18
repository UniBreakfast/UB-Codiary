from consolekeycatch import catch_key


def greeting(text):
    print('\n '+'~'*78)
    print(' '*((80-len(text))//2)+text)
    print(' '+'~'*78+'\n')


def vertical_menu(choice_list, header=None, footer=None, data=None, master=None):
    done = False
    while not done:

        try:    header_str = header(data)
        except:    header_str = header

        width = max([len(choice[0]) for choice in choice_list])
        print()
        print(('     '+str(header_str)+'\n   '+'-'*(width+6))*bool(header_str), end='')
        print()
        for num, choice in enumerate(choice_list):
            print('   ', str(num+1)+'.', choice[0])
        print(('   '+'-'*(max(width+6, len(str(footer))+4))+'\n     '+str(footer))*bool(footer), end='\n\n\n')
        choice = 0
        choice = catch_key(list(range(1, len(choice_list)+1)))
        done = choice_list[choice-1][1]()


def add_entry_dialog(prompt=None, button=None, data=None, master=None):
    line = input(' '+prompt+'\n   ')
    data.itemlist.append(data.CustomObject(line))

