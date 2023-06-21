from user_screen import UserGUI, root
import controller_variables

screens = {"userscreen" : UserGUI(),}

class Controller:

    def hide_viewable_canvas():
        for _, screen in screens.items():
            if screen.canvas.winfo_viewable():
                screen.hide_canvas()

    def go_to_mainscreen_check():
        if controller_variables.main_screen:
            controller_variables.main_screen = False
            Controller.hide_viewable_canvas()
        root.after(70, Controller.go_to_mainscreen_check)

    def go_to_profilescreen_check():
        if controller_variables.profile_screen:
            controller_variables.profile_screen = False
            Controller.hide_viewable_canvas()
        root.after(70, Controller.go_to_profilescreen_check)

Controller.go_to_mainscreen_check()
Controller.go_to_profilescreen_check()