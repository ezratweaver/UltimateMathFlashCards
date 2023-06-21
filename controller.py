from user_screen import UserScreenGUI, root
import controller_variables

userscreen = UserScreenGUI()

class Controller:
    def go_to_mainscreen_check():
        if controller_variables.main_screen:
            controller_variables.main_screen = False
            userscreen.hide_canvas()
        root.after(70, Controller.go_to_mainscreen_check)

    def go_to_profilescreen_check():
        if controller_variables.profile_screen:
            controller_variables.profile_screen = False
            userscreen.hide_canvas()
        root.after(70, Controller.go_to_profilescreen_check)

Controller.go_to_mainscreen_check()
Controller.go_to_profilescreen_check()