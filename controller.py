import sys

sys.path.append("./utilities")
sys.path.append("./assets")

import screens.user_screen
import screens.text_screen
import screens.profile_screen

import assets


screen_objects = { "user_screen" : screens.user_screen.UserScreen(), "text_screen" : screens.text_screen.TextScreen(),
                  "profile_screen" : screens.profile_screen.ProfileScreen() }



def user_screen_init():
    screen_objects["user_screen"]
