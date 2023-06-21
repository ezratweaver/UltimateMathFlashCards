from tkinter import Tk, PhotoImage
from os import path, chdir
from sys import argv

exe_dir = path.dirname(path.abspath(argv[0]))
chdir(exe_dir)

WINDOW_COLOR = "#3556FB"

USERSCREEN_FOLDER = "userscreen"

root = Tk()
root.geometry("800x500")
root.title("")
root.resizable(False, False)

def add_asset(subfolder, filename):
    """
    Load image asset from 'assets/subfolder/filename.png' and return PhotoImage obj.

    Parameters:
        subfolder (str): Subfolder name inside 'assets' directory.
        filename (str): Name of the image file to load (extension must be .png).

    Returns:
        PhotoImage: Loaded image asset as a PhotoImage object.

    """
    return PhotoImage(file=f"assets/{subfolder}/{filename}.png")

#BUTTON BACKGROUNDS
button_long = add_asset(
    "buttons", "button_long")
button_long_selected = add_asset(
    "buttons", "button_long_selected")
button_square = add_asset(
    "buttons", "button_square")
button_square_selected = add_asset(
    "buttons", "button_square_selected")
#USERSCREEN ASSETS
userscreen_banners = {
    1: PhotoImage(file="assets/userscreen/userlist_1.png"),
    2: PhotoImage(file="assets/userscreen/userlist_2.png"),
    3: PhotoImage(file="assets/userscreen/userlist_3.png"),
    4: PhotoImage(file="assets/userscreen/userlist_4.png"),
    5: PhotoImage(file="assets/userscreen/userlist_5.png"),
    6: PhotoImage(file="assets/userscreen/userlist_6.png"),
}
userscreen_useradd = add_asset(
    USERSCREEN_FOLDER, "useradd")
userscreen_userprofile = add_asset(
    USERSCREEN_FOLDER, "userprofile")
userscreen_confirm = add_asset(
    USERSCREEN_FOLDER, "confirm")
userscreen_cancel = add_asset(
    USERSCREEN_FOLDER, "cancel")
userscreen_please_enter_name = add_asset(
    USERSCREEN_FOLDER, "please_enter_name")
userscreen_username_enter_banner = add_asset(
    USERSCREEN_FOLDER, "username_enter_banner")
