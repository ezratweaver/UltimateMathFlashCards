from user_screen import UserGUI, root
from text_screen import EnterTextGUI
from controller_variables import screen_variables

screens = {"user_screen" : UserGUI(), "text_screen" : EnterTextGUI()}

class Controller:

    def hide_viewable_canvas():
        for _, screen in screens.items():
            if screen.canvas.winfo_viewable():
                screen.hide_canvas()

    def screen_variable_check():
        for screen, boolean in screen_variables.items():
            if boolean:
                Controller.hide_viewable_canvas()
                screens[screen].show_canvas()
                screen_variables[screen] = False
        root.after(70, Controller.screen_variable_check)

Controller.screen_variable_check()
