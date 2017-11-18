import tkinter as tki


def loop():

    try:    greet()
    except:    pass

    root.mainloop()


def greeting(text):
    global greet
    def greet():
        wnd_greet = tki.Toplevel(root)
        wnd_greet.transient(root)
        wnd_greet.focus()
        wnd_greet.geometry('+300+300')
        tki.Label(wnd_greet, text=text).pack(padx=10, pady=10)
        tki.Button(wnd_greet, text='Ok', command=wnd_greet.destroy).pack(pady=10)


def vertical_menu(choice_list, header=None, footer=None, master=None):
    global root
    try:
        root
        window = tki.Toplevel(master)
        window.transient(master)
        # to be continued
    except:
        root = tki.Tk()
        window = root

    if header:    tki.Label(window, text=header).pack(padx=10, pady=10)
    for choice in choice_list:
        tki.Button(window, text=choice[0], command=choice[1]).pack()
    if footer:    tki.Label(window, text=footer).pack(padx=10, pady=10)
