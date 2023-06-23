from tkinter import Canvas, Button
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
            398,
            250,
            image=assets.textscreen_username_enter_banner
        )
        self.canvas.create_image(
            400,
            220,
            image=assets.textscreen_please_enter_name
        )
        self.canvas.create_image(
            400,
            273,
            image=assets.textscreen_enterbox
        )
        cancel_button_bg = self.canvas.create_image(
            275,
            273,
            image=assets.button_square
        )
        confirm_button_bg = self.canvas.create_image(
            525,
            273,
            image=assets.button_square
        )
        cancel_button = Button(
            self.canvas, 
            fg="#000000",
            # bg="#D9D9D9",
            activebackground="#D9D9D9",
            image=assets.textscreen_cancel,
            anchor="center",
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        cancel_button.place(x=253, y=254, width=45, height=40)
        confirm_button = Button(
            self.canvas, 
            fg="#000000",
            # bg="#D9D9D9",
            activebackground="#D9D9D9",
            image=assets.textscreen_confirm,
            anchor="center",
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        confirm_button.place(x=516, y=265, width=20, height=20)


    def show_canvas(self) -> None:
        self.canvas.pack()

    def hide_canvas(self) -> None:
        self.canvas.pack_forget()



if __name__ == "__main__":
    text = EnterTextGUI()
    text.show_canvas()
    root.mainloop()