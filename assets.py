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

userlist_banners = {
    1: PhotoImage(file="assets/userscreen/userlist_1.png"),
    2: PhotoImage(file="assets/userscreen/userlist_2.png"),
    3: PhotoImage(file="assets/userscreen/userlist_3.png"),
    4: PhotoImage(file="assets/userscreen/userlist_4.png"),
    5: PhotoImage(file="assets/userscreen/userlist_5.png"),
    6: PhotoImage(file="assets/userscreen/userlist_6.png"),
}

image_usertitlebg = PhotoImage(
    file="assets/userscreen/usertitlebg.png")
image_useractionbg = PhotoImage(
    file="assets/userscreen/useractionbg.png")
image_usertitlebg_selected = PhotoImage(
    file="assets/userscreen/usertitlebg_selected.png")
image_useractionbg_selected = PhotoImage(
    file="assets/userscreen/useractionbg_selected.png")
image_useradd = PhotoImage(
    file="assets/userscreen/useradd.png")
image_userprofile = PhotoImage(
    file="assets/userscreen/userprofile.png")
