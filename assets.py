from tkinter import Tk, PhotoImage
from os import path, chdir
from sys import argv

exe_dir = path.dirname(path.abspath(argv[0]))
chdir(exe_dir)

WINDOW_COLOR = "#3556FB"

window = Tk()


userlist_banners = {
    1: PhotoImage(file="assets/userscreen/userlist_1.png"),
    2: PhotoImage(file="assets/userscreen/userlist_2.png"),
    3: PhotoImage(file="assets/userscreen/userlist_3.png"),
    4: PhotoImage(file="assets/userscreen/userlist_4.png"),
    5: PhotoImage(file="assets/userscreen/userlist_5.png"),
    6: PhotoImage(file="assets/userscreen/userlist_6.png"),
}

image_usertitlebg = PhotoImage(file="assets/userscreen/usertitlebg.png")
image_useractionbg = PhotoImage(file="assets/userscreen/useractionbg.png")
image_useradd = PhotoImage(file="assets/userscreen/useradd.png")
image_userprofile = PhotoImage(file="assets/userscreen/userprofile.png")
