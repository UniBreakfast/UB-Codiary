import tkinter as tki


def loop():

    try:    greet()
    except:    pass

    root.mainloop()


def rooting(master):
    global root
    try:
        root
        window = tki.Toplevel(master)
        window.transient(master)
        # to be continued
    except:
        root = tki.Tk()
        window = root
    return window


def greeting(text):
    global greet
    def greet():
        wnd_greet = tki.Toplevel(root)
        wnd_greet.transient(root)
        wnd_greet.focus()
        wnd_greet.geometry('+300+300')
        tki.Label(wnd_greet, text=text).pack(padx=10, pady=10)
        tki.Button(wnd_greet, text='Ok', command=wnd_greet.destroy).pack(pady=10)


def vertical_menu(choice_list, header=None, footer=None, data=None, master=None):
    window = rooting(master)

    try:    header_str = header(data)
    except:    header_str = header

    if header_str:    tki.Label(window, text=header_str).pack(padx=10, pady=10)
    for choice in choice_list:
        def cfunc(choice=choice):    choice[1](window)
        tki.Button(window, text=choice[0], command=cfunc).pack()
        #tki.Button(window, text=choice[0], command=lambda c=choice: c[1](window)).pack()
    if footer:    tki.Label(window, text=footer).pack(padx=10, pady=10)


def add_entry_dialog(prompt=None, button=None, data=None, master=None):
    window = rooting(master)
    tki.Label(window, text=prompt).pack(padx=10, pady=10)
    ntr = tki.Entry(window)
    ntr.pack(padx=10, pady=10, expand=True, fill='x')
    def take_ntr(_=0):
        data.itemlist.append(data.CustomObject(ntr.get()))
        print(data.itemlist)
        window.destroy()
        return 'break'
    ntr.bind('<Return>', take_ntr)
    tki.Button(window, text=button, command=lambda: (take_ntr(), window.destroy())).pack()
