from tkinter import Canvas, Button, Entry
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
        
        def validate_input(current_input):
            if current_input == "":
                return True
            return len(current_input) <= 10

        validate_cmd = root.register(validate_input)

        def enter_pressed(event):
            print("hi   ")

        text_entry = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Encode Sans", 20),
            justify="center",
            validate="key",
            validatecommand=(validate_cmd, "%P"),
        )
        text_entry.place(x=313.0, y=251.0, width=176.0, height=44.0)
        text_entry.bind("<Return>", enter_pressed)
        text_entry.focus_set()


    def show_canvas(self) -> None:
        self.canvas.pack()

    def hide_canvas(self) -> None:
        self.canvas.pack_forget()



if __name__ == "__main__":
    text = EnterTextGUI()
    text.show_canvas()
    root.mainloop()