import sys

sys.path.append("./utilities")
sys.path.append("./assets")

import screens.user_screen
import screens.text_screen
import screens.profile_screen
import memory
import assets
import user_data

screen_objects = { "user_screen" : screens.user_screen.UserScreen(), "text_screen" : screens.text_screen.TextScreen(),
                  "profile_screen" : screens.profile_screen.ProfileScreen() }


def hide_viewable_canvas():
    for _, screen in screen_objects.items():
        if screen.canvas.winfo_viewable():
            screen.hide_canvas()

# SHOW SCREENS FUNCTIONS 

def show_userscreen():
    hide_viewable_canvas()
    screen_objects["user_screen"].show_canvas()
    user_screen_init()


def show_profile_screen():
    hide_viewable_canvas()
    screen_objects["profile_screen"].show_canvas()
    profile_screen_init()


def show_text_screen():
    hide_viewable_canvas()
    screen_objects["text_screen"].show_canvas()

# USER_SCREEN FUNCTIONS

def title_button_pressed(position):
    memory.current_user = position
    print(memory.all_users[memory.current_user])


def action_button_pressed(position):
    memory.current_user = position
    show_profile_screen()


def empty_action_button_pressed():
    show_text_screen()
    screen_objects["text_screen"].buttons["confirm_button"].config(command=create_user_action)
    screen_objects["text_screen"].buttons["cancel_button"].config(command=show_userscreen)
    screen_objects["text_screen"].text_entry.bind("<Return>", create_user_action)


def user_screen_init():
    action_buttons = screen_objects["user_screen"].action_buttons
    title_buttons = screen_objects["user_screen"].title_buttons

    for x in range(len(action_buttons)):
        if title_buttons[x].cget("text") != "":
            title_buttons[x].config(command=lambda x=x: title_button_pressed(x)) 
            action_buttons[x].config(command=lambda x=x: action_button_pressed(x))
        else:
            action_buttons[x].config(command=empty_action_button_pressed)

# TEXT_SCREEN FUNCTIONS

def create_user_action(_=None):
    entry_data = screen_objects["text_screen"].text_entry.get()
    user_data.create_user(entry_data)
    show_userscreen()
    

def rename_user_action(_=None):
    entry_data = screen_objects["text_screen"].text_entry.get()
    current_user = memory.all_users[memory.current_user] 
    new_user_dict = user_data.rename_user(current_user, entry_data)
    user_data.dump_user(new_user_dict)
    show_profile_screen()


# PROFILE_SCREEN FUNCTIONS

def profile_screen_init():
    screen_objects["profile_screen"].buttons["back_button"].config(command=back_button_pressed)
    screen_objects["profile_screen"].buttons["rename_button"].config(command=rename_button_pressed)


def back_button_pressed():
    show_userscreen()


def history_button_pressed():
    pass


def delete_user():
    pass


def rename_button_pressed():
    screen_objects["text_screen"].buttons["confirm_button"].config(command=rename_user_action)
    screen_objects["text_screen"].text_entry.bind("<Return>", rename_user_action)
    screen_objects["text_screen"].buttons["cancel_button"].config(command=show_profile_screen)
    show_text_screen()

