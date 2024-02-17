import sys

sys.path.append("./utilities")
sys.path.append("./assets")

import screens.user_screen
import screens.text_screen
import screens.profile_screen
import memory
import assets

print(memory.all_users)

screen_objects = { "user_screen" : screens.user_screen.UserScreen(), "text_screen" : screens.text_screen.TextScreen(),
                  "profile_screen" : screens.profile_screen.ProfileScreen() }


def hide_viewable_canvas():
    for _, screen in screen_objects.items():
        if screen.canvas.winfo_viewable():
            screen.hide_canvas()

 
def show_userscreen():
    screen_objects["user_screen"].show_canvas()


def show_profile_screen():
    screen_objects["profile_screen"].show_canvas()


def user_screen_init():
    action_buttons = screen_objects["user_screen"].action_buttons
    title_buttons = screen_objects["user_screen"].title_buttons

    for x in range(len(action_buttons)):
        if title_buttons[x].cget("text") != "":
            title_buttons[x].config(command=lambda: print(memory.all_users[x])) 


