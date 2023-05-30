from tkinter import Canvas
from assets import window, WINDOW_COLOR
from userdata import get_userlist_banner

class UserScreenGUI:

    def __init__(self) -> None:
        self.userscreen_canv = Canvas(
            window, bg=WINDOW_COLOR,
            height=500, width = 800,
            bd=0, highlightthickness=0,
            relief="ridge")
        self.userscreen_canv.pack()

        self.userlist_banner = self.userscreen_canv.create_image(
            400,
            250,
            image=get_userlist_banner()
        )

userscreen = UserScreenGUI()
window.geometry("800x500")
window.title("")
window.resizable(False, False)
window.mainloop()
