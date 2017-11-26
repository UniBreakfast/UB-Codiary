
def main():
    declare_general_screens()
    fill_greeting()
    fill_mainmenu()

    view.loop()


def declare_general_screens():
    face.scr_mainmenu = face.Screen(view.vertical_menu, 'Главное меню', None, 'PACER')

    face.scr_greeting = face.Screen(view.info, 'Приветствие', face.scr_mainmenu)

    face.scr_endeavors  = face.Screen(view.listing,       'Стремления', face.scr_mainmenu)
    face.scr_activities = face.Screen(view.listing,        'Действия',  face.scr_mainmenu)
    face.scr_quests     = face.Screen(view.listing,         'Квесты',   face.scr_mainmenu)
    face.scr_stats      = face.Screen(view.vertical_menu, 'Статистика', face.scr_mainmenu)

    face.scr_help = face.Screen(view.info, 'Подсказка', face.scr_mainmenu)

    face.scr_exitpromt = face.Screen(view.prompt, 'Конец?',    face.scr_mainmenu)


def fill_greeting():
    def unbind(event=None):
        try:       face.scr_greeting.parent.window.unbind('<Expose>')
        except:    pass
    face.scr_greeting.startwith = unbind
    face.scr_greeting.text = 'Текст приветствия'


def fill_mainmenu():
    face.scr_mainmenu.startwith = face.scr_greeting
    def header():
        header  = 'У тебя сейчас' + '\n'
        header += str(data.selfesteem) + ' Веры В Себя  и' + '\n'
        header += str(data.act_quests) + ' активных Квестов' + '\n'
        header += 'Чем займёмся?'
        return header
    face.scr_mainmenu.header = header
    face.scr_mainmenu.menuitems = [ ('Стремления', face.scr_endeavors,  1),
                                    ( 'Действия',  face.scr_activities, 2),
                                    (  'Квесты',   face.scr_quests,     3),
                                    ('Статистика', face.scr_stats,      4),
                                    (  'Выход',    view.go_out,     'Esc') ]
    face.scr_mainmenu.hotkeys = [ ('F1', face.scr_help) ]
    face.scr_mainmenu.footer = 'пользователь: ' + data.username
    face.scr_mainmenu.endwith = face.scr_exitpromt