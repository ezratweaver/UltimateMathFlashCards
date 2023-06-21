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


#BUTTON BACKGROUNDS
buttonbg_long = PhotoImage(
    file="assets/userscreen/usertitlebg.png")
buttonbg_square = PhotoImage(
    file="assets/userscreen/useractionbg.png")
#USERSCREEN ASSETS
userscreen_banners = {
    1: PhotoImage(file="assets/userscreen/userlist_1.png"),
    2: PhotoImage(file="assets/userscreen/userlist_2.png"),
    3: PhotoImage(file="assets/userscreen/userlist_3.png"),
    4: PhotoImage(file="assets/userscreen/userlist_4.png"),
    5: PhotoImage(file="assets/userscreen/userlist_5.png"),
    6: PhotoImage(file="assets/userscreen/userlist_6.png"),
}
userscreen_usertitlebg_selected = PhotoImage(
    file="assets/userscreen/usertitlebg_selected.png")
userscreen_useractionbg_selected = PhotoImage(
    file="assets/userscreen/useractionbg_selected.png")
userscreen_useradd = PhotoImage(
    file="assets/userscreen/useradd.png")
userscreen_userprofile = PhotoImage(
    file="assets/userscreen/userprofile.png")
