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
    