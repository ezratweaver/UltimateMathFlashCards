import sys
sys.path.append("..")

from userscreen.user_screen import UserGUI, root
from textscreen.text_screen import EnterTextGUI
from profilescreen.profile_screen import ProfileGUI
from utilities.controller_variables import screen_variables

screens = {"user_screen" : UserGUI(), "text_screen" : EnterTextGUI(), # TODO: Rename screen names and chart them out
           "profile_screen" : ProfileGUI()}

class Controller:

    @staticmethod
    def hide_viewable_canvas():
        for _, screen in screens.items():
            if screen.canvas.winfo_viewable():
                screen.hide_canvas()

    @staticmethod
    def screen_variable_check():
        for screen, boolean in screen_variables.items():
            if boolean:
                screen_variables[screen] = False
                Controller.hide_viewable_canvas()
                screens[screen].show_canvas()
        root.after(1, Controller.screen_variable_check)


screens["profile_screen"].buttons["history_button"].config(command=lambda: print("History Button Pressed"))

# TODO: Rewrite controller using this /\ instead of previous implementations


Controller.screen_variable_check()
                
