
screens = []

class Screen:
    exist = False
    window = None

    def __init__(self, template, name, parent=None, title=None, header=None, footer=None,
                 startwith=None, endwith=None):
        face.screens.append(self)
        self.template  = template
        self.startwith = startwith
        self.endwith   = endwith
        self.name   = name
        self.parent = parent
        self.title  = title if title else name
        self.header = header
        self.footer = footer

        #self. =

    def __call__(self, event=None):
        if self.exist:    self.window.focus()
        else:      return self.show()

    def show(self):
        return self.template(self)
