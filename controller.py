from userscreen import UserScreenGUI, root

userscreen = UserScreenGUI()

class Controller:
    def go_to_mainscreen_check():
        if userscreen.main_screen:
            userscreen.main_screen = False
            userscreen.hide_canvas()
        root.after(70, Controller.go_to_mainscreen_check)

    def go_to_profilescreen_check():
        if userscreen.profile_screen:
            userscreen.profile_screen = False
            userscreen.hide_canvas()
        root.after(70, Controller.go_to_profilescreen_check)

Controller.go_to_mainscreen_check()
Controller.go_to_profilescreen_check()