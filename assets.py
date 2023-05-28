from tkinter import Tk, PhotoImage
from os import path, chdir
from sys import argv

EXE_DIR = path.dirname(argv[0])
chdir(EXE_DIR)

WINDOW_COLOR = "#3556FB"

window = Tk()

class Assets:
    usertitlebg = PhotoImage(file="assets/userscreen/usertitlebg.png")
    useractionbg = PhotoImage(file="assets/userscreen/useractionbg.png")
    useradd = PhotoImage(file="assets/userscreen/useradd.png")
    userprofile = PhotoImage(file="assets/userscreen/userprofile.png")
    userlist_1 = PhotoImage(file="assets/userscreen/userlist_1.png")
    userlist_2 = PhotoImage(file="assets/userscreen/userlist_2.png")
    userlist_3 = PhotoImage(file="assets/userscreen/userlist_3.png")
    userlist_4 = PhotoImage(file="assets/userscreen/userlist_4.png")
    userlist_5 = PhotoImage(file="assets/userscreen/userlist_5.png")
    userlist_6 = PhotoImage(file="assets/userscreen/userlist_6.png")