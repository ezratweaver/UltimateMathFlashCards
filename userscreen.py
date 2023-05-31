from tkinter import Canvas
from userdata import get_userlist_banner, get_user_count
from assets import window, WINDOW_COLOR
import assets

usertitle_pos = {
    0 : 250,
    1 : 218,
    2 : 186,
    3 : 154,
    4 : 121,
    5 : 88,
}

class UserScreenGUI:

    def __init__(self) -> None:
        self.userscreen_canv = Canvas(
            window, bg=WINDOW_COLOR,
            height=500, width = 800,
            bd=0, highlightthickness=0,
            relief="ridge")
        self.userscreen_canv.pack()

    def print_screen(self) -> None:
        self.userlist_banner = self.userscreen_canv.create_image(
            400,
            250,
            image=get_userlist_banner()
        )

        usercount = get_user_count()
        start_pos = usertitle_pos.get(usercount)
        for _ in range(usercount + 1):
            self.userscreen_canv.create_image(
                434,
                start_pos,
                image=assets.usertitlebg
            )
            start_pos = start_pos + 65

userscreen = UserScreenGUI()
userscreen.print_screen()
window.geometry("800x500")
window.title("")
window.resizable(False, False)
window.mainloop()
