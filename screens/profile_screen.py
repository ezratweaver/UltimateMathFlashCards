import sys
from tkinter import Canvas, Button

sys.path.append("../assets")
from assets import root, WINDOW_COLOR, bind_hover_animation
import assets


class ProfileGUI:

    def __init__(self) -> None:
        self.button_bgs = {}
        self.buttons = {}
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
            145,
            430,
            image=assets.profilescreen["button_banner"]
        )

        self.canvas.create_image(
            315,
            430,
            image=assets.profilescreen["button_banner"]
        )
        
        self.canvas.create_image(
            485,
            430,
            image=assets.profilescreen["button_banner"]
        )

        self.canvas.create_image(
            655,
            430,
            image=assets.profilescreen["button_banner"]
        )

        self.button_bgs["back_button"] = self.canvas.create_image(
            145,
            430,
            image=assets.buttons["profile_action_button"]
        )

        self.button_bgs["history_button"] = self.canvas.create_image(
            315,
            430,
            image=assets.buttons["profile_action_button"]
        )

        self.button_bgs["remove_button"] = self.canvas.create_image(
            485,
            430,
            image=assets.buttons["profile_action_button"]
        )

        self.button_bgs["rename_button"] = self.canvas.create_image(
            655,
            430,
            image=assets.buttons["profile_action_button"]
        )

        self.buttons["back_button"] = Button(
            self.canvas, 
            fg="#000000",
            bg="#D9D9D9",
            activebackground="#D9D9D9",
            command=self.back_button_pressed,
            image=assets.profilescreen["back"],
            anchor="center",
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.buttons["back_button"].place(x=113, y=416, width=64, height=29)

        self.buttons["history_button"] = Button(
            self.canvas, 
            fg="#000000",
            bg="#D9D9D9",
            activebackground="#D9D9D9",
            image=assets.profilescreen["history"],
            anchor="center",
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.buttons["history_button"].place(x=283, y=416, width=64, height=29)

        self.buttons["remove_button"] = Button(
            self.canvas, 
            fg="#000000",
            bg="#D9D9D9",
            activebackground="#D9D9D9",
            image=assets.profilescreen["remove"],
            anchor="center",
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.buttons["remove_button"].place(x=453, y=416, width=64, height=29)

        self.buttons["rename_button"] = Button(
            self.canvas, 
            fg="#000000",
            bg="#D9D9D9",
            activebackground="#D9D9D9",
            image=assets.profilescreen["rename"],
            anchor="center",
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.buttons["rename_button"].place(x=623, y=416, width=64, height=29)

        bind_hover_animation(self.canvas, self.button_bgs,
                             self.buttons, assets.buttons["profile_action_button"],
                             assets.buttons["profile_action_button_selected"])

    def back_button_pressed(self):
        pass

    def show_canvas(self) -> None:
        self.canvas.pack()

    def hide_canvas(self) -> None:
        self.canvas.pack_forget()


if __name__ == "__main__":
    p = ProfileGUI()
    p.show_canvas()
    root.mainloop()
