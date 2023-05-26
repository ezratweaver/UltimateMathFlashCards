from tkinter import Canvas
from assets import window, WINDOW_COLOR

class UserScreen:

    def __init__(self):
        self.userscreen_canv = Canvas(
            window, bg=WINDOW_COLOR,
            height=500, width = 800,
            bd=0, highlightthickness=0,
            relief="ridge")
        
        self.userscreen_canv.pack()





userscreeen = UserScreen()
window.geometry("800x500")
window.title("")
window.resizable(False, False)
window.mainloop()
