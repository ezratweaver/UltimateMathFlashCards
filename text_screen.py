from tkinter import Canvas
from assets import root, WINDOW_COLOR
import assets

class EnterTextGUI:

    def __init__(self) -> None:
        self.canvas = Canvas(
            root, bg=WINDOW_COLOR,
            height=500, width = 800,
            bd=0, highlightthickness=0,
            relief="ridge")
        