from tkinter import Canvas, Button, font
from typing import List
from userdata import get_userlist_banner, check_for_users, grab_font_size
from assets import window, WINDOW_COLOR
import assets

MAX_USERS = 6
START_POSITIONS = {
    0 : 250,
    1 : 218, 2 : 186,
    3 : 154, 4 : 121,
    5 : 88, 6 : 88
}
FONT_SIZES = {
    1 : 27, 8 : 25,
    10 : 22, 12 : 18,
    14: 16, 15: 15
}

USER_BUTTON_DIMENSIONS = (43, 160)

all_users = check_for_users()
usercount = len(all_users)

user_title_font = font.Font(family="Encode Sans", size=25 * -1)

current_user = None

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
            image=get_userlist_banner(usercount)
        )

    def print_user_buttons(self, usercount) -> List[object]:
        y_start_pos = START_POSITIONS.get(usercount)
        title_buttons = []
        action_buttons = []
        if usercount >= MAX_USERS: #Add an extra button if MAX_USERS has not been
            usercount = MAX_USERS - 1                     #reached, otherwise dont.
        for x in range(usercount + 1):
            self.userscreen_canv.create_image(
                434,
                y_start_pos,
                image=assets.image_usertitlebg)
            self.userscreen_canv.create_image(
                314,
                y_start_pos,
                image=assets.image_useractionbg)
            title_buttons.append(Button(
                self.userscreen_canv,
                fg="#000000",
                bg="#D9D9D9",
                anchor="w",
                borderwidth=0,
                highlightthickness=0,
                relief="flat"))
            title_buttons[x].place(x = 354, y = y_start_pos - 21, 
                                 width=160.0, height=43.0)
            action_buttons.append(Button(
                self.userscreen_canv,
                fg="#000000",
                bg="#D9D9D9",
                image=assets.image_useradd,
                anchor="center",
                borderwidth=0,
                highlightthickness=0,
                relief="flat"))
            action_buttons[x].place(x = 289, y = y_start_pos - 21, 
                                    width=50.0, height=43.0)
            y_start_pos = y_start_pos + 65
        for x, user in enumerate(all_users):
            font_size = grab_font_size(user["displayname"], 
                    *USER_BUTTON_DIMENSIONS, user_title_font)
            print(f"username: {user['displayname']} | fontsize: {font_size}")
            title_buttons[x].config(text=f" {user['displayname']}", 
                                    command=lambda x=x: setattr(self, "current_user", 
                                    self.log_into_user(x)),
                                    font=("Encode Sans", font_size))
            action_buttons[x].config(image=assets.image_userprofile)

    def log_into_user(self, user_position) -> None:
        return all_users[user_position]

    def run_gui(self) -> None:
        self.print_banner()
        self.print_user_buttons(usercount)

userscreen = UserScreenGUI()
userscreen.run_gui()
window.geometry("800x500")
window.title("")
window.resizable(False, False)
window.mainloop()
