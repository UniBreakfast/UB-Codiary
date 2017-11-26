

def scr_text(text):
    def scr_root():
        print(text)
    view.scr_root = scr_root


def loop():
    for root in [screen for screen in face.screens if not screen.parent]:
        done = False
        while not done:    done = root()



