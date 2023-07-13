from tkinter import Canvas
from assets import root, WINDOW_COLOR
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

        self.button_bgs["delete_button"] = self.canvas.create_image(
            485,
            430,
            image=assets.buttons["profile_action_button"]
        )

        self.button_bgs["edit_button"] = self.canvas.create_image(
            655,
            430,
            image=assets.buttons["profile_action_button"]
        )

    def show_canvas(self) -> None:
        self.canvas.pack()

    def hide_canvas(self) -> None:
        self.canvas.pack_forget()


if __name__ == "__main__":
    p = ProfileGUI()
    p.show_canvas()
    root.mainloop()