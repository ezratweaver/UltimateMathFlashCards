from tkinter import Canvas, Button
from assets import root, WINDOW_COLOR
import assets

class EnterTextGUI:

    def __init__(self) -> None:
        self.button_bgs = {}
        self.buttons = {}

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
        self.button_bgs["cancel_button"] = self.canvas.create_image(
            275,
            273,
            image=assets.button_square
        )
        self.buttons["cancel_button"] = Button(
            self.canvas, 
            fg="#000000",
            bg="#D9D9D9",
            activebackground="#D9D9D9",
            image=assets.textscreen_cancel,
            anchor="center",
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.buttons["cancel_button"].place(x=250, y=252, width=51, height=43)

        self.button_bgs["confirm_button"] = self.canvas.create_image(
            525,
            273,
            image=assets.button_square
        )
        self.buttons["confirm_button"] = Button(
            self.canvas,
            fg="#000000",
            bg="#D9D9D9",
            activebackground="#D9D9D9",
            image=assets.textscreen_confirm,
            anchor="center",
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.buttons["confirm_button"].place(x=500, y=252, width=51, height=43)

        for key, button in self.buttons.items():
            button.bind("<Enter>", lambda event, x=key:
                assets.image_modify(event, self.canvas,
                self.button_bgs[x], assets.button_square_selected))
            button.bind("<Leave>", lambda event, x=key:
                assets.image_modify(event, self.canvas,
                self.button_bgs[x], assets.button_square))


    def show_canvas(self) -> None:
        self.canvas.pack()

    def hide_canvas(self) -> None:
        self.canvas.pack_forget()



if __name__ == "__main__":
    text = EnterTextGUI()
    text.show_canvas()
    root.mainloop()