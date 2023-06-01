from tkinter import Canvas, Button
from userdata import get_userlist_banner, get_user_count
from assets import window, WINDOW_COLOR
import assets

user_y_start_pos = {
    0 : 250,
    1 : 218,
    2 : 186,
    3 : 154,
    4 : 121,
    5 : 88,
    6 : 88,
}

class UserScreenGUI:

    def __init__(self) -> None:
        self.userscreen_canv = Canvas(
            window, bg=WINDOW_COLOR,
            height=500, width = 800,
            bd=0, highlightthickness=0,
            relief="ridge")
        self.userscreen_canv.pack()

    def print_banner(self) -> None:
        self.userlist_banner = self.userscreen_canv.create_image(
            400,
            250,
            image=get_userlist_banner()
        )

    def print_button_bg(self) -> None:
        usercount = get_user_count()
        if usercount >= 6:
            usercount = 5
        y_start_pos = user_y_start_pos.get(usercount)
        userbuttons = []
        for x in range(usercount + 1):
            self.userscreen_canv.create_image(
                434,
                y_start_pos,
                image=assets.usertitlebg
            )
            self.userscreen_canv.create_image(
                314,
                y_start_pos,
                image=assets.useractionbg
            )
            userbuttons.append(Button(self.userscreen_canv))
            print(userbuttons[x - 1].place(x = 434, y = y_start_pos - 13))
            y_start_pos = y_start_pos + 65

    def run_gui(self) -> None:
        self.print_banner()
        self.print_button_bg()


userscreen = UserScreenGUI()
userscreen.run_gui()
window.geometry("800x500")
window.title("")
window.resizable(False, False)
window.mainloop()
