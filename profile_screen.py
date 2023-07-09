from tkinter import Canvas
from assets import root, WINDOW_COLOR
import assets

class ProfileGUI:

    def __init__(self) -> None:
        self.canvas = Canvas(
            root, bg=WINDOW_COLOR,
            height=500, width = 800,
            bd=0, highlightthickness=0,
            relief="ridge")

        self.canvas.create_image(
            400,
            200,
            image=assets.profilescreen["banner"]
        )

        self.canvas.create_image(
            120,
            430,
            image=assets.profilescreen["button_banner"]
        )

        self.canvas.create_image(
            300,
            430,
            image=assets.profilescreen["button_banner"]
        )
        
        self.canvas.create_image(
            480,
            430,
            image=assets.profilescreen["button_banner"]
        )

        self.canvas.create_image(
            650,
            430,
            image=assets.profilescreen["button_banner"]
        )

    def show_canvas(self) -> None:
        self.canvas.pack()

    def hide_canvas(self) -> None:
        self.canvas.pack_forget()


if __name__ == "__main__":
    p = ProfileGUI()
    p.show_canvas()
    root.mainloop()