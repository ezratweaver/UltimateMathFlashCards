from tkinter import Canvas, Button, font
from typing import List
from user_data import get_userlist_banner, check_for_users, get_font_size
from assets import root, WINDOW_COLOR, userscreen_banners
import assets
import controller_variables

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

user_title_font = font.Font(family="Encode Sans", size=20)

current_user = None

class UserScreenGUI:

    def __init__(self) -> None:
        self.canvas = Canvas(
            root, bg=WINDOW_COLOR,
            height=500, width = 800,
            bd=0, highlightthickness=0,
            relief="ridge")

    def print_banner(self) -> None:
        self.userlist_banner = self.canvas.create_image(
            400,
            250,
            image=get_userlist_banner(usercount, userscreen_banners)
        )

    def button_bg_modify(event, color, canvas,
                        image_id, new_image):
        event.widget.config(bg=color, activebackground=color)
        canvas.itemconfigure(image_id, image=new_image)

    def print_user_buttons(self, usercount: int) -> List[object]:
        """
        Create and configure user buttons in the graphical user interface.

        Parameters:
            self: The instance of the class.
            usercount: An integer representing the number of users for whom buttons 
                        need to be created.
        """
        y_start_pos = START_POSITIONS.get(usercount)
        title_buttons = []
        title_buttons_bg = []
        action_buttons = []
        action_buttons_bg = []
        if usercount >= MAX_USERS: #Add an extra button if MAX_USERS has not been
            usercount = MAX_USERS - 1                     #reached, otherwise dont.
        for x in range(usercount + 1):
            title_buttons_bg.append(self.canvas.create_image(
                434,
                y_start_pos,
                image=assets.button_long))
            action_buttons_bg.append(self.canvas.create_image(
                314,
                y_start_pos,
                image=assets.button_square))
            title_buttons.append(Button(
                self.canvas,
                fg="#000000",
                bg="#D9D9D9",
                activebackground="#D9D9D9",
                anchor="center",
                borderwidth=0,
                highlightthickness=0,
                relief="flat"))
            title_buttons[x].place(x = 354, y = y_start_pos - 21,
                                 width=160.0, height=43.0)
            action_buttons.append(Button(
                self.canvas,
                fg="#000000",
                bg="#D9D9D9",
                activebackground="#D9D9D9",
                image=assets.userscreen_useradd,
                anchor="center",
                borderwidth=0,
                highlightthickness=0,
                relief="flat"))
            action_buttons[x].place(x = 289, y = y_start_pos - 21,
                                    width=50.0, height=43.0)
            y_start_pos = y_start_pos + 65
        for x, user in enumerate(all_users):
            font_size = get_font_size(user["displayname"], title_buttons[x],
                                       user_title_font, root)
            title_buttons[x].config(text=f"{user['displayname']}", 
                                    command=lambda x=x: setattr(self, "current_user", 
                                    self.log_into_user(x)),
                                    font=("Encode Sans", font_size))
            action_buttons[x].config(image=assets.userscreen_userprofile, 
                        command=lambda x=x: setattr(self, "current_user", 
                        self.view_user(x)))
        for x, title_button in enumerate(title_buttons):
            title_button.bind("<Enter>", lambda event, x=x: 
                UserScreenGUI.button_bg_modify(event, "#C3C3C3", self.canvas,
                            title_buttons_bg[x], assets.button_long_selected))
            title_button.bind("<Leave>" , lambda event, x=x: 
                UserScreenGUI.button_bg_modify(event, "#D9D9D9", self.canvas,
                            title_buttons_bg[x], assets.button_long))
        for x, action_button in enumerate(action_buttons):
            action_button.bind("<Enter>", lambda event, x=x: 
                UserScreenGUI.button_bg_modify(event, "#C3C3C3", self.canvas,
                            action_buttons_bg[x], assets.button_square_selected))
            action_button.bind("<Leave>" , lambda event, x=x: 
                UserScreenGUI.button_bg_modify(event, "#D9D9D9", self.canvas,
                            action_buttons_bg[x], assets.button_square))

    def log_into_user(self, user_position) -> dict:
        controller_variables.main_screen = True
        return all_users[user_position]
    
    def view_user(self, user_position) -> dict:
        controller_variables.profile_screen = True
        return all_users[user_position]

    def run_gui(self) -> None:
        self.print_banner()
        self.print_user_buttons(usercount)

    def show_canvas(self) -> None:
        self.canvas.pack()

    def hide_canvas(self) -> None:
        self.canvas.pack_forget()

if __name__ == "__main__":
    userscreen = UserScreenGUI()
    userscreen.run_gui()
    userscreen.show_canvas()
    root.title("Userscreen Individual Screen")
    root.mainloop()
