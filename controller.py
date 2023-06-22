from user_screen import UserGUI, root
from text_screen import EnterTextGUI
import controller_variables

screens = {"userscreen" : UserGUI(), "textscreen" : EnterTextGUI}

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

    def go_to_textscreen_check():
        if controller_variables.text_screen:
            controller_variables.text_screen = False
            Controller.hide_viewable_canvas()
            screens["textscreen"].show_canvas()
        root.after(70, Controller.go_to_textscreen_check)


functions = [
    getattr(Controller, attr) for attr in dir(
        Controller) if callable(
            getattr(Controller, attr)) and attr.startswith('go')
            ]
for function in functions:
    function()
