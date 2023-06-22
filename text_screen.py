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
        
        self.canvas.create_image(
            400,
            250,
            image=assets.textscreen_username_enter_banner
        )
        
    def show_canvas(self) -> None:
        self.canvas.pack()

    def hide_canvas(self) -> None:
        self.canvas.pack_forget()



if __name__ == "__main__":
    text = EnterTextGUI()
    text.show_canvas()
    root.mainloop()