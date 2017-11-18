def greeting(text):
    print('\n '+'~'*78)
    print(' '*((80-len(text))//2)+text)
    print(' '+'~'*78+'\n')


def vertical_menu(choice_list, header=None, footer=None):
    done = False
    while not done:
        width = max([len(choice[0]) for choice in choice_list])
        print(('     '+str(header)+'\n   '+'-'*(width+6))*bool(header), end='')
        print()
        for num, choice in enumerate(choice_list):
            print('   ', str(num+1)+'.', choice[0])
        print(('   '+'-'*(max(width+6, len(str(footer))+4))+'\n     '+str(footer))*bool(footer))
        choice = 0
        while choice not in range(1, len(choice_list)+1):
            try:    choice = int(input())
            except:    continue
        done = choice_list[choice-1][1]()
