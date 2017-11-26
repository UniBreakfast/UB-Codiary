import tkinter as tki


class Header(tki.Label):
    def __init__(self, master, text):
        super().__init__(self, master, text)


def scr_text(text):
    view.root = tki.Tk()
    tki.Label(view.root, text=text).pack()



def loop():
    for root in [screen for screen in face.screens if not screen.parent]:
        root()
        root.window.mainloop()


def go_out():
    pass


def make_window(screen):
    if screen.parent:
        screen.window = tki.Toplevel(screen.parent.window)
        screen.window.transient(screen.parent.window)
    else:
        screen.window = tki.Tk()
    screen.window.title(screen.title)
    return screen.window


def vertical_menu(screen):
    window = make_window(screen)

    if screen.header:
        header = screen.header if type(screen.header) is str else screen.header()
        screen.lb_header = tki.Label(window, text=header)
        screen.lb_header.pack()

    screen.bt_menuitems = []
    for item in screen.menuitems:
        screen.bt_menuitems.append(tki.Button(window, text=item[0], command=item[1]))
    for bt_item in screen.bt_menuitems:    bt_item.pack()

    if screen.footer:
        footer = screen.footer if type(screen.footer) is str else screen.footer()
        screen.lb_footer = tki.Label(window, text=footer)
        screen.lb_footer.pack()

    if screen.startwith:    window.bind('<Expose>', screen.startwith)


def info(screen):
    window = make_window(screen)

    text = screen.text if type(screen.text) is str else screen.text()
    screen.lb_text = tki.Label(window, text=text)
    screen.lb_text.pack()

    if screen.startwith:    window.bind('<Expose>', screen.startwith)



def listing():
    pass
def prompt():
    pass
