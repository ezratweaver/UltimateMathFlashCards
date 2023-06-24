from tkinter import Tk, PhotoImage
from os import path, chdir
from sys import argv

exe_dir = path.dirname(path.abspath(argv[0]))
chdir(exe_dir)

WINDOW_COLOR = "#3556FB"

USERSCREEN_FOLDER = "userscreen"
TEXTSCREEN_FOLDER = "textscreen"

root = Tk()
root.geometry("800x500")
root.title("")
root.resizable(False, False)

def image_modify(event, active, canvas,
                    image_id, new_image):
    if active:
        color = "#C3C3C3"
    if not active:
        color = "#D9D9D9"
    event.widget.config(bg=color, activebackground=color)
    canvas.itemconfigure(image_id, image=new_image)

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
#USER SCREEN ASSETS
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
#ENTER TEXT SCREEN ASSETS
textscreen_confirm = add_asset(
    TEXTSCREEN_FOLDER, "confirm")
textscreen_cancel = add_asset(
    TEXTSCREEN_FOLDER, "cancel")
textscreen_please_enter_name = add_asset(
    TEXTSCREEN_FOLDER, "please_enter_name")
textscreen_username_enter_banner = add_asset(
    TEXTSCREEN_FOLDER, "username_enter_banner")
textscreen_enterbox = add_asset(
    TEXTSCREEN_FOLDER, "enter_box")