from tkinter import Tk, PhotoImage
from os import path, chdir
from sys import argv

exe_dir = path.dirname(path.abspath(argv[0]))
chdir(exe_dir)

WINDOW_COLOR = "#3556FB"

root = Tk()
root.geometry("800x500")
root.title("")
root.resizable(False, False)

def add_asset(subfolder, filename):
    """
    Loads an image asset from the 'assets' directory and returns a PhotoImage object.

    Parameters:
        string (str): The name or path of the image file to load. 
                      It should be relative to the 'assets' directory.

    Returns:
        PhotoImage: A PhotoImage object representing the loaded image asset.

    """
    return PhotoImage(file=f"assets/{subfolder}/{filename}.png")

#BUTTON BACKGROUNDS
button_long = PhotoImage(
    file="assets/buttons/button_long.png")
button_long_selected = PhotoImage(
    file="assets/buttons/button_long_selected.png")
button_square = PhotoImage(
    file="assets/buttons/button_square.png")
button_square_selected = PhotoImage(
    file="assets/buttons/button_square_selected.png")
#USERSCREEN ASSETS
userscreen_banners = {
    1: PhotoImage(file="assets/userscreen/userlist_1.png"),
    2: PhotoImage(file="assets/userscreen/userlist_2.png"),
    3: PhotoImage(file="assets/userscreen/userlist_3.png"),
    4: PhotoImage(file="assets/userscreen/userlist_4.png"),
    5: PhotoImage(file="assets/userscreen/userlist_5.png"),
    6: PhotoImage(file="assets/userscreen/userlist_6.png"),
}
userscreen_useradd = add_asset("userscreen", "useradd")
userscreen_userprofile = add_asset("userscreen", "userprofile")
userscreen_confirm = add_asset("userscreen", "confirm")
