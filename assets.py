from tkinter import Tk, PhotoImage
from os import path, chdir
from sys import argv

EXE_DIR = path.dirname(argv[0])
chdir(EXE_DIR)

WINDOW_COLOR = "#3556FB"

window = Tk()

class Assets:
    userlist_banners = {
        1: PhotoImage(file="assets/userscreen/userlist_1.png"),
        2: PhotoImage(file="assets/userscreen/userlist_2.png"),
        3: PhotoImage(file="assets/userscreen/userlist_3.png"),
        4: PhotoImage(file="assets/userscreen/userlist_4.png"),
        5: PhotoImage(file="assets/userscreen/userlist_5.png"),
        6: PhotoImage(file="assets/userscreen/userlist_6.png"),
    }
    usertitlebg = PhotoImage(file="assets/userscreen/usertitlebg.png")
    useractionbg = PhotoImage(file="assets/userscreen/useractionbg.png")
    useradd = PhotoImage(file="assets/userscreen/useradd.png")
    userprofile = PhotoImage(file="assets/userscreen/userprofile.png")
