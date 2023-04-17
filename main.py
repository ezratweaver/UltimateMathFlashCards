from pathlib import Path
from json import loads, dumps
from cryptography.fernet import Fernet
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, ttk
from os import chdir, path, listdir, system
from random import randint
from operator import add, sub, floordiv, mul
from datetime import datetime
from sys import argv
from sound import Sound

system("cls")

exe_dir = path.dirname(argv[0])
chdir(exe_dir)


OUTPUT_PATH = exe_dir
ASSETS_PATH = OUTPUT_PATH / Path("assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


WINDOW_COLOR = "#3556FB"
window = Tk()


startscreen_canvas = Canvas(
    window,
    bg=WINDOW_COLOR,
    height=500,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
mainscreen_canvas = Canvas(
    window,
    bg=WINDOW_COLOR,
    height=500,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
optionsscreen_canvas = Canvas(
    window,
    bg=WINDOW_COLOR,
    height=500,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
finalscreen_canvas = Canvas(
    window,
    bg=WINDOW_COLOR,
    height=500,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
historyscreen_canvas = Canvas(
    window,
    bg=WINDOW_COLOR,
    height=500,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
userscreen_canvas = Canvas(
    window,
    bg=WINDOW_COLOR,
    height=500,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
profilescreen_canvas = Canvas(
    window,
    bg=WINDOW_COLOR,
    height=500,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)


class UserScreen:
    image_bg_image = PhotoImage(file=relative_to_assets("bg_image.png"))
    image_mainbanner = PhotoImage(file=relative_to_assets("userscreen/mainbanner.png"))
    image_usertitle_bg = PhotoImage(
        file=relative_to_assets("userscreen/usertitle_bg.png")
    )
    image_usertitle_bg_selected = PhotoImage(
        file=relative_to_assets("userscreen/usertitle_bg_selected.png")
    )
    image_usericon_bg = PhotoImage(
        file=relative_to_assets("userscreen/usericon_bg.png")
    )
    image_usericon_bg_selected = PhotoImage(
        file=relative_to_assets("userscreen/usericon_bg_selected.png")
    )
    image_actionbutton_banner = PhotoImage(
        file=relative_to_assets("userscreen/actionbutton_banner.png")
    )
    image_actionbutton_bg = PhotoImage(
        file=relative_to_assets("userscreen/actionbutton_bg.png")
    )
    image_actionbutton_bg_selected = PhotoImage(
        file=relative_to_assets("userscreen/actionbutton_bg_selected.png")
    )
    image_usericon = PhotoImage(file=relative_to_assets("userscreen/usericon.png"))
    image_useradd = PhotoImage(file=relative_to_assets("userscreen/useradd.png"))
    image_backbutton = PhotoImage(file=relative_to_assets("userscreen/backbutton.png"))
    image_userremove = PhotoImage(file=relative_to_assets("userscreen/userremove.png"))
    image_popup_banner = PhotoImage(
        file=relative_to_assets("userscreen/popup_banner.png")
    )
    image_popup_text = PhotoImage(file=relative_to_assets("userscreen/popup_text.png"))
    image_ok_bg = PhotoImage(file=relative_to_assets("userscreen/ok_bg.png"))
    image_ok_bg_selected = PhotoImage(
        file=relative_to_assets("userscreen/ok_bg_selected.png")
    )
    image_ok = PhotoImage(file=relative_to_assets("userscreen/ok.png"))
    image_newuser_banner = PhotoImage(
        file=relative_to_assets("userscreen/newuser_banner.png")
    )
    image_newuser_text = PhotoImage(
        file=relative_to_assets("userscreen/newuser_text.png")
    )
    image_entry_bg = PhotoImage(file=relative_to_assets("userscreen/entry_bg.png"))
    image_verify_bg = PhotoImage(file=relative_to_assets("userscreen/verify_bg.png"))
    image_verify_bg_selected = PhotoImage(
        file=relative_to_assets("userscreen/verify_bg_selected.png")
    )
    image_cancel = PhotoImage(file=relative_to_assets("userscreen/cancel.png"))
    image_confirm = PhotoImage(file=relative_to_assets("userscreen/confirm.png"))
    image_delete_confirm_banner = PhotoImage(
        file=relative_to_assets("userscreen/delete_confirm_banner.png")
    )
    image_delete_confirm_bg = PhotoImage(
        file=relative_to_assets("userscreen/delete_confirm_bg.png")
    )
    image_delete_confirm_bg_selected = PhotoImage(
        file=relative_to_assets("userscreen/delete_confirm_bg_selected.png")
    )
    image_del_confirm_yes = PhotoImage(
        file=relative_to_assets("userscreen/del_confirm_yes.png")
    )
    image_del_confirm_no = PhotoImage(
        file=relative_to_assets("userscreen/del_confirm_no.png")
    )

    bg_image = userscreen_canvas.create_image(395.0, 255.0, image=image_bg_image)
    mainbanner = userscreen_canvas.create_image(400.0, 219.0, image=image_mainbanner)
    usertitle0_bg = userscreen_canvas.create_image(
        436.0, 99.0, image=image_usertitle_bg
    )
    usertitle1_bg = userscreen_canvas.create_image(
        436.0, 178.0, image=image_usertitle_bg
    )
    usertitle2_bg = userscreen_canvas.create_image(
        436.0, 257.0, image=image_usertitle_bg
    )
    usertitle3_bg = userscreen_canvas.create_image(
        436.0, 336.0, image=image_usertitle_bg
    )
    usericon0_bg = userscreen_canvas.create_image(299.0, 99.0, image=image_usericon_bg)
    usericon1_bg = userscreen_canvas.create_image(299.0, 178.0, image=image_usericon_bg)
    usericon2_bg = userscreen_canvas.create_image(299.0, 257.0, image=image_usericon_bg)
    usericon3_bg = userscreen_canvas.create_image(299.0, 336.0, image=image_usericon_bg)
    backbutton_banner = userscreen_canvas.create_image(
        248.0, 453.0, image=image_actionbutton_banner
    )
    backbutton_bg = userscreen_canvas.create_image(
        248.0, 452.0, image=image_actionbutton_bg
    )
    userremove_banner = userscreen_canvas.create_image(
        551.0, 453.0, image=image_actionbutton_banner
    )
    userremove_bg = userscreen_canvas.create_image(
        552.0, 452.0, image=image_actionbutton_bg
    )

    button_usertitle0 = Button(
        userscreen_canvas,
        text="",
        fg="#000000",
        bg="#D9D9D9",
        anchor="w",
        font=("Encode Sans", 27 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: UserScreen.log_into_user(0),
        relief="flat",
    )
    button_usertitle0.place(x=352.0, y=76.5, width=170.0, height=47.0)
    button_usertitle0.config(activebackground="#C3C3C3")

    def user0_button_onenter(event):
        event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(
            UserScreen.usertitle0_bg, image=UserScreen.image_usertitle_bg_selected
        )

    def user0_button_onleave(event):
        event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(
            UserScreen.usertitle0_bg, image=UserScreen.image_usertitle_bg
        )

    button_usertitle0.bind("<Enter>", user0_button_onenter)
    button_usertitle0.bind("<Leave>", user0_button_onleave)

    button_usertitle1 = Button(
        userscreen_canvas,
        text="",
        fg="#000000",
        bg="#D9D9D9",
        anchor="w",
        font=("Encode Sans", 27 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: UserScreen.log_into_user(1),
        relief="flat",
    )
    button_usertitle1.place(x=352.0, y=155.5, width=170.0, height=47.0)
    button_usertitle1.config(activebackground="#C3C3C3")

    def user1_button_onenter(event):
        event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(
            UserScreen.usertitle1_bg, image=UserScreen.image_usertitle_bg_selected
        )

    def user1_button_onleave(event):
        event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(
            UserScreen.usertitle1_bg, image=UserScreen.image_usertitle_bg
        )

    button_usertitle1.bind("<Enter>", user1_button_onenter)
    button_usertitle1.bind("<Leave>", user1_button_onleave)

    button_usertitle2 = Button(
        userscreen_canvas,
        text="",
        fg="#000000",
        bg="#D9D9D9",
        anchor="w",
        font=("Encode Sans", 27 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: UserScreen.log_into_user(2),
        relief="flat",
    )
    button_usertitle2.place(x=352.0, y=233.5, width=170.0, height=47.0)
    button_usertitle2.config(activebackground="#C3C3C3")

    def user2_button_onenter(event):
        event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(
            UserScreen.usertitle2_bg, image=UserScreen.image_usertitle_bg_selected
        )

    def user2_button_onleave(event):
        event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(
            UserScreen.usertitle2_bg, image=UserScreen.image_usertitle_bg
        )

    button_usertitle2.bind("<Enter>", user2_button_onenter)
    button_usertitle2.bind("<Leave>", user2_button_onleave)

    button_usertitle3 = Button(
        userscreen_canvas,
        text="",
        fg="#000000",
        bg="#D9D9D9",
        anchor="w",
        font=("Encode Sans", 27 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: UserScreen.log_into_user(3),
        relief="flat",
    )
    button_usertitle3.place(x=352.0, y=312.5, width=170.0, height=47.0)
    button_usertitle3.config(activebackground="#C3C3C3")

    def user3_button_onenter(event):
        event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(
            UserScreen.usertitle3_bg, image=UserScreen.image_usertitle_bg_selected
        )

    def user3_button_onleave(event):
        event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(
            UserScreen.usertitle3_bg, image=UserScreen.image_usertitle_bg
        )

    button_usertitle3.bind("<Enter>", user3_button_onenter)
    button_usertitle3.bind("<Leave>", user3_button_onleave)

    def log_into_user(userlevel):
        Sound.sound_buttonpress.play()
        Data.userlevel = userlevel
        Data.highscore_dict = Data.user_data[userlevel]["highscore"]
        OptionsScreen.reset_settings()
        userscreen_canvas.pack_forget()
        startscreen_canvas.pack()

    temp = None

    def create_user(userlevel):
        Sound.sound_buttonpress.play()
        UserScreen.temp = userlevel
        UserScreen.hide_buttons(1000, 1000)
        newuser_banner = userscreen_canvas.create_image(
            400.0, 217.0, image=UserScreen.image_newuser_banner
        )
        newuser_text = userscreen_canvas.create_image(
            401.0, 188.0, image=UserScreen.image_newuser_text
        )
        entry_bg = userscreen_canvas.create_image(
            399.0, 239.0, image=UserScreen.image_entry_bg
        )
        cancel_bg = userscreen_canvas.create_image(
            274.0, 239.0, image=UserScreen.image_verify_bg
        )
        confirm_bg = userscreen_canvas.create_image(
            524.0, 239.0, image=UserScreen.image_verify_bg
        )

        def validate_input(current_input):
            if current_input == "":
                return True
            current_input
            return len(current_input) <= 10

        validate_cmd = window.register(validate_input)

        def enter_pressed(event):
            newuser_username = username_entry.get()
            exit_create_user()
            Data.add_user(newuser_username, UserScreen.temp)

        username_entry = Entry(
            userscreen_canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Encode Sans", 20),
            justify="center",
            validate="key",
            validatecommand=(validate_cmd, "%P"),
        )
        username_entry.place(x=313.0, y=218.0, width=173.0, height=41.0)
        username_entry.bind("<Return>", enter_pressed)
        username_entry.focus_set()

        button_cancel = Button(
            userscreen_canvas,
            image=UserScreen.image_cancel,
            borderwidth=0,
            bg="#D9D9D9",
            highlightthickness=0,
            command=lambda: exit_create_user(),
            relief="flat",
        )
        button_cancel.place(x=252.0, y=220.0, width=45, height=39)
        button_cancel.config(activebackground="#C3C3C3")

        def button_cancel_onenter(event):
            event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(
                cancel_bg, image=UserScreen.image_verify_bg_selected
            )

        def button_cancel_onleave(event):
            event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(
                cancel_bg, image=UserScreen.image_verify_bg
            )

        button_cancel.bind("<Enter>", button_cancel_onenter)
        button_cancel.bind("<Leave>", button_cancel_onleave)

        button_confirm = Button(
            userscreen_canvas,
            image=UserScreen.image_confirm,
            borderwidth=0,
            bg="#D9D9D9",
            highlightthickness=0,
            command=lambda: enter_pressed(None),
            relief="flat",
        )
        button_confirm.place(x=502.0, y=220.0, width=45, height=39)
        button_confirm.config(activebackground="#C3C3C3")

        def button_confirm_onenter(event):
            event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(
                confirm_bg, image=UserScreen.image_verify_bg_selected
            )

        def button_confirm_onleave(event):
            event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(
                confirm_bg, image=UserScreen.image_verify_bg
            )

        button_confirm.bind("<Enter>", button_confirm_onenter)
        button_confirm.bind("<Leave>", button_confirm_onleave)

        def exit_create_user():
            Sound.sound_buttonpress.play()
            UserScreen.hide_buttons(-1000, -1000)
            userscreen_canvas.delete(newuser_banner)
            userscreen_canvas.delete(newuser_text)
            userscreen_canvas.delete(entry_bg)
            userscreen_canvas.delete(cancel_bg)
            userscreen_canvas.delete(confirm_bg)
            button_cancel.destroy()
            button_confirm.destroy()
            username_entry.destroy()

    def show_user_profile(i):
        Sound.sound_buttonpress.play()
        ProfileScreen.personalize_screen(i)
        userscreen_canvas.pack_forget()
        profilescreen_canvas.pack()

    button_useraction0 = Button(
        userscreen_canvas,
        image=image_useradd,
        bg="#D9D9D9",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: UserScreen.create_user(0),
        relief="flat",
    )
    button_useraction0.place(x=271.0, y=75.0, width=56.0, height=50.0)
    button_useraction0.config(activebackground="#C3C3C3")

    def useraction0_onenter(event):
        event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(
            UserScreen.usericon0_bg, image=UserScreen.image_usericon_bg_selected
        )

    def useraction0_onleave(event):
        event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(
            UserScreen.usericon0_bg, image=UserScreen.image_usericon_bg
        )

    button_useraction0.bind("<Enter>", useraction0_onenter)
    button_useraction0.bind("<Leave>", useraction0_onleave)

    button_useraction1 = Button(
        userscreen_canvas,
        image=image_useradd,
        bg="#D9D9D9",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: UserScreen.create_user(1),
        relief="flat",
    )
    button_useraction1.place(x=271.0, y=154.0, width=56.0, height=50.0)
    button_useraction1.config(activebackground="#C3C3C3")

    def useraction1_onenter(event):
        event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(
            UserScreen.usericon1_bg, image=UserScreen.image_usericon_bg_selected
        )

    def useraction1_onleave(event):
        event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(
            UserScreen.usericon1_bg, image=UserScreen.image_usericon_bg
        )

    button_useraction1.bind("<Enter>", useraction1_onenter)
    button_useraction1.bind("<Leave>", useraction1_onleave)

    button_useraction2 = Button(
        userscreen_canvas,
        image=image_useradd,
        bg="#D9D9D9",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: UserScreen.create_user(2),
        relief="flat",
    )
    button_useraction2.place(x=271.0, y=233.0, width=56.0, height=50.0)
    button_useraction2.config(activebackground="#C3C3C3")

    def useraction2_onenter(event):
        event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(
            UserScreen.usericon2_bg, image=UserScreen.image_usericon_bg_selected
        )

    def useraction2_onleave(event):
        event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(
            UserScreen.usericon2_bg, image=UserScreen.image_usericon_bg
        )

    button_useraction2.bind("<Enter>", useraction2_onenter)
    button_useraction2.bind("<Leave>", useraction2_onleave)

    button_useraction3 = Button(
        userscreen_canvas,
        image=image_useradd,
        bg="#D9D9D9",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: UserScreen.create_user(3),
        relief="flat",
    )
    button_useraction3.place(x=271.0, y=312.0, width=56.0, height=50.0)
    button_useraction3.config(activebackground="#C3C3C3")

    def useraction3_onenter(event):
        event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(
            UserScreen.usericon3_bg, image=UserScreen.image_usericon_bg_selected
        )

    def useraction3_onleave(event):
        event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(
            UserScreen.usericon3_bg, image=UserScreen.image_usericon_bg
        )

    button_useraction3.bind("<Enter>", useraction3_onenter)
    button_useraction3.bind("<Leave>", useraction3_onleave)

    def confirm_remove_user(i):
        Sound.sound_buttonpress.play()
        try:
            username = Data.user_data[i]["displayname"]
        except:
            return

        UserScreen.hide_buttons(1000, 1000)
        delete_confirm_banner = userscreen_canvas.create_image(
            400.0, 220.0, image=UserScreen.image_delete_confirm_banner
        )
        delete_text = userscreen_canvas.create_text(
            401.0,
            195.0,
            anchor="center",
            text=f"Delete {username}?",
            fill="#000000",
            font=("Encode Sans", 25 * -1),
        )
        delete_confirm_bg_yes = userscreen_canvas.create_image(
            461.0, 236.0, image=UserScreen.image_delete_confirm_bg
        )
        delete_confirm_bg_no = userscreen_canvas.create_image(
            341.0, 236.0, image=UserScreen.image_delete_confirm_bg
        )

        button_delete_yes = Button(
            userscreen_canvas,
            image=UserScreen.image_del_confirm_yes,
            borderwidth=0,
            bg="#D9D9D9",
            highlightthickness=0,
            command=lambda: confirm_delete_user(i),
            relief="flat",
        )
        button_delete_yes.place(x=422.0, y=221.0, width=80.0, height=32.0)
        button_delete_yes.config(activebackground="#C3C3C3")

        def button_delete_yes_onenter(event):
            event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(
                delete_confirm_bg_yes, image=UserScreen.image_delete_confirm_bg_selected
            )

        def button_delete_yes_onleave(event):
            event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(
                delete_confirm_bg_yes, image=UserScreen.image_delete_confirm_bg
            )

        button_delete_yes.bind("<Enter>", button_delete_yes_onenter)
        button_delete_yes.bind("<Leave>", button_delete_yes_onleave)

        button_delete_no = Button(
            userscreen_canvas,
            image=UserScreen.image_del_confirm_no,
            borderwidth=0,
            bg="#D9D9D9",
            highlightthickness=0,
            command=lambda: exit_delete_prompt(),
            relief="flat",
        )
        button_delete_no.place(x=301.0, y=221.0, width=80.0, height=32.0)
        button_delete_no.config(activebackground="#C3C3C3")

        def button_delete_no_onenter(event):
            event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(
                delete_confirm_bg_no, image=UserScreen.image_delete_confirm_bg_selected
            )

        def button_delete_no_onleave(event):
            event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(
                delete_confirm_bg_no, image=UserScreen.image_delete_confirm_bg
            )

        button_delete_no.bind("<Enter>", button_delete_no_onenter)
        button_delete_no.bind("<Leave>", button_delete_no_onleave)

        def confirm_delete_user(i):
            Sound.sound_buttonpress.play()
            exit_delete_prompt()
            Data.remove_user(i)

        def exit_delete_prompt():
            Sound.sound_buttonpress.play()
            UserScreen.remove_user_mode()
            userscreen_canvas.delete(delete_confirm_banner)
            userscreen_canvas.delete(delete_text)
            userscreen_canvas.delete(delete_confirm_bg_yes)
            userscreen_canvas.delete(delete_confirm_bg_no)
            button_delete_yes.destroy()
            button_delete_no.destroy()

            UserScreen.hide_buttons(-1000, -1000)

    def remove_user_mode():
        Sound.sound_buttonpress.play()
        UserScreen.remove_mode = not UserScreen.remove_mode
        if UserScreen.remove_mode:
            for i, element in enumerate(Data.useraction_buttons):
                element.config(
                    image=UserScreen.image_userremove,
                    command=lambda userlevel=i: UserScreen.confirm_remove_user(
                        userlevel
                    ),
                )
        else:
            for i, element in enumerate(Data.useraction_buttons):
                element.config(
                    image=UserScreen.image_useradd,
                    command=lambda userlevel=i: UserScreen.create_user(userlevel),
                )
            Data.check_for_users()

    def back_button_pressed():
        Sound.sound_buttonpress.play()
        if UserScreen.remove_mode:
            UserScreen.remove_user_mode()
        if Data.userlevel == None:
            UserScreen.login_error()
        else:
            userscreen_canvas.pack_forget()
            startscreen_canvas.pack()

    button_back = Button(
        userscreen_canvas,
        image=image_backbutton,
        bg="#D9D9D9",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: UserScreen.back_button_pressed(),
        relief="flat",
    )
    button_back.place(x=216.0, y=441.0, width=65.0, height=23.0)
    button_back.config(activebackground="#C3C3C3")

    def buttonback_onenter(event):
        event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(
            UserScreen.backbutton_bg, image=UserScreen.image_actionbutton_bg_selected
        )

    def buttonback_onleave(event):
        event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(
            UserScreen.backbutton_bg, image=UserScreen.image_actionbutton_bg
        )

    button_back.bind("<Enter>", buttonback_onenter)
    button_back.bind("<Leave>", buttonback_onleave)

    remove_mode = False
    button_userremove = Button(
        userscreen_canvas,
        image=image_userremove,
        bg="#D9D9D9",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: UserScreen.remove_user_mode(),
        relief="flat",
    )
    button_userremove.place(x=520.0, y=441.0, width=65.0, height=23.0)
    button_userremove.config(activebackground="#C3C3C3")

    def userremove_onenter(event):
        event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(
            UserScreen.userremove_bg, image=UserScreen.image_actionbutton_bg_selected
        )

    def userremove_onleave(event):
        event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(
            UserScreen.userremove_bg, image=UserScreen.image_actionbutton_bg
        )

    button_userremove.bind("<Enter>", userremove_onenter)
    button_userremove.bind("<Leave>", userremove_onleave)

    def login_error():
        UserScreen.hide_buttons(1000, 1000)
        popup_banner = userscreen_canvas.create_image(
            399.0, 210.0, image=UserScreen.image_popup_banner
        )
        popup_text = userscreen_canvas.create_image(
            399.0, 187.0, image=UserScreen.image_popup_text
        )
        ok_bg = userscreen_canvas.create_image(
            399.0, 228.0, image=UserScreen.image_ok_bg
        )

        button_ok = Button(
            userscreen_canvas,
            image=UserScreen.image_ok,
            bg="#D9D9D9",
            activebackground="#C3C3C3",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: hide_error(),
            relief="flat",
        )
        button_ok.place(x=358.0, y=213.0, width=82.5, height=31.0)

        def buttonback_onenter(event):
            event.widget.config(bg="#C3C3C3"), userscreen_canvas.itemconfigure(
                ok_bg, image=UserScreen.image_ok_bg_selected
            )

        def buttonback_onleave(event):
            event.widget.config(bg="#D9D9D9"), userscreen_canvas.itemconfigure(
                ok_bg, image=UserScreen.image_ok_bg
            )

        button_ok.bind("<Enter>", buttonback_onenter)
        button_ok.bind("<Leave>", buttonback_onleave)

        def hide_error():
            Sound.sound_buttonpress.play()
            userscreen_canvas.delete(popup_banner)
            userscreen_canvas.delete(popup_text)
            userscreen_canvas.delete(ok_bg)
            button_ok.destroy()

            UserScreen.hide_buttons(-1000, -1000)

    def hide_buttons(x, y):
        try:
            for titlebutton in Data.usertitle_buttons:
                titlebutton.place_configure(
                    x=titlebutton.winfo_x() + x, y=titlebutton.winfo_y() + y
                )
        except:
            pass
        for actionbutton in Data.useraction_buttons:
            actionbutton.place_configure(
                x=actionbutton.winfo_x() + x, y=actionbutton.winfo_y() + y
            )


class ProfileScreen:
    current_user = None
    image_profile_banner = PhotoImage(
        file=relative_to_assets("profilescreen/profile_banner.png")
    )
    image_username_bg = PhotoImage(
        file=relative_to_assets("profilescreen/username_bg.png")
    )
    image_stats = PhotoImage(file=relative_to_assets("profilescreen/stats.png"))
    image_action_banner = PhotoImage(
        file=relative_to_assets("profilescreen/action_banner.png")
    )
    image_action_bg = PhotoImage(file=relative_to_assets("profilescreen/action_bg.png"))
    image_action_bg_selected = PhotoImage(
        file=relative_to_assets("profilescreen/action_bg_selected.png")
    )
    image_back = PhotoImage(file=relative_to_assets("profilescreen/back.png"))
    image_edit = PhotoImage(file=relative_to_assets("profilescreen/edit.png"))
    image_history = PhotoImage(file=relative_to_assets("profilescreen/history.png"))

    bg_image = profilescreen_canvas.create_image(
        395.0, 255.0, image=UserScreen.image_bg_image
    )
    profile_banner = profilescreen_canvas.create_image(
        398.0, 211.0, image=image_profile_banner
    )
    username_bg = profilescreen_canvas.create_image(
        403.0, 101.0, image=image_username_bg
    )
    stats = profilescreen_canvas.create_image(302.0, 221.0, image=image_stats)
    back_banner = profilescreen_canvas.create_image(
        197.0, 452.0, image=image_action_banner
    )
    history_banner = profilescreen_canvas.create_image(
        399.0, 452.0, image=image_action_banner
    )
    edit_banner = profilescreen_canvas.create_image(
        601.0, 452.0, image=image_action_banner
    )
    back_bg = profilescreen_canvas.create_image(197.0, 451.0, image=image_action_bg)
    history_bg = profilescreen_canvas.create_image(399.0, 451.0, image=image_action_bg)
    edit_bg = profilescreen_canvas.create_image(601.0, 451.0, image=image_action_bg)

    def personalize_screen(userlevel):
        ProfileScreen.current_user = userlevel
        username = Data.user_data[userlevel]["displayname"]
        gamesplayed = len(Data.user_data[userlevel]["gamehistory"])
        grade_to_percentage = {
            "A+": 97,
            "A": 93,
            "A-": 90,
            "B+": 87,
            "B": 83,
            "B-": 80,
            "C+": 77,
            "C": 73,
            "C-": 70,
            "D+": 67,
            "D": 63,
            "D-": 60,
            "F": 0,
        }
        highestscore = 0
        highestscoremode = "None"
        mostplayed = {"None": 0}
        total_percent = 0
        for game in Data.user_data[userlevel]["gamehistory"]:
            if game["correct"] > highestscore:
                highestscore = game["correct"]
                highestscoremode = game["mode"]
            if game["mode"] not in mostplayed:
                mostplayed[game["mode"]] = 1
            else:
                mostplayed[game["mode"]] += 1
            gamepercent = game["correct"] / (game["incorrect"] + game["correct"])
            total_percent = total_percent + gamepercent
        try:
            average_percent = total_percent / gamesplayed
        except:
            average_percent = 0

        for grade in sorted(grade_to_percentage.keys()):
            if round(average_percent * 100, 2) >= grade_to_percentage[grade]:
                grade = grade
                if gamesplayed == 0:
                    grade = "None"
                break

        profilescreen_canvas.itemconfig(ProfileScreen.grade_text, text=grade)
        profilescreen_canvas.itemconfig(
            ProfileScreen.favorite_mode, text=max(mostplayed, key=mostplayed.get)
        )
        profilescreen_canvas.itemconfig(
            ProfileScreen.average_percent, text=f"{round(average_percent * 100, 2)}%"
        )
        profilescreen_canvas.itemconfig(
            ProfileScreen.highest_score_mode, text=highestscoremode
        )
        profilescreen_canvas.itemconfig(ProfileScreen.highest_score, text=highestscore)
        profilescreen_canvas.itemconfig(ProfileScreen.games_played, text=gamesplayed)
        profilescreen_canvas.itemconfig(ProfileScreen.username_text, text=username)

    username_text = profilescreen_canvas.create_text(
        405.0,
        81.0,
        anchor="center",
        text="Ezra Weaver",
        fill="#000000",
        font=("Encode Sans", 28 * -1),
    )
    grade_text = profilescreen_canvas.create_text(
        291.0,
        117.0,
        anchor="nw",
        text="A+",
        fill="#000000",
        font=("Encode Sans", 17 * -1),
    )
    average_percent = profilescreen_canvas.create_text(
        326.0,
        154.0,
        anchor="nw",
        text="95",
        fill="#000000",
        font=("Encode Sans", 17 * -1),
    )
    highest_score = profilescreen_canvas.create_text(
        346.0,
        192.0,
        anchor="nw",
        text="63",
        fill="#000000",
        font=("Encode Sans", 17 * -1),
    )
    highest_score_mode = profilescreen_canvas.create_text(
        394.0,
        228.0,
        anchor="nw",
        text="*-easy-2:00",
        fill="#000000",
        font=("Encode Sans", 17 * -1),
    )
    favorite_mode = profilescreen_canvas.create_text(
        354.0,
        265.0,
        anchor="nw",
        text="*-easy-2:00",
        fill="#000000",
        font=("Encode Sans", 17 * -1),
    )
    games_played = profilescreen_canvas.create_text(
        354.0,
        302.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Encode Sans", 17 * -1),
    )

    def button_back_pressed():
        Sound.sound_buttonpress.play()
        profilescreen_canvas.pack_forget()
        userscreen_canvas.pack()

    button_back = Button(
        profilescreen_canvas,
        image=image_back,
        borderwidth=0,
        bg="#D9D9D9",
        highlightthickness=0,
        command=lambda: ProfileScreen.button_back_pressed(),
        relief="flat",
    )
    button_back.place(x=164.0, y=437.0, width=66.0, height=28.0)
    button_back.config(activebackground="#C3C3C3")

    def button_back_onenter(event):
        event.widget.config(bg="#C3C3C3"), profilescreen_canvas.itemconfigure(
            ProfileScreen.back_bg, image=ProfileScreen.image_action_bg_selected
        ),

    def button_back_onleave(event):
        event.widget.config(bg="#D9D9D9"), profilescreen_canvas.itemconfigure(
            ProfileScreen.back_bg, image=ProfileScreen.image_action_bg
        )

    button_back.bind("<Enter>", button_back_onenter)
    button_back.bind("<Leave>", button_back_onleave)

    def button_edit_pressed():
        Sound.sound_buttonpress.play()
        ProfileScreen.button_back.config(command=lambda: None)
        ProfileScreen.button_edit.config(command=lambda: None)
        ProfileScreen.button_history.config(command=lambda: None)
        newuser_banner = profilescreen_canvas.create_image(
            400.0, 217.0, image=UserScreen.image_newuser_banner
        )
        newuser_text = profilescreen_canvas.create_image(
            401.0, 188.0, image=UserScreen.image_newuser_text
        )
        entry_bg = profilescreen_canvas.create_image(
            399.0, 239.0, image=UserScreen.image_entry_bg
        )
        cancel_bg = profilescreen_canvas.create_image(
            274.0, 239.0, image=UserScreen.image_verify_bg
        )
        confirm_bg = profilescreen_canvas.create_image(
            524.0, 239.0, image=UserScreen.image_verify_bg
        )

        def validate_input(current_input):
            if current_input == "":
                return True
            current_input
            return len(current_input) <= 10

        validate_cmd = window.register(validate_input)

        def enter_pressed(event):
            new_username = username_entry.get()
            Data.rename_user(ProfileScreen.current_user, new_username)
            profilescreen_canvas.itemconfig(
                ProfileScreen.username_text, text=new_username
            )
            exit_rename()

        username_entry = Entry(
            profilescreen_canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Encode Sans", 20),
            justify="center",
            validate="key",
            validatecommand=(validate_cmd, "%P"),
        )
        username_entry.place(x=313.0, y=218.0, width=173.0, height=41.0)
        username_entry.bind("<Return>", enter_pressed)
        username_entry.focus_set()

        button_cancel = Button(
            profilescreen_canvas,
            image=UserScreen.image_cancel,
            borderwidth=0,
            bg="#D9D9D9",
            highlightthickness=0,
            command=lambda: exit_rename(),
            relief="flat",
        )
        button_cancel.place(x=252.0, y=220.0, width=45, height=39)
        button_cancel.config(activebackground="#C3C3C3")

        def button_cancel_onenter(event):
            event.widget.config(bg="#C3C3C3")
            profilescreen_canvas.itemconfigure(
                cancel_bg, image=UserScreen.image_verify_bg_selected
            )

        def button_cancel_onleave(event):
            event.widget.config(bg="#D9D9D9")
            profilescreen_canvas.itemconfigure(
                cancel_bg, image=UserScreen.image_verify_bg
            )

        button_cancel.bind("<Enter>", button_cancel_onenter)
        button_cancel.bind("<Leave>", button_cancel_onleave)

        button_confirm = Button(
            profilescreen_canvas,
            image=UserScreen.image_confirm,
            borderwidth=0,
            bg="#D9D9D9",
            highlightthickness=0,
            command=lambda: enter_pressed(None),
            relief="flat",
        )
        button_confirm.place(x=502.0, y=220.0, width=45, height=39)
        button_confirm.config(activebackground="#C3C3C3")

        def button_confirm_onenter(event):
            event.widget.config(bg="#C3C3C3"), profilescreen_canvas.itemconfigure(
                confirm_bg, image=UserScreen.image_verify_bg_selected
            )

        def button_confirm_onleave(event):
            event.widget.config(bg="#D9D9D9"), profilescreen_canvas.itemconfigure(
                confirm_bg, image=UserScreen.image_verify_bg
            )

        button_confirm.bind("<Enter>", button_confirm_onenter)
        button_confirm.bind("<Leave>", button_confirm_onleave)

        def exit_rename():
            Sound.sound_buttonpress.play()
            ProfileScreen.button_back.config(
                command=lambda: ProfileScreen.button_back_pressed()
            )
            ProfileScreen.button_edit.config(
                command=lambda: ProfileScreen.button_edit_pressed()
            )
            ProfileScreen.button_history.config(
                command=lambda: ProfileScreen.button_history_pressed()
            )
            profilescreen_canvas.delete(newuser_banner)
            profilescreen_canvas.delete(newuser_text)
            profilescreen_canvas.delete(entry_bg)
            profilescreen_canvas.delete(cancel_bg)
            profilescreen_canvas.delete(confirm_bg)
            button_cancel.destroy()
            button_confirm.destroy()
            username_entry.destroy()

    button_edit = Button(
        profilescreen_canvas,
        image=image_edit,
        borderwidth=0,
        bg="#D9D9D9",
        highlightthickness=0,
        command=lambda: ProfileScreen.button_edit_pressed(),
        relief="flat",
    )
    button_edit.place(x=568.0, y=437.0, width=66.0, height=28.0)
    button_edit.config(activebackground="#C3C3C3")

    def button_edit_onenter(event):
        event.widget.config(bg="#C3C3C3"), profilescreen_canvas.itemconfigure(
            ProfileScreen.edit_bg, image=ProfileScreen.image_action_bg_selected
        ),

    def button_edit_onleave(event):
        event.widget.config(bg="#D9D9D9"), profilescreen_canvas.itemconfigure(
            ProfileScreen.edit_bg, image=ProfileScreen.image_action_bg
        )

    button_edit.bind("<Enter>", button_edit_onenter)
    button_edit.bind("<Leave>", button_edit_onleave)

    def button_history_pressed():
        Sound.sound_buttonpress.play()
        HistoryScreen.display_data(ProfileScreen.current_user)
        HistoryScreen.back_button.config(
            command=lambda: ProfileScreen.changed_back_button_pressed()
        )

        historyscreen_canvas.coords(HistoryScreen.buttonbanner_2, 1000, 1000)
        historyscreen_canvas.coords(HistoryScreen.actionbuttonbg_2, 1000, 1000)
        HistoryScreen.info_button.place_configure(x=1000, y=1000)

        profilescreen_canvas.pack_forget()
        historyscreen_canvas.pack()

    def changed_back_button_pressed():
        Sound.sound_buttonpress.play()
        historyscreen_canvas.pack_forget()
        profilescreen_canvas.pack()

        historyscreen_canvas.coords(
            HistoryScreen.buttonbanner_2,
            710.0,
            453.0,
        )
        historyscreen_canvas.coords(HistoryScreen.actionbuttonbg_2, 710.0, 453.0)
        HistoryScreen.info_button.place_configure(x=663.0, y=438.0)

        HistoryScreen.back_button.config(
            command=lambda: HistoryScreen.back_button_pressed()
        )

    button_history = Button(
        profilescreen_canvas,
        image=image_history,
        borderwidth=0,
        bg="#D9D9D9",
        highlightthickness=0,
        command=lambda: ProfileScreen.button_history_pressed(),
        relief="flat",
    )
    button_history.place(x=366.0, y=437.0, width=66.0, height=28.0)
    button_history.config(activebackground="#C3C3C3")

    def button_history_onenter(event):
        event.widget.config(bg="#C3C3C3"), profilescreen_canvas.itemconfigure(
            ProfileScreen.history_bg, image=ProfileScreen.image_action_bg_selected
        ),

    def button_history_onleave(event):
        event.widget.config(bg="#D9D9D9"), profilescreen_canvas.itemconfigure(
            ProfileScreen.history_bg, image=ProfileScreen.image_action_bg
        )

    button_history.bind("<Enter>", button_history_onenter)
    button_history.bind("<Leave>", button_history_onleave)


class StartScreen:
    muted = False
    image_titlebanner = PhotoImage(
        file=relative_to_assets("startscreen/titlebanner.png")
    )
    image_title = PhotoImage(file=relative_to_assets("startscreen/title.png"))
    image_version = PhotoImage(file=relative_to_assets("startscreen/version.png"))
    image_buttonbanner = PhotoImage(
        file=relative_to_assets("startscreen/buttonbanner.png")
    )
    image_buttonbg = PhotoImage(file=relative_to_assets("startscreen/buttonbg.png"))
    image_buttonbg_selected = PhotoImage(
        file=relative_to_assets("startscreen/buttonbg_selected.png")
    )
    image_play = PhotoImage(file=relative_to_assets("startscreen/play.png"))
    image_leaderboard = PhotoImage(
        file=relative_to_assets("startscreen/leaderboard.png")
    )
    image_users = PhotoImage(file=relative_to_assets("startscreen/users.png"))
    image_unmuted = PhotoImage(file=relative_to_assets("startscreen/unmuted.png"))
    image_muted = PhotoImage(file=relative_to_assets("startscreen/volumemuted.png"))

    bg_image = startscreen_canvas.create_image(
        395.0, 255.0, image=UserScreen.image_bg_image
    )
    title_banner = startscreen_canvas.create_image(
        400.0, 106.0, image=image_titlebanner
    )
    title = startscreen_canvas.create_image(400.0, 100.0, image=image_title)
    version = startscreen_canvas.create_image(574.0, 141.0, image=image_version)

    play_buttonbanner = startscreen_canvas.create_image(
        400.0, 241.0, image=image_buttonbanner
    )
    play_buttonbg = startscreen_canvas.create_image(401.0, 240.0, image=image_buttonbg)

    volume_buttonbanner = startscreen_canvas.create_image(
        400.0, 389.0, image=image_buttonbanner
    )
    volume_buttonbg = startscreen_canvas.create_image(
        401.0, 388.0, image=image_buttonbg
    )

    users_buttonbanner = startscreen_canvas.create_image(
        474.0, 315.0, image=image_buttonbanner
    )
    users_buttonbg = startscreen_canvas.create_image(475.0, 314.0, image=image_buttonbg)

    leaderboard_buttonbanner = startscreen_canvas.create_image(
        329.0, 315.0, image=image_buttonbanner
    )
    leaderboard_buttonbg = startscreen_canvas.create_image(
        330.0, 314.0, image=image_buttonbg
    )

    def volume_button_pressed():
        if StartScreen.muted == False:
            StartScreen.button_volume.configure(image=StartScreen.image_muted)
            Sound.muted_all_sounds(0.0)
        else:
            StartScreen.button_volume.configure(image=StartScreen.image_unmuted)
            Sound.muted_all_sounds(1.0)
            Sound.sound_buttonpress.play()
        StartScreen.muted = not StartScreen.muted

    button_volume = Button(
        startscreen_canvas,
        image=image_unmuted,
        borderwidth=0,
        activebackground="#C3C3C3",
        bg="#D9D9D9",
        highlightthickness=0,
        command=lambda: StartScreen.volume_button_pressed(),
        relief="flat",
    )
    button_volume.place(x=366.0, y=373.0, width=70, height=32)

    def button_volume_onenter(event):
        event.widget.config(bg="#C3C3C3"), startscreen_canvas.itemconfigure(
            StartScreen.volume_buttonbg, image=StartScreen.image_buttonbg_selected
        )

    def button_volume_onleave(event):
        event.widget.config(bg="#D9D9D9"), startscreen_canvas.itemconfigure(
            StartScreen.volume_buttonbg, image=StartScreen.image_buttonbg
        )

    button_volume.bind("<Enter>", button_volume_onenter)
    button_volume.bind("<Leave>", button_volume_onleave)

    def user_button_pressed():
        Sound.sound_buttonpress.play()
        startscreen_canvas.pack_forget()
        userscreen_canvas.pack()

    button_users = Button(
        startscreen_canvas,
        image=image_users,
        borderwidth=0,
        activebackground="#C3C3C3",
        bg="#D9D9D9",
        highlightthickness=0,
        command=lambda: StartScreen.user_button_pressed(),
        relief="flat",
    )
    button_users.place(x=440.0, y=299.0, width=70, height=32)

    def button_users_onenter(event):
        event.widget.config(bg="#C3C3C3"), startscreen_canvas.itemconfigure(
            StartScreen.users_buttonbg, image=StartScreen.image_buttonbg_selected
        )

    def button_users_onleave(event):
        event.widget.config(bg="#D9D9D9"), startscreen_canvas.itemconfigure(
            StartScreen.users_buttonbg, image=StartScreen.image_buttonbg
        )

    button_users.bind("<Enter>", button_users_onenter)
    button_users.bind("<Leave>", button_users_onleave)

    def launch_button_pressed():
        Sound.sound_buttonpress.play()
        startscreen_canvas.pack_forget()
        mainscreen_canvas.pack()

    button_play = Button(
        startscreen_canvas,
        image=image_play,
        borderwidth=0,
        activebackground="#C3C3C3",
        bg="#D9D9D9",
        highlightthickness=0,
        command=lambda: StartScreen.launch_button_pressed(),
        relief="flat",
    )
    button_play.place(x=366.0, y=225.0, width=70, height=32)

    def button_play_onenter(event):
        event.widget.config(bg="#C3C3C3"), startscreen_canvas.itemconfigure(
            StartScreen.play_buttonbg, image=StartScreen.image_buttonbg_selected
        )

    def button_play_onleave(event):
        event.widget.config(bg="#D9D9D9"), startscreen_canvas.itemconfigure(
            StartScreen.play_buttonbg, image=StartScreen.image_buttonbg
        )

    button_play.bind("<Enter>", button_play_onenter)
    button_play.bind("<Leave>", button_play_onleave)

    button_leaderboard = Button(
        startscreen_canvas,
        image=image_leaderboard,
        borderwidth=0,
        activebackground="#C3C3C3",
        bg="#D9D9D9",
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat",
    )
    button_leaderboard.place(x=295.0, y=299.0, width=70, height=32)

    def button_leaderboard_onenter(event):
        event.widget.config(bg="#C3C3C3"), startscreen_canvas.itemconfigure(
            StartScreen.leaderboard_buttonbg, image=StartScreen.image_buttonbg_selected
        )

    def button_leaderboard_onleave(event):
        event.widget.config(bg="#D9D9D9"), startscreen_canvas.itemconfigure(
            StartScreen.leaderboard_buttonbg, image=StartScreen.image_buttonbg
        )

    button_leaderboard.bind("<Enter>", button_leaderboard_onenter)
    button_leaderboard.bind("<Leave>", button_leaderboard_onleave)


class Data:
    userlevel = None
    key = b"Kcq-tBBR5XbbOyH15njkMwKsO41l4J_diMGNerJQsKU="
    fernet_key = Fernet(key)
    highscore_dict = {"*-classical-twominute": 0}
    directory_path = "users"
    user_data = []
    usertitle_buttons = [
        UserScreen.button_usertitle0,
        UserScreen.button_usertitle1,
        UserScreen.button_usertitle2,
        UserScreen.button_usertitle3,
    ]
    useraction_buttons = [
        UserScreen.button_useraction0,
        UserScreen.button_useraction1,
        UserScreen.button_useraction2,
        UserScreen.button_useraction3,
    ]
    usertitle_button_positions = [76.5, 155.5, 233.5, 312.5]
    logged_in_users = []

    def check_for_users():
        Data.user_data = []
        user_name_and_level = {}
        for i, filename in enumerate(listdir(Data.directory_path)):
            if filename.endswith(".json"):
                file_path = path.join(Data.directory_path, filename)
                with open(file_path) as file:
                    decrypted_data = Data.fernet_key.decrypt(file.read())
                    data = loads(decrypted_data)
                    Data.user_data.append(data)
                    try:
                        user_name_and_level[
                            Data.user_data[i]["displayname"]
                        ] = Data.user_data[i]["userlevel"]
                    except:
                        pass
        for name, userlevel in user_name_and_level.items():
            try:
                Data.usertitle_buttons[userlevel].config(text=name)
            except:
                pass
            Data.useraction_buttons[userlevel].config(
                image=UserScreen.image_usericon,
                command=lambda userlevel=userlevel: UserScreen.show_user_profile(
                    userlevel
                ),
            )
        for i, element in enumerate(Data.usertitle_buttons):
            try:
                if element.cget("text") == "":
                    element.place(x=2000, y=2000)
                else:
                    Data.logged_in_users.append(i)
                    element.place_configure(
                        x=352.0,
                        y=Data.usertitle_button_positions[i],
                        width=170.0,
                        height=47.0,
                    )
            except:
                pass

    def clean_users():
        for element in Data.usertitle_buttons:
            element.config(text="")
        for i, element in enumerate(Data.useraction_buttons):
            element.config(
                image=UserScreen.image_useradd,
                command=lambda userlevel=i: UserScreen.create_user(userlevel),
            )

    def add_user(username, userlevel):
        newuser_dictionary = {
            "userlevel": userlevel,
            "displayname": username,
            "highscore": {"*-classical-twominute": 0},
            "gamehistory": [],
        }
        userfile = f"users/user{userlevel}.json"
        jsondump = dumps(newuser_dictionary)
        encrypted_jsondump = Data.fernet_key.encrypt(jsondump.encode())
        with open(userfile, "w") as file:
            file.write(encrypted_jsondump.decode())
        Data.check_for_users()

    def rename_user(userlevel, name):
        Data.user_data[userlevel]["displayname"] = name
        userfile = f"users/user{userlevel}.json"
        jsondump = dumps(Data.user_data[userlevel])
        encrypted_jsondump = Data.fernet_key.encrypt(jsondump.encode())
        with open(userfile, "w") as file:
            file.write(encrypted_jsondump.decode())
        Data.check_for_users()

    def remove_user(i):
        empty_dictionary = {}
        userfile = f"users/user{i}.json"
        jsondump = dumps(empty_dictionary)
        encrypted_jsondump = Data.fernet_key.encrypt(jsondump.encode())
        with open(userfile, "w") as file:
            file.write(encrypted_jsondump.decode())
        Data.userlevel = None
        Data.clean_users()
        Data.check_for_users()

    def dump_highscore():
        Data.user_data[Data.userlevel]["highscore"] = Data.highscore_dict
        usercount = -1
        for dictionary in Data.user_data:
            usercount += 1
            userfile = f"users/user{usercount}.json"
            jsondump = dumps(dictionary)
            encrypted_jsondump = Data.fernet_key.encrypt(jsondump.encode())
            with open(userfile, "w") as file:
                file.write(encrypted_jsondump.decode())

    def does_score_exist():
        if (
            Data.highscore_dict.get(
                f"{OptionsScreen.flashcardtype}-{OptionsScreen.flashcarddifficulty}-{OptionsScreen.flashcardtime}"
            )
            is None
        ):
            Data.highscore_dict[
                f"{OptionsScreen.flashcardtype}-{OptionsScreen.flashcarddifficulty}-{OptionsScreen.flashcardtime}"
            ] = "0"


class MainScreen:
    currentscore = 0
    high_score = 0
    flashcard1 = ""
    flashcard2 = ""
    last_flashcard1 = 20000000
    last_flashcard2 = 1
    correctanswer = ""
    feedback = ""
    final_feedback = ""
    incorrect = 0
    countdown_initialized = False
    game_started = False
    # mainScreen Images
    image_flashcard = PhotoImage(file=relative_to_assets("mainscreen/flashbg.png"))
    image_banner6 = PhotoImage(file=relative_to_assets("mainscreen/banner6.png"))
    image_banner7 = PhotoImage(file=relative_to_assets("mainscreen/banner7.png"))
    image_banner8 = PhotoImage(file=relative_to_assets("mainscreen/banner8.png"))
    image_line1 = PhotoImage(file=relative_to_assets("mainscreen/line1.png"))
    image_mathoperator_multiplication = PhotoImage(
        file=relative_to_assets("mainscreen/mathoperatorX.png")
    )
    image_mathoperator_minus = PhotoImage(
        file=relative_to_assets("mainscreen/mathoperator-.png")
    )
    image_mathoperator_plus = PhotoImage(
        file=relative_to_assets("mainscreen/mathoperator+.png")
    )
    image_mathoperator_divide = PhotoImage(
        file=relative_to_assets("mainscreen/mathoperatord.png")
    )
    image_entryboxbg = PhotoImage(file=relative_to_assets("mainscreen/entryboxbg.png"))
    image_timerbg = PhotoImage(file=relative_to_assets("mainscreen/timerbg.png"))
    image_scoreboxbg = PhotoImage(file=relative_to_assets("mainscreen/scoreboxbg.png"))
    image_line2 = PhotoImage(file=relative_to_assets("mainscreen/line2.png"))
    image_scorebg = PhotoImage(file=relative_to_assets("mainscreen/scorebg.png"))
    image_startbuttonbg = PhotoImage(
        file=relative_to_assets("mainscreen/startbuttonbg.png")
    )
    image_startbuttonbg_selected = PhotoImage(
        file=relative_to_assets("mainscreen/startbuttonbg_selected.png")
    )
    image_startbutton = PhotoImage(
        file=relative_to_assets("mainscreen/startbutton.png")
    )
    image_entrybox = PhotoImage(file=relative_to_assets("mainscreen/entrybox.png"))
    image_buttonbox = PhotoImage(file=relative_to_assets("mainscreen/buttonbox.png"))
    image_buttonboxbg = PhotoImage(
        file=relative_to_assets("mainscreen/buttonboxbg.png")
    )
    image_buttonboxbg_selected = PhotoImage(
        file=relative_to_assets("mainscreen/buttonboxbg_selected.png")
    )
    image_backbutton = PhotoImage(file=relative_to_assets("mainscreen/backbutton.png"))
    image_settingsbutton = PhotoImage(
        file=relative_to_assets("mainscreen/settingsbutton.png")
    )
    image_historybutton = PhotoImage(
        file=relative_to_assets("mainscreen/historybutton.png")
    )
    image_countdownbox = PhotoImage(
        file=relative_to_assets("mainscreen/countdownbox.png")
    )
    image_cancel_countdown_bg = PhotoImage(
        file=relative_to_assets("mainscreen/cancel_countdown_bg.png")
    )
    image_cancel_countdown_bg_selected = PhotoImage(
        file=relative_to_assets("mainscreen/cancel_countdown_bg_selected.png")
    )
    image_cancel_countdown_button = PhotoImage(
        file=relative_to_assets("mainscreen/cancel_countdown_button.png")
    )
    image_quit_banner = PhotoImage(
        file=relative_to_assets("mainscreen/quit_banner.png")
    )
    image_quit_buttonbg = PhotoImage(
        file=relative_to_assets("mainscreen/quit_buttonbg.png")
    )
    image_quit_buttonbg_selected = PhotoImage(
        file=relative_to_assets("mainscreen/quit_buttonbg_selected.png")
    )
    image_no_quit_button = PhotoImage(
        file=relative_to_assets("mainscreen/no_quit_button.png")
    )
    image_yes_quit_button = PhotoImage(
        file=relative_to_assets("mainscreen/yes_quit_button.png")
    )

    bg_image = mainscreen_canvas.create_image(
        395.0, 255.0, image=UserScreen.image_bg_image
    )
    flashcard = mainscreen_canvas.create_image(408.0, 218.0, image=image_flashcard)
    banner6 = mainscreen_canvas.create_image(640.0, 134.0, image=image_banner6)
    correctanswerbgbox = mainscreen_canvas.create_image(
        641.0, 221.0, image=image_banner7
    )
    startbuttonbgbox = mainscreen_canvas.create_image(641.0, 302.0, image=image_banner7)
    banner8 = mainscreen_canvas.create_image(410.0, 378.0, image=image_banner8)
    line1 = mainscreen_canvas.create_image(413.0, 262.0, image=image_line1)
    mathoperator = mainscreen_canvas.create_image(
        462.0, 236.0, image=image_mathoperator_multiplication
    )
    entryboxbg = mainscreen_canvas.create_image(386.0, 289.0, image=image_entryboxbg)
    timerbg = mainscreen_canvas.create_image(642.0, 135.0, image=image_timerbg)
    scoreboxbg = mainscreen_canvas.create_image(163.0, 187.0, image=image_scoreboxbg)
    line2_1 = mainscreen_canvas.create_image(161.0, 137.0, image=image_line2)
    line2_2 = mainscreen_canvas.create_image(161.0, 222.0, image=image_line2)
    scorebg_1 = mainscreen_canvas.create_image(161.0, 249.0, image=image_scorebg)
    scorebg_2 = mainscreen_canvas.create_image(161.0, 163.0, image=image_scorebg)
    startbuttonbg = mainscreen_canvas.create_image(
        641.0, 301.5, image=image_startbuttonbg
    )
    buttonbox_1 = mainscreen_canvas.create_image(161.0, 320.0, image=image_buttonbox)
    buttonbox_2 = mainscreen_canvas.create_image(161.0, 381.0, image=image_buttonbox)
    buttonbox_3 = mainscreen_canvas.create_image(64.0, 34.0, image=image_buttonbox)
    buttonboxbg_1 = mainscreen_canvas.create_image(64.0, 34.0, image=image_buttonboxbg)
    buttonboxbg_2 = mainscreen_canvas.create_image(
        161.0, 320.0, image=image_buttonboxbg
    )
    buttonboxbg_3 = mainscreen_canvas.create_image(
        161.0, 381.0, image=image_buttonboxbg
    )

    def back_button_pressed():
        Sound.sound_buttonpress.play()
        if MainScreen.game_started == True:
            MainScreen.confirm_quit()
        else:
            mainscreen_canvas.pack_forget()
            startscreen_canvas.pack()

    back_button = Button(
        mainscreen_canvas,
        image=image_backbutton,
        bg="#D9D9D9",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: MainScreen.back_button_pressed(),
        relief="flat",
    )
    back_button.place(x=34.0, y=23.5, width=59.0, height=22.0)
    back_button.config(activebackground="#C3C3C3")

    def backbutton_onenter(event):
        event.widget.config(bg="#C3C3C3"), mainscreen_canvas.itemconfigure(
            MainScreen.buttonboxbg_1, image=MainScreen.image_buttonboxbg_selected
        ),

    def backbutton_onleave(event):
        event.widget.config(bg="#D9D9D9"), mainscreen_canvas.itemconfigure(
            MainScreen.buttonboxbg_1, image=MainScreen.image_buttonboxbg
        )

    back_button.bind("<Enter>", backbutton_onenter)
    back_button.bind("<Leave>", backbutton_onleave)

    def settings_button_pressed():
        Sound.sound_buttonpress.play()
        optionsscreen_canvas.itemconfig(
            OptionsScreen.specific_highscore_text,
            text=Data.highscore_dict[
                f"{OptionsScreen.flashcardtype}-{OptionsScreen.flashcarddifficulty}-{OptionsScreen.flashcardtime}"
            ],
        )
        mainscreen_canvas.pack_forget()
        optionsscreen_canvas.pack()

    settings_button = Button(
        mainscreen_canvas,
        image=image_settingsbutton,
        bg="#D9D9D9",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: MainScreen.settings_button_pressed(),
        relief="flat",
    )
    settings_button.place(x=131, y=310, width=59.0, height=22.0)
    settings_button.config(activebackground="#C3C3C3")

    def settingsbutton_onenter(event):
        event.widget.config(bg="#C3C3C3"), mainscreen_canvas.itemconfigure(
            MainScreen.buttonboxbg_2, image=MainScreen.image_buttonboxbg_selected
        ),

    def settingsbutton_onleave(event):
        event.widget.config(bg="#D9D9D9"), mainscreen_canvas.itemconfigure(
            MainScreen.buttonboxbg_2, image=MainScreen.image_buttonboxbg
        )

    settings_button.bind("<Enter>", settingsbutton_onenter)
    settings_button.bind("<Leave>", settingsbutton_onleave)

    def history_button_pressed():
        Sound.sound_buttonpress.play()
        HistoryScreen.display_data(Data.userlevel)
        mainscreen_canvas.pack_forget()
        historyscreen_canvas.pack()

    history_button = Button(
        mainscreen_canvas,
        image=image_historybutton,
        bg="#D9D9D9",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: MainScreen.history_button_pressed(),
        relief="flat",
    )
    history_button.place(x=131.0, y=370.5, width=59.0, height=22.0)
    history_button.config(activebackground="#C3C3C3")

    def historybutton_onenter(event):
        event.widget.config(bg="#C3C3C3"), mainscreen_canvas.itemconfigure(
            MainScreen.buttonboxbg_3, image=MainScreen.image_buttonboxbg_selected
        ),

    def historybutton_onleave(event):
        event.widget.config(bg="#D9D9D9"), mainscreen_canvas.itemconfigure(
            MainScreen.buttonboxbg_3, image=MainScreen.image_buttonboxbg
        )

    history_button.bind("<Enter>", historybutton_onenter)
    history_button.bind("<Leave>", historybutton_onleave)

    def start_button_pressed():
        MainScreen.place_countdownscreen()
        Sound.sound_buttonpress.play()

    start_button = Button(
        mainscreen_canvas,
        image=image_startbutton,
        borderwidth=0,
        bg="#D9D9D9",
        highlightthickness=0,
        command=lambda: MainScreen.start_button_pressed(),
        relief="flat",
    )
    start_button.place(x=604.0, y=290.0, width=72.0, height=25.0)
    start_button.config(activebackground="#C3C3C3")

    def startbutton_onenter(event):
        event.widget.config(bg="#C3C3C3"), mainscreen_canvas.itemconfigure(
            MainScreen.startbuttonbg, image=MainScreen.image_startbuttonbg_selected
        ),

    def startbutton_onleave(event):
        event.widget.config(bg="#D9D9D9"), mainscreen_canvas.itemconfigure(
            MainScreen.startbuttonbg, image=MainScreen.image_startbuttonbg
        )

    start_button.bind("<Enter>", startbutton_onenter)
    start_button.bind("<Leave>", startbutton_onleave)

    flashcard2_text = mainscreen_canvas.create_text(
        359.0,
        184.0,
        anchor="nw",
        text=flashcard1,
        fill="#000000",
        font=("Helvetica", 70 * -1),
    )
    flashcard1_text = mainscreen_canvas.create_text(
        359.0,
        116.0,
        anchor="nw",
        text=flashcard2,
        fill="#000000",
        font=("Helvetica", 70 * -1),
    )
    time_text = mainscreen_canvas.create_text(
        591.0,
        113.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Encode Sans", 40 * -1),
    )
    feedback_text = mainscreen_canvas.create_text(
        359.0,
        360.0,
        anchor="nw",
        text=feedback,
        fill="#000000",
        font=("Encode Sans", 30 * -1),
    )
    highscore_text = mainscreen_canvas.create_text(
        160.0,
        250.0,
        anchor="center",
        text="",
        fill="#000000",
        font=("Encode Sans", 23 * -1),
    )
    currentscore_text = mainscreen_canvas.create_text(
        160,
        163.0,
        anchor="center",
        text="",
        fill="#000000",
        font=("Encode Sans", 23 * -1),
    )
    correctanswer_text = mainscreen_canvas.create_text(
        640.0,
        222.0,
        anchor="center",
        text="",
        fill="#000000",
        font=("Encode Sans", 38 * -1),
    )
    mainscreen_canvas.create_text(
        103.0,
        187.0,
        anchor="nw",
        text="High Score",
        fill="#000000",
        font=("Encode Sans", 25 * -1),
    )
    mainscreen_canvas.create_text(
        88.0,
        103.0,
        anchor="nw",
        text="Current Score",
        fill="#000000",
        font=("Encode Sans", 25 * -1),
    )

    def place_countdownscreen():
        countdownbox = mainscreen_canvas.create_image(
            407.0, 211.0, image=MainScreen.image_countdownbox
        )
        cancel_countdown_bg = mainscreen_canvas.create_image(
            297.0, 113.0, image=MainScreen.image_cancel_countdown_bg
        )

        countdown_title_text = mainscreen_canvas.create_text(
            352.0,
            109.0,
            anchor="nw",
            text="Starts in...",
            fill="#000000",
            font=("Encode Sans", 25 * -1),
        )
        countdown_counter_text = mainscreen_canvas.create_text(
            385.0,
            178.0,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Helvetica", 70 * -1),
        )

        cancel_countdown_button = Button(
            mainscreen_canvas,
            image=MainScreen.image_cancel_countdown_button,
            borderwidth=0,
            highlightthickness=0,
            bg="#D9D9D9",
            command=lambda: cancel_countdown(),
            relief="flat",
        )
        cancel_countdown_button.place(x=289.4, y=104.5, width=17.5, height=17.0)
        cancel_countdown_button.config(activebackground="#C3C3C3")

        def cancelcountdownbutton_onenter(event):
            event.widget.config(bg="#C3C3C3"), mainscreen_canvas.itemconfigure(
                cancel_countdown_bg, image=MainScreen.image_cancel_countdown_bg_selected
            ),

        def cancelcountdownbutton_onleave(event):
            event.widget.config(bg="#D9D9D9"), mainscreen_canvas.itemconfigure(
                cancel_countdown_bg, image=MainScreen.image_cancel_countdown_bg
            )

        cancel_countdown_button.bind("<Enter>", cancelcountdownbutton_onenter)
        cancel_countdown_button.bind("<Leave>", cancelcountdownbutton_onleave)
        MainScreen.pre_game_cleanup()
        MainScreen.back_button.place(
            x=34000000.0,
            y=23.5,
        )

        def destroy_countdownscreen():
            mainscreen_canvas.delete(countdownbox)
            mainscreen_canvas.delete(countdown_counter_text)
            mainscreen_canvas.delete(countdown_title_text)
            mainscreen_canvas.delete(cancel_countdown_bg)
            cancel_countdown_button.destroy()
            MainScreen.back_button.place(x=34.0, y=23.5)

        def initialize_countdown(seconds, callback):
            if seconds == 0:
                callback()
                MainScreen.start_game()
                return
            mainscreen_canvas.itemconfig(countdown_counter_text, text=seconds)
            seconds -= 1
            Sound.sound_countdown_tick.play()
            mainscreen_canvas.countdownloop = mainscreen_canvas.after(
                1000, initialize_countdown, seconds, callback
            )

        def cancel_countdown():
            Sound.sound_buttonpress.play()
            mainscreen_canvas.after_cancel(mainscreen_canvas.countdownloop)
            MainScreen.post_game_cleanup()
            destroy_countdownscreen()

        initialize_countdown(3, destroy_countdownscreen)

    def confirm_quit():
        quit_banner = mainscreen_canvas.create_image(
            408.0, 215.0, image=MainScreen.image_quit_banner
        )
        quit_buttonbg_1 = mainscreen_canvas.create_image(
            348.0, 230.0, image=MainScreen.image_quit_buttonbg
        )
        quit_buttonbg_2 = mainscreen_canvas.create_image(
            468.0, 230.0, image=MainScreen.image_quit_buttonbg
        )
        quit_text = mainscreen_canvas.create_text(
            294.0,
            176.0,
            anchor="nw",
            text="Do you want to quit?\n",
            fill="#000000",
            font=("Encode Sans", 25 * -1),
        )

        def yes_quit_button_pressed():
            Sound.sound_buttonpress.play()
            destroy_quitbox()
            MainScreen.game_started = False
            if OptionsScreen.flashcardtime == "practice":
                MainScreen.post_game_cleanup()
                return
            mainscreen_canvas.after_cancel(mainscreen_canvas.maintimerloop)
            MainScreen.post_game_cleanup()

        yes_quit_button = Button(
            image=MainScreen.image_yes_quit_button,
            borderwidth=0,
            highlightthickness=0,
            bg="#D9D9D9",
            command=lambda: yes_quit_button_pressed(),
            relief="flat",
        )
        yes_quit_button.place(x=429.0, y=217.0, width=80.0, height=26.0)
        yes_quit_button.config(activebackground="#C3C3C3")

        def yes_quitbutton_onenter(event):
            event.widget.config(bg="#C3C3C3"), mainscreen_canvas.itemconfigure(
                quit_buttonbg_2, image=MainScreen.image_quit_buttonbg_selected
            ),

        def yes_quitbutton_onleave(event):
            event.widget.config(bg="#D9D9D9"), mainscreen_canvas.itemconfigure(
                quit_buttonbg_2, image=MainScreen.image_quit_buttonbg
            )

        yes_quit_button.bind("<Enter>", yes_quitbutton_onenter)
        yes_quit_button.bind("<Leave>", yes_quitbutton_onleave)

        def no_quit_button_pressed():
            Sound.sound_buttonpress.play()
            destroy_quitbox()

        no_quit_button = Button(
            image=MainScreen.image_no_quit_button,
            borderwidth=0,
            highlightthickness=0,
            bg="#D9D9D9",
            command=lambda: no_quit_button_pressed(),
            relief="flat",
        )
        no_quit_button.place(x=308.0, y=217.0, width=80.0, height=26.0)
        no_quit_button.config(activebackground="#C3C3C3")

        def no_quitbutton_onenter(event):
            event.widget.config(bg="#C3C3C3"), mainscreen_canvas.itemconfigure(
                quit_buttonbg_1, image=MainScreen.image_quit_buttonbg_selected
            ),

        def no_quitbutton_onleave(event):
            event.widget.config(bg="#D9D9D9"), mainscreen_canvas.itemconfigure(
                quit_buttonbg_1, image=MainScreen.image_quit_buttonbg
            )

        no_quit_button.bind("<Enter>", no_quitbutton_onenter)
        no_quit_button.bind("<Leave>", no_quitbutton_onleave)

        def destroy_quitbox():
            mainscreen_canvas.delete(quit_banner)
            mainscreen_canvas.delete(quit_buttonbg_1)
            mainscreen_canvas.delete(quit_buttonbg_2)
            mainscreen_canvas.delete(quit_text)
            no_quit_button.destroy()
            yes_quit_button.destroy()

    def start_game():
        MainScreen.game_started = True
        mainscreen_canvas.itemconfig(
            MainScreen.currentscore_text, text=MainScreen.currentscore
        )
        MainScreen.entrybox.place(x=364.0, y=278.0, width=44.0, height=21.0)
        MainScreen.entrybox.focus_set()
        MainScreen.generate_problem()
        if OptionsScreen.flashcardtime == "practice":
            mainscreen_canvas.itemconfig(MainScreen.highscore_text, text="0")
            return
        mainscreen_canvas.itemconfig(
            MainScreen.highscore_text,
            text=Data.highscore_dict[
                f"{OptionsScreen.flashcardtype}-{OptionsScreen.flashcarddifficulty}-{OptionsScreen.flashcardtime}"
            ],
        )
        MainScreen.start_timer(OptionsScreen.minutes, OptionsScreen.seconds)

    def generate_problem():
        MainScreen.flashcard1 = randint(
            OptionsScreen.difficultyint1, OptionsScreen.difficultyint2
        )
        MainScreen.flashcard2 = randint(
            OptionsScreen.difficultyint1, OptionsScreen.difficultyint2
        )
        do_math = {"+": add, "-": sub, "/": floordiv, "*": mul}[
            OptionsScreen.flashcardtype
        ]
        MainScreen.correctanswer = do_math(MainScreen.flashcard1, MainScreen.flashcard2)
        MainScreen.check_problem()
        mainscreen_canvas.itemconfig(
            MainScreen.flashcard2_text, text=MainScreen.flashcard2
        )
        mainscreen_canvas.itemconfig(
            MainScreen.flashcard1_text, text=MainScreen.flashcard1
        )

    def check_problem():
        if MainScreen.correctanswer < 0:
            MainScreen.generate_problem()
        if (
            MainScreen.flashcard1 == MainScreen.last_flashcard1
            and MainScreen.flashcard2 == MainScreen.last_flashcard2
        ) or (
            MainScreen.flashcard1 == MainScreen.last_flashcard2
            and MainScreen.flashcard2 == MainScreen.last_flashcard1
        ):
            MainScreen.generate_problem()
        if (
            OptionsScreen.flashcardtype == "/"
            and not MainScreen.flashcard1 % MainScreen.flashcard2 == 0
        ):
            MainScreen.generate_problem()
        if MainScreen.flashcard2 > 10 and MainScreen.flashcard1 < 10:
            MainScreen.generate_problem()

    def problem_wrong():
        MainScreen.animation_shake_flashcard(0)
        MainScreen.animation_score_change(0, -6, -8)
        MainScreen.feedback = "Wrong!"
        MainScreen.incorrect = MainScreen.incorrect + 1
        Sound.sound_wrong.play()
        if MainScreen.currentscore > 0:
            MainScreen.currentscore = MainScreen.currentscore - 1

    def problem_correct():
        MainScreen.animation_score_change(0, -2, 2)
        MainScreen.feedback = "Correct!"
        MainScreen.currentscore = MainScreen.currentscore + 1
        Sound.sound_correct.play()

    def animation_shake_flashcard(animation_count):
        if animation_count % 2 == 0:
            move_amount = -5
        else:
            move_amount = 5
        animation_count += 1
        mainscreen_canvas.coords(MainScreen.flashcard, 408.0 + move_amount, 218.0)
        if animation_count < 4:
            mainscreen_canvas.after(
                50, MainScreen.animation_shake_flashcard, animation_count
            )
        if animation_count == 4:
            mainscreen_canvas.coords(MainScreen.flashcard, 408, 218.0)

    def animation_score_change(animation_count, stage_one_size, stage_two_size):
        if animation_count % 2 == 0:
            font_size = stage_one_size
        else:
            font_size = stage_two_size
        animation_count += 1
        mainscreen_canvas.itemconfigure(
            MainScreen.currentscore_text, font=("Encode Sans", 23 + font_size)
        )
        if animation_count < 3:
            mainscreen_canvas.after(
                60,
                MainScreen.animation_score_change,
                animation_count,
                stage_one_size,
                stage_two_size,
            )
        if animation_count == 3:
            mainscreen_canvas.itemconfigure(
                MainScreen.currentscore_text, font=("Encode Sans", 23 * -1)
            )

    def user_pressed_enter(event):
        user_answer = MainScreen.entrybox.get()
        try:
            if int(user_answer) == MainScreen.correctanswer:
                MainScreen.problem_correct()
            else:
                MainScreen.problem_wrong()
        except:
            return
        mainscreen_canvas.itemconfig(
            MainScreen.currentscore_text, text=MainScreen.currentscore
        )
        mainscreen_canvas.itemconfig(
            MainScreen.correctanswer_text, text=MainScreen.correctanswer
        )
        mainscreen_canvas.itemconfig(MainScreen.feedback_text, text=MainScreen.feedback)
        MainScreen.last_flashcard1 = MainScreen.flashcard1
        MainScreen.last_flashcard2 = MainScreen.flashcard2
        MainScreen.generate_problem()
        MainScreen.entrybox.delete(0, "end")

    def start_timer(minutes, seconds):
        if minutes == 00 and seconds == 1:
            MainScreen.end_game()
            return

        if seconds == 00:
            minutes -= 1
            seconds = 60

        seconds -= 1
        Sound.sound_timer_tick.play()
        mainscreen_canvas.itemconfig(
            MainScreen.time_text, text=f"{minutes:2}:{seconds:02}"
        )

        mainscreen_canvas.maintimerloop = mainscreen_canvas.after(
            1000, MainScreen.start_timer, minutes, seconds
        )

    def pre_game_cleanup():
        MainScreen.start_button.place(x=60400.0, y=290.0, width=72.0, height=25.0)
        MainScreen.history_button.place(x=13100.0, y=370.5, width=59.0, height=22.0)
        MainScreen.settings_button.place(x=13100, y=310, width=59.0, height=22.0)
        mainscreen_canvas.coords(
            MainScreen.buttonbox_1,
            16100.0,
            320.0,
        )
        mainscreen_canvas.coords(
            MainScreen.buttonbox_2,
            16100.0,
            320.0,
        )
        mainscreen_canvas.coords(MainScreen.buttonboxbg_3, 16100.0, 320.0)
        mainscreen_canvas.coords(MainScreen.buttonboxbg_2, 16100.0, 320.0)
        mainscreen_canvas.coords(MainScreen.startbuttonbg, 16100.0, 320.0)
        mainscreen_canvas.coords(MainScreen.startbuttonbgbox, 16100.0, 320.0)

    def post_game_cleanup():
        MainScreen.start_button.place(x=604.0, y=290.0, width=72.0, height=25.0)
        MainScreen.history_button.place(x=131.0, y=370.5, width=59.0, height=22.0)
        MainScreen.settings_button.place(x=131, y=310, width=59.0, height=22.0)
        mainscreen_canvas.coords(
            MainScreen.buttonbox_1,
            161.0,
            320.0,
        )
        mainscreen_canvas.coords(
            MainScreen.buttonbox_2,
            161.0,
            381.0,
        )
        mainscreen_canvas.coords(
            MainScreen.buttonboxbg_3,
            161.0,
            381.0,
        )
        mainscreen_canvas.coords(
            MainScreen.buttonboxbg_2,
            161.0,
            320.0,
        )
        mainscreen_canvas.itemconfig(MainScreen.time_text, text="")
        mainscreen_canvas.itemconfig(MainScreen.flashcard2_text, text="")
        mainscreen_canvas.itemconfig(MainScreen.flashcard1_text, text="")
        mainscreen_canvas.itemconfig(MainScreen.currentscore_text, text="")
        mainscreen_canvas.itemconfig(MainScreen.highscore_text, text="")
        mainscreen_canvas.itemconfig(MainScreen.correctanswer_text, text="")
        mainscreen_canvas.itemconfig(MainScreen.feedback_text, text="")
        mainscreen_canvas.coords(MainScreen.startbuttonbg, 641.0, 301.5)
        mainscreen_canvas.coords(MainScreen.startbuttonbgbox, 641.0, 302)
        MainScreen.entrybox.place(x=36400.0, y=278.0)
        MainScreen.currentscore = 0
        MainScreen.incorrect = 0
        MainScreen.game_started = False
        MainScreen.entrybox.delete(0, "end")

    def is_new_highscore():
        if int(MainScreen.currentscore) > int(
            Data.highscore_dict[
                f"{OptionsScreen.flashcardtype}-{OptionsScreen.flashcarddifficulty}-{OptionsScreen.flashcardtime}"
            ]
        ):
            FinalScreen.finalscore_feedback_text = "New Highscore!"
            Sound.sound_win.play()
            Data.highscore_dict[
                f"{OptionsScreen.flashcardtype}-{OptionsScreen.flashcarddifficulty}-{OptionsScreen.flashcardtime}"
            ] = MainScreen.currentscore
        else:
            FinalScreen.finalscore_feedback_text = "Better Luck Next TIme!"
            Sound.sound_times_up.play()

    def log_game():
        if MainScreen.currentscore == 0:
            return
        current_datetime = datetime.now()
        current_date = current_datetime.strftime("%m/%d/%Y")
        current_time = current_datetime.strftime("%I:%M %p")
        log_dictionary = {
            "date": current_date,
            "time": current_time,
            "correct": MainScreen.currentscore,
            "incorrect": MainScreen.incorrect,
            "mode": f"{OptionsScreen.flashcardtype}-{OptionsScreen.flashcarddifficulty}-{OptionsScreen.flashcardtime}",
        }
        Data.user_data[Data.userlevel]["gamehistory"].append(log_dictionary)

    def end_game():
        mainscreen_canvas.pack_forget()
        finalscreen_canvas.pack()
        finalscreen_canvas.itemconfig(
            FinalScreen.yourscore_text, text=MainScreen.currentscore
        )
        finalscreen_canvas.itemconfig(
            FinalScreen.highscore_text,
            text=Data.highscore_dict[
                f"{OptionsScreen.flashcardtype}-{OptionsScreen.flashcarddifficulty}-{OptionsScreen.flashcardtime}"
            ],
        )
        finalscreen_canvas.itemconfig(
            FinalScreen.incorrect_text, text=MainScreen.incorrect
        )
        MainScreen.is_new_highscore()
        finalscreen_canvas.itemconfig(
            FinalScreen.feedback_text, text=FinalScreen.finalscore_feedback_text
        )
        MainScreen.log_game()
        Data.dump_highscore()
        MainScreen.post_game_cleanup()

    def validate_main_input(current_input):
        if current_input == "":
            return True
        try:
            int(current_input)
            return len(current_input) <= 4
        except ValueError:
            return False

    mainscreen_validate_cmd = window.register(validate_main_input)

    # Entry Box
    entryboxbg = mainscreen_canvas.create_image(386.0, 289.5, image=image_entrybox)
    entrybox = Entry(
        mainscreen_canvas,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Encode Sans", 13),
        validate="key",
        validatecommand=(mainscreen_validate_cmd, "%P"),
    )

    entrybox.bind("<Return>", user_pressed_enter)


class OptionsScreen:
    flashcardtype = "*"
    flashcarddifficulty = "classical"
    flashcardtime = "twominute"
    difficultyint1 = 1
    difficultyint2 = 15
    explanationtitle = None
    explanation = None
    minutes = 2
    seconds = 1

    # optionsscreen Images
    image_banner9 = PhotoImage(file=relative_to_assets("optionsscreen/banner9.png"))
    image_banner10 = PhotoImage(file=relative_to_assets("optionsscreen/banner10.png"))
    image_descriptionbox = PhotoImage(
        file=relative_to_assets("optionsscreen/descriptionbox.png")
    )
    image_buttonbg_outline = PhotoImage(
        file=relative_to_assets("optionsscreen/buttonbg_outline.png")
    )
    image_buttonbg_outline_selected = PhotoImage(
        file=relative_to_assets("optionsscreen/buttonbg_outline_selected.png")
    )
    image_buttonbg = PhotoImage(file=relative_to_assets("optionsscreen/buttonbg.png"))
    image_buttonbg_selected = PhotoImage(
        file=relative_to_assets("optionsscreen/buttonbg_selected.png")
    )
    image_flashcardtype_title = PhotoImage(
        file=relative_to_assets("optionsscreen/flashcardtype_title.png")
    )
    image_difficulty_title = PhotoImage(
        file=relative_to_assets("optionsscreen/difficulty_title.png")
    )
    image_time_title = PhotoImage(
        file=relative_to_assets("optionsscreen/time_title.png")
    )
    image_back_buttonbg = PhotoImage(
        file=relative_to_assets("optionsscreen/back_buttonbg.png")
    )
    image_back_buttonbg_selected = PhotoImage(
        file=relative_to_assets("optionsscreen/back_buttonbg_selected.png")
    )
    image_addition_button = PhotoImage(
        file=relative_to_assets("optionsscreen/addition_button.png")
    )
    image_subtraction_button = PhotoImage(
        file=relative_to_assets("optionsscreen/subtraction_button.png")
    )
    image_multiplication_button = PhotoImage(
        file=relative_to_assets("optionsscreen/multiplication_button.png")
    )
    image_division_button = PhotoImage(
        file=relative_to_assets("optionsscreen/division_button.png")
    )
    image_medium_button = PhotoImage(
        file=relative_to_assets("optionsscreen/medium_button.png")
    )
    image_easy_button = PhotoImage(
        file=relative_to_assets("optionsscreen/easy_button.png")
    )
    image_practice_button = PhotoImage(
        file=relative_to_assets("optionsscreen/practice_button.png")
    )
    image_twominute_button = PhotoImage(
        file=relative_to_assets("optionsscreen/2minute_button.png")
    )
    image_oneminute_button = PhotoImage(
        file=relative_to_assets("optionsscreen/1minute_button.png")
    )
    image_thirtysecond_button = PhotoImage(
        file=relative_to_assets("optionsscreen/30second_button.png")
    )
    image_hard_button = PhotoImage(
        file=relative_to_assets("optionsscreen/hard_button.png")
    )
    image_classical_button = PhotoImage(
        file=relative_to_assets("optionsscreen/classical_button.png")
    )
    image_back_button = PhotoImage(
        file=relative_to_assets("optionsscreen/back_button.png")
    )
    image_highscore_banner = PhotoImage(
        file=relative_to_assets("optionsscreen/highscore_banner.png")
    )
    image_highscore_bg = PhotoImage(
        file=relative_to_assets("optionsscreen/highscore_bg.png")
    )
    # Place Elements
    bg_image = optionsscreen_canvas.create_image(
        395.0, 255.0, image=UserScreen.image_bg_image
    )
    banner9_1 = optionsscreen_canvas.create_image(132.0, 163.0, image=image_banner9)
    banner9_2 = optionsscreen_canvas.create_image(399.0, 166.0, image=image_banner9)
    banner9_3 = optionsscreen_canvas.create_image(666.0, 166.0, image=image_banner9)
    banner10 = optionsscreen_canvas.create_image(106.0, 455.0, image=image_banner10)
    descriptionbox = optionsscreen_canvas.create_image(
        391.0, 403.0, image=image_descriptionbox
    )
    back_buttonbg = optionsscreen_canvas.create_image(
        107.0, 454.0, image=image_back_buttonbg
    )

    buttonbg_difficulty_classical = optionsscreen_canvas.create_image(
        400.0, 102.0, image=image_buttonbg_outline
    )
    buttonbg_difficulty_easy = optionsscreen_canvas.create_image(
        400.0, 150.0, image=image_buttonbg
    )
    buttonbg_difficulty_medium = optionsscreen_canvas.create_image(
        400.0, 198.0, image=image_buttonbg
    )
    buttonbg_difficulty_hard = optionsscreen_canvas.create_image(
        400.0, 246.0, image=image_buttonbg
    )

    buttonbg_time_twominute = optionsscreen_canvas.create_image(
        667.0, 102.0, image=image_buttonbg_outline
    )
    buttonbg_time_oneminute = optionsscreen_canvas.create_image(
        667.0, 150.0, image=image_buttonbg
    )
    buttonbg_time_thirtysecond = optionsscreen_canvas.create_image(
        667.0, 198.0, image=image_buttonbg
    )
    buttonbg_time_practice = optionsscreen_canvas.create_image(
        667.0, 246.0, image=image_buttonbg
    )

    buttonbg_type_multiplication = optionsscreen_canvas.create_image(
        135.0, 102.0, image=image_buttonbg_outline
    )
    buttonbg_type_subtraction = optionsscreen_canvas.create_image(
        135.0, 150.0, image=image_buttonbg
    )
    buttonbg_type_addition = optionsscreen_canvas.create_image(
        135.0, 198.0, image=image_buttonbg
    )
    buttonbg_type_division = optionsscreen_canvas.create_image(
        135.0, 246.0, image=image_buttonbg
    )

    flashcardtype_title = optionsscreen_canvas.create_image(
        134.0, 63.0, image=image_flashcardtype_title
    )
    difficulty_title = optionsscreen_canvas.create_image(
        400.0, 63.0, image=image_difficulty_title
    )
    time_title = optionsscreen_canvas.create_image(666.0, 63.0, image=image_time_title)

    highscore_banner = optionsscreen_canvas.create_image(
        691.0, 413.0, image=image_highscore_banner
    )
    highscore_bg = optionsscreen_canvas.create_image(
        691.0, 428.0, image=image_highscore_bg
    )
    optionsscreen_canvas.create_text(
        647.0,
        379.0,
        anchor="nw",
        text="Highscore:",
        fill="#000000",
        font=("Encode Sans", 19 * -1),
    )
    specific_highscore_text = optionsscreen_canvas.create_text(
        691.0,
        428.0,
        anchor="center",
        text=Data.highscore_dict[
            f"{flashcardtype}-{flashcarddifficulty}-{flashcardtime}"
        ],
        fill="#000000",
        font=("Encode Sans", 19 * -1),
    )

    def reset_settings():
        OptionsScreen.flashcardtype = "*"
        OptionsScreen.flashcarddifficulty = "classical"
        OptionsScreen.flashcardtime = "twominute"
        OptionsScreen.difficultyint1 = 1
        OptionsScreen.difficultyint2 = 15
        OptionsScreen.explanationtitle = None
        OptionsScreen.explanation = None
        OptionsScreen.minutes = 2
        OptionsScreen.seconds = 1
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.specific_highscore_text,
            text=Data.highscore_dict[
                f"{OptionsScreen.flashcardtype}-{OptionsScreen.flashcarddifficulty}-{OptionsScreen.flashcardtime}"
            ],
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_type_multiplication,
            image=OptionsScreen.image_buttonbg_outline,
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_type_addition, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_type_subtraction, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_type_division, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_difficulty_classical,
            image=OptionsScreen.image_buttonbg_outline,
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_difficulty_hard, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_difficulty_medium, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_difficulty_easy, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_time_thirtysecond, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_time_oneminute, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_time_practice, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_time_twominute,
            image=OptionsScreen.image_buttonbg_outline,
        )

    def multiplication_button_pressed():
        OptionsScreen.flashcardtype = "*"
        (
            OptionsScreen.explanationtitle,
            OptionsScreen.explanation,
            OptionsScreen.difficultyint1,
            OptionsScreen.difficultyint2,
        ) = OptionsScreen.get_info(
            OptionsScreen.flashcardtype, OptionsScreen.flashcarddifficulty
        )
        OptionsScreen.explanationtitle = "Multiplication -"
        OptionsScreen.explanation = "Put your time tables to the test!"
        mainscreen_canvas.itemconfigure(
            MainScreen.mathoperator, image=MainScreen.image_mathoperator_multiplication
        )
        OptionsScreen.clear_type_outline()
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_type_multiplication,
            image=OptionsScreen.image_buttonbg_outline_selected,
        )

    multiplication_button = Button(
        optionsscreen_canvas,
        image=image_multiplication_button,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=lambda: OptionsScreen.multiplication_button_pressed(),
        relief="flat",
    )
    multiplication_button.place(x=110.0, y=90.5, width=50.0, height=22.0)
    multiplication_button.config(activebackground="#C3C3C3")

    def multiplicationbutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if OptionsScreen.flashcardtype == "*":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_type_multiplication,
                image=OptionsScreen.image_buttonbg_outline_selected,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_type_multiplication,
                image=OptionsScreen.image_buttonbg_selected,
            )

    def multiplicationbutton_onleave(event):
        event.widget.config(bg="#D9D9D9")
        if OptionsScreen.flashcardtype == "*":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_type_multiplication,
                image=OptionsScreen.image_buttonbg_outline,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_type_multiplication,
                image=OptionsScreen.image_buttonbg,
            )

    multiplication_button.bind("<Enter>", multiplicationbutton_onenter)
    multiplication_button.bind("<Leave>", multiplicationbutton_onleave)

    def subtraction_button_pressed():
        OptionsScreen.flashcardtype = "-"
        (
            OptionsScreen.explanationtitle,
            OptionsScreen.explanation,
            OptionsScreen.difficultyint1,
            OptionsScreen.difficultyint2,
        ) = OptionsScreen.get_info(
            OptionsScreen.flashcardtype, OptionsScreen.flashcarddifficulty
        )
        OptionsScreen.explanationtitle = "Subtraction -"
        OptionsScreen.explanation = "Put your subtraction skills to the test!"
        OptionsScreen.clear_type_outline()
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_type_subtraction,
            image=OptionsScreen.image_buttonbg_outline_selected,
        )
        mainscreen_canvas.itemconfigure(
            MainScreen.mathoperator, image=MainScreen.image_mathoperator_minus
        )

    subtraction_button = Button(
        optionsscreen_canvas,
        image=image_subtraction_button,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=lambda: OptionsScreen.subtraction_button_pressed(),
        relief="flat",
    )
    subtraction_button.place(x=110.0, y=139.0, width=50.0, height=22.0)
    subtraction_button.config(activebackground="#C3C3C3")

    def subtractionbutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if OptionsScreen.flashcardtype == "-":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_type_subtraction,
                image=OptionsScreen.image_buttonbg_outline_selected,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_type_subtraction,
                image=OptionsScreen.image_buttonbg_selected,
            )

    def subtractionbutton_onleave(event):
        event.widget.config(bg="#D9D9D9")
        if OptionsScreen.flashcardtype == "-":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_type_subtraction,
                image=OptionsScreen.image_buttonbg_outline,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_type_subtraction,
                image=OptionsScreen.image_buttonbg,
            )

    subtraction_button.bind("<Enter>", subtractionbutton_onenter)
    subtraction_button.bind("<Leave>", subtractionbutton_onleave)

    def addition_button_pressed():
        OptionsScreen.flashcardtype = "+"
        (
            OptionsScreen.explanationtitle,
            OptionsScreen.explanation,
            OptionsScreen.difficultyint1,
            OptionsScreen.difficultyint2,
        ) = OptionsScreen.get_info(
            OptionsScreen.flashcardtype, OptionsScreen.flashcarddifficulty
        )
        OptionsScreen.explanationtitle = "Addition -"
        OptionsScreen.explanation = "Put your addition skills to the test!"
        OptionsScreen.clear_type_outline()
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_type_addition,
            image=OptionsScreen.image_buttonbg_outline_selected,
        )
        mainscreen_canvas.itemconfigure(
            MainScreen.mathoperator, image=MainScreen.image_mathoperator_plus
        )

    addition_button = Button(
        optionsscreen_canvas,
        image=image_addition_button,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=lambda: OptionsScreen.addition_button_pressed(),
        relief="flat",
    )
    addition_button.place(x=110.0, y=187.0, width=50.0, height=22.0)
    addition_button.config(activebackground="#C3C3C3")

    def additionbutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if OptionsScreen.flashcardtype == "+":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_type_addition,
                image=OptionsScreen.image_buttonbg_outline_selected,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_type_addition,
                image=OptionsScreen.image_buttonbg_selected,
            )

    def additionbutton_onleave(event):
        event.widget.config(bg="#D9D9D9"),
        if OptionsScreen.flashcardtype == "+":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_type_addition,
                image=OptionsScreen.image_buttonbg_outline,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_type_addition, image=OptionsScreen.image_buttonbg
            )

    addition_button.bind("<Enter>", additionbutton_onenter)
    addition_button.bind("<Leave>", additionbutton_onleave)

    def divison_button_pressed():
        OptionsScreen.flashcardtype = "/"
        (
            OptionsScreen.explanationtitle,
            OptionsScreen.explanation,
            OptionsScreen.difficultyint1,
            OptionsScreen.difficultyint2,
        ) = OptionsScreen.get_info(
            OptionsScreen.flashcardtype, OptionsScreen.flashcarddifficulty
        )
        OptionsScreen.explanationtitle = "Divison -"
        OptionsScreen.explanation = "Put your division skills to the test!"
        OptionsScreen.clear_type_outline()
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_type_division,
            image=OptionsScreen.image_buttonbg_outline_selected,
        )
        mainscreen_canvas.itemconfigure(
            MainScreen.mathoperator, image=MainScreen.image_mathoperator_divide
        )

    division_button = Button(
        optionsscreen_canvas,
        image=image_division_button,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=lambda: OptionsScreen.divison_button_pressed(),
        relief="flat",
    )
    division_button.place(x=110.0, y=235.0, width=50.0, height=22.0)
    division_button.config(activebackground="#C3C3C3")

    def divisionbutton_onenter(event):
        event.widget.config(bg="#C3C3C3"),
        if OptionsScreen.flashcardtype == "/":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_type_division,
                image=OptionsScreen.image_buttonbg_outline_selected,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_type_division,
                image=OptionsScreen.image_buttonbg_selected,
            )

    def divisionbutton_onleave(event):
        event.widget.config(bg="#D9D9D9"),
        if OptionsScreen.flashcardtype == "/":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_type_division,
                image=OptionsScreen.image_buttonbg_outline,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_type_division, image=OptionsScreen.image_buttonbg
            )

    division_button.bind("<Enter>", divisionbutton_onenter)
    division_button.bind("<Leave>", divisionbutton_onleave)

    def clear_type_outline():
        Sound.sound_buttonpress.play()
        optionsscreen_canvas.itemconfig(
            OptionsScreen.description_title, text=OptionsScreen.explanationtitle
        )
        OptionsScreen.description.config(text=OptionsScreen.explanation)
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_type_addition, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_type_division, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_type_multiplication,
            image=OptionsScreen.image_buttonbg,
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_type_subtraction, image=OptionsScreen.image_buttonbg
        )
        Data.does_score_exist()
        optionsscreen_canvas.itemconfig(
            OptionsScreen.specific_highscore_text,
            text=Data.highscore_dict[
                f"{OptionsScreen.flashcardtype}-{OptionsScreen.flashcarddifficulty}-{OptionsScreen.flashcardtime}"
            ],
        )

    # Difficulty Buttons

    def classical_button_pressed():
        OptionsScreen.flashcarddifficulty = "classical"
        (
            OptionsScreen.explanationtitle,
            OptionsScreen.explanation,
            OptionsScreen.difficultyint1,
            OptionsScreen.difficultyint2,
        ) = OptionsScreen.get_info(
            OptionsScreen.flashcardtype, OptionsScreen.flashcarddifficulty
        )
        OptionsScreen.clear_difficulty_outline()
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_difficulty_classical,
            image=OptionsScreen.image_buttonbg_outline_selected,
        )

    classical_button = Button(
        optionsscreen_canvas,
        image=image_classical_button,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=lambda: OptionsScreen.classical_button_pressed(),
        relief="flat",
    )
    classical_button.place(x=375.0, y=91.0, width=50.0, height=22.0)
    classical_button.config(activebackground="#C3C3C3")

    def classicalbutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if OptionsScreen.flashcarddifficulty == "classical":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_difficulty_classical,
                image=OptionsScreen.image_buttonbg_outline_selected,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_difficulty_classical,
                image=OptionsScreen.image_buttonbg_selected,
            )

    def classicalbutton_onleave(event):
        event.widget.config(bg="#D9D9D9"),
        if OptionsScreen.flashcarddifficulty == "classical":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_difficulty_classical,
                image=OptionsScreen.image_buttonbg_outline,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_difficulty_classical,
                image=OptionsScreen.image_buttonbg,
            )

    classical_button.bind("<Enter>", classicalbutton_onenter)
    classical_button.bind("<Leave>", classicalbutton_onleave)

    def easy_button_pressed():
        OptionsScreen.flashcarddifficulty = "easy"
        (
            OptionsScreen.explanationtitle,
            OptionsScreen.explanation,
            OptionsScreen.difficultyint1,
            OptionsScreen.difficultyint2,
        ) = OptionsScreen.get_info(
            OptionsScreen.flashcardtype, OptionsScreen.flashcarddifficulty
        )
        OptionsScreen.clear_difficulty_outline()
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_difficulty_easy,
            image=OptionsScreen.image_buttonbg_outline_selected,
        )
        OptionsScreen.flashcarddifficulty = "easy"

    easy_button = Button(
        optionsscreen_canvas,
        image=image_easy_button,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=lambda: OptionsScreen.easy_button_pressed(),
        relief="flat",
    )
    easy_button.place(x=375.0, y=140.0, width=50.0, height=20.0)
    easy_button.config(activebackground="#C3C3C3")

    def easybutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if OptionsScreen.flashcarddifficulty == "easy":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_difficulty_easy,
                image=OptionsScreen.image_buttonbg_outline_selected,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_difficulty_easy,
                image=OptionsScreen.image_buttonbg_selected,
            )

    def easybutton_onleave(event):
        event.widget.config(bg="#D9D9D9")
        if OptionsScreen.flashcarddifficulty == "easy":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_difficulty_easy,
                image=OptionsScreen.image_buttonbg_outline,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_difficulty_easy,
                image=OptionsScreen.image_buttonbg,
            )

    easy_button.bind("<Enter>", easybutton_onenter)
    easy_button.bind("<Leave>", easybutton_onleave)

    def medium_button_pressed():
        OptionsScreen.flashcarddifficulty = "medium"
        (
            OptionsScreen.explanationtitle,
            OptionsScreen.explanation,
            OptionsScreen.difficultyint1,
            OptionsScreen.difficultyint2,
        ) = OptionsScreen.get_info(
            OptionsScreen.flashcardtype, OptionsScreen.flashcarddifficulty
        )
        OptionsScreen.clear_difficulty_outline()
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_difficulty_medium,
            image=OptionsScreen.image_buttonbg_outline_selected,
        )
        OptionsScreen.flashcarddifficulty = "medium"

    medium_button = Button(
        optionsscreen_canvas,
        image=image_medium_button,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=lambda: OptionsScreen.medium_button_pressed(),
        relief="flat",
    )
    medium_button.place(x=374.0, y=187.0, width=52.0, height=22.0)
    medium_button.config(activebackground="#C3C3C3")

    def mediumbutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if OptionsScreen.flashcarddifficulty == "medium":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_difficulty_medium,
                image=OptionsScreen.image_buttonbg_outline_selected,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_difficulty_medium,
                image=OptionsScreen.image_buttonbg_selected,
            )

    def mediumbutton_onleave(event):
        event.widget.config(bg="#D9D9D9")
        if OptionsScreen.flashcarddifficulty == "medium":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_difficulty_medium,
                image=OptionsScreen.image_buttonbg_outline,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_difficulty_medium,
                image=OptionsScreen.image_buttonbg,
            )

    medium_button.bind("<Enter>", mediumbutton_onenter)
    medium_button.bind("<Leave>", mediumbutton_onleave)

    def hard_button_pressed():
        OptionsScreen.flashcarddifficulty = "hard"
        (
            OptionsScreen.explanationtitle,
            OptionsScreen.explanation,
            OptionsScreen.difficultyint1,
            OptionsScreen.difficultyint2,
        ) = OptionsScreen.get_info(
            OptionsScreen.flashcardtype, OptionsScreen.flashcarddifficulty
        )
        OptionsScreen.clear_difficulty_outline()
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_difficulty_hard,
            image=OptionsScreen.image_buttonbg_outline_selected,
        )
        OptionsScreen.flashcarddifficulty = "hard"

    hard_button = Button(
        optionsscreen_canvas,
        image=image_hard_button,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=lambda: OptionsScreen.hard_button_pressed(),
        relief="flat",
    )
    hard_button.place(x=375.0, y=234.5, width=50.0, height=22.0)
    hard_button.config(activebackground="#C3C3C3")

    def hardbutton_onenter(event):
        event.widget.config(bg="#C3C3C3"),
        if OptionsScreen.flashcarddifficulty == "hard":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_difficulty_hard,
                image=OptionsScreen.image_buttonbg_outline_selected,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_difficulty_hard,
                image=OptionsScreen.image_buttonbg_selected,
            )

    def hardbutton_onleave(event):
        event.widget.config(bg="#D9D9D9"),
        if OptionsScreen.flashcarddifficulty == "hard":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_difficulty_hard,
                image=OptionsScreen.image_buttonbg_outline,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_difficulty_hard,
                image=OptionsScreen.image_buttonbg,
            )

    hard_button.bind("<Enter>", hardbutton_onenter)
    hard_button.bind("<Leave>", hardbutton_onleave)

    difficulty_info = {
        ("/", "classical"): (
            "Classical -",
            "Divide numbers up to 50's! A classical challenge!",
            1,
            50,
        ),
        ("-", "classical"): (
            "Classical -",
            "Subtract up to the 70's! A classical challenge!",
            1,
            79,
        ),
        ("*", "classical"): (
            "Classical -",
            "Times tables up to the 15's! A classical challenge!",
            1,
            15,
        ),
        ("+", "classical"): (
            "Classical -",
            "Addition up to the 70's! A classical challenge!",
            1,
            79,
        ),
        ("/", "easy"): ("Easy -", "Divide numbers 15 and below!", 1, 15),
        ("-", "easy"): ("Easy -", "Subtract numbers 30 and below!", 1, 29),
        ("*", "easy"): ("Easy -", "Times tables up to the 10's!", 1, 10),
        ("+", "easy"): ("Easy -", "Add numbers 30 and below!", 1, 29),
        ("/", "medium"): ("Medium -", "Divide numbers up to 25!", 1, 25),
        ("-", "medium"): ("Medium -", "Subtract numbers up to 50!", 1, 50),
        ("*", "medium"): ("Medium -", "Times tables up to the 13's!", 1, 13),
        ("+", "medium"): ("Medium -", "Add numbers up to 50!", 1, 50),
        ("/", "hard"): ("Hard -", "Divide numbers below the 100's!", 1, 99),
        ("-", "hard"): ("Hard -", "Subtract numbers below the 100's!", 1, 99),
        ("*", "hard"): ("Hard -", "Times tables up to the 20's!", 1, 20),
        ("+", "hard"): ("Hard -", "Add numbers below the 100's!", 1, 99),
    }

    def get_info(card_type, difficulty):
        return OptionsScreen.difficulty_info.get((card_type, difficulty))

    def clear_difficulty_outline():
        Sound.sound_buttonpress.play()
        optionsscreen_canvas.itemconfig(
            OptionsScreen.description_title, text=OptionsScreen.explanationtitle
        )
        OptionsScreen.description.config(text=OptionsScreen.explanation)
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_difficulty_hard, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_difficulty_medium, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_difficulty_easy, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_difficulty_classical,
            image=OptionsScreen.image_buttonbg,
        )
        Data.does_score_exist()
        optionsscreen_canvas.itemconfig(
            OptionsScreen.specific_highscore_text,
            text=Data.highscore_dict[
                f"{OptionsScreen.flashcardtype}-{OptionsScreen.flashcarddifficulty}-{OptionsScreen.flashcardtime}"
            ],
        )

    def practice_button_pressed():
        OptionsScreen.explanationtitle = "Practice -"
        OptionsScreen.flashcardtime = "practice"
        OptionsScreen.explanation = (
            "No time limit! Tone your math skills! (No results will be stored)"
        )
        OptionsScreen.clear_time_outline()
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_time_practice,
            image=OptionsScreen.image_buttonbg_outline_selected,
        )

    practice_button = Button(
        optionsscreen_canvas,
        image=image_practice_button,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=lambda: OptionsScreen.practice_button_pressed(),
        relief="flat",
    )
    practice_button.place(x=642.0, y=235.0, width=50.0, height=22.0)
    practice_button.config(activebackground="#C3C3C3")

    def practicebutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if OptionsScreen.flashcardtime == "practice":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_time_practice,
                image=OptionsScreen.image_buttonbg_outline_selected,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_time_practice,
                image=OptionsScreen.image_buttonbg_selected,
            )

    def practicebutton_onleave(event):
        event.widget.config(bg="#D9D9D9")
        if OptionsScreen.flashcardtime == "practice":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_time_practice,
                image=OptionsScreen.image_buttonbg_outline,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_time_practice, image=OptionsScreen.image_buttonbg
            )

    practice_button.bind("<Enter>", practicebutton_onenter)
    practice_button.bind("<Leave>", practicebutton_onleave)

    def twominute_button_pressed():
        OptionsScreen.minutes = 2
        OptionsScreen.seconds = 1
        OptionsScreen.explanationtitle = "2:00 -"
        OptionsScreen.explanation = "A good test of math skill and endurance! This is the standard flash card time!"
        OptionsScreen.flashcardtime = "twominute"
        OptionsScreen.clear_time_outline()
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_time_twominute,
            image=OptionsScreen.image_buttonbg_outline_selected,
        )

    twominute_button = Button(
        optionsscreen_canvas,
        image=image_twominute_button,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=lambda: OptionsScreen.twominute_button_pressed(),
        relief="flat",
    )
    twominute_button.place(x=644.0, y=92.0, width=47.0, height=20.0)
    twominute_button.config(activebackground="#C3C3C3")

    def twominutebutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if OptionsScreen.flashcardtime == "twominute":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_time_twominute,
                image=OptionsScreen.image_buttonbg_outline_selected,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_time_twominute,
                image=OptionsScreen.image_buttonbg_selected,
            )

    def twominutebutton_onleave(event):
        event.widget.config(bg="#D9D9D9")
        if OptionsScreen.flashcardtime == "twominute":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_time_twominute,
                image=OptionsScreen.image_buttonbg_outline,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_time_twominute,
                image=OptionsScreen.image_buttonbg,
            )

    twominute_button.bind("<Enter>", twominutebutton_onenter)
    twominute_button.bind("<Leave>", twominutebutton_onleave)

    def oneminute_button_pressed():
        OptionsScreen.minutes = 1
        OptionsScreen.seconds = 1
        OptionsScreen.explanationtitle = "1:00 -"
        OptionsScreen.explanation = "Low on time? how about a minute of pure math!"
        OptionsScreen.flashcardtime = "oneminute"
        OptionsScreen.clear_time_outline()
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_time_oneminute,
            image=OptionsScreen.image_buttonbg_outline_selected,
        )

    oneminute_button = Button(
        optionsscreen_canvas,
        image=image_oneminute_button,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=lambda: OptionsScreen.oneminute_button_pressed(),
        relief="flat",
    )
    oneminute_button.place(x=642.0, y=139.0, width=50.0, height=22.0)
    oneminute_button.config(activebackground="#C3C3C3")

    def oneminutebutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if OptionsScreen.flashcardtime == "oneminute":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_time_oneminute,
                image=OptionsScreen.image_buttonbg_outline_selected,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_time_oneminute,
                image=OptionsScreen.image_buttonbg_selected,
            )

    def oneminutebutton_onleave(event):
        event.widget.config(bg="#D9D9D9")
        if OptionsScreen.flashcardtime == "oneminute":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_time_oneminute,
                image=OptionsScreen.image_buttonbg_outline,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_time_oneminute,
                image=OptionsScreen.image_buttonbg,
            )

    oneminute_button.bind("<Enter>", oneminutebutton_onenter)
    oneminute_button.bind("<Leave>", oneminutebutton_onleave)

    def thirtysecond_button_pressed():
        OptionsScreen.minutes = 0
        OptionsScreen.seconds = 31
        OptionsScreen.explanationtitle = "0:30 -"
        OptionsScreen.explanation = (
            "Wanna show off? Only thirty seconds to show your true math skills!"
        )
        OptionsScreen.flashcardtime = "thirtysecond"
        OptionsScreen.clear_time_outline()
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_time_thirtysecond,
            image=OptionsScreen.image_buttonbg_outline_selected,
        )

    thirtysecond_button = Button(
        optionsscreen_canvas,
        image=image_thirtysecond_button,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=lambda: OptionsScreen.thirtysecond_button_pressed(),
        relief="flat",
    )
    thirtysecond_button.place(x=642.0, y=187.0, width=50.0, height=22.0)
    thirtysecond_button.config(activebackground="#C3C3C3")

    def thirtysecondbutton_onenter(event):
        event.widget.config(bg="#C3C3C3")
        if OptionsScreen.flashcardtime == "thirtysecond":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_time_thirtysecond,
                image=OptionsScreen.image_buttonbg_outline_selected,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_time_thirtysecond,
                image=OptionsScreen.image_buttonbg_selected,
            )

    def thirtysecondbutton_onleave(event):
        event.widget.config(bg="#D9D9D9")
        if OptionsScreen.flashcardtime == "thirtysecond":
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_time_thirtysecond,
                image=OptionsScreen.image_buttonbg_outline,
            )
        else:
            optionsscreen_canvas.itemconfigure(
                OptionsScreen.buttonbg_time_thirtysecond,
                image=OptionsScreen.image_buttonbg,
            )

    thirtysecond_button.bind("<Enter>", thirtysecondbutton_onenter)
    thirtysecond_button.bind("<Leave>", thirtysecondbutton_onleave)

    def clear_time_outline():
        Sound.sound_buttonpress.play()
        optionsscreen_canvas.itemconfig(
            OptionsScreen.description_title, text=OptionsScreen.explanationtitle
        )
        OptionsScreen.description.config(text=OptionsScreen.explanation)
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_time_thirtysecond, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_time_twominute, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_time_oneminute, image=OptionsScreen.image_buttonbg
        )
        optionsscreen_canvas.itemconfigure(
            OptionsScreen.buttonbg_time_practice, image=OptionsScreen.image_buttonbg
        )
        Data.does_score_exist()
        optionsscreen_canvas.itemconfig(
            OptionsScreen.specific_highscore_text,
            text=Data.highscore_dict[
                f"{OptionsScreen.flashcardtype}-{OptionsScreen.flashcarddifficulty}-{OptionsScreen.flashcardtime}"
            ],
        )

    # Back Button
    def back_button_pressed():
        Sound.sound_buttonpress.play()
        optionsscreen_canvas.pack_forget()
        mainscreen_canvas.pack()

    back_button = Button(
        optionsscreen_canvas,
        image=image_back_button,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=lambda: OptionsScreen.back_button_pressed(),
        relief="flat",
    )
    back_button.place(x=60.0, y=440.0, width=94.0, height=30.0)
    back_button.config(activebackground="#C3C3C3")

    def backbutton_onenter(event):
        event.widget.config(bg="#C3C3C3"), optionsscreen_canvas.itemconfigure(
            OptionsScreen.back_buttonbg,
            image=OptionsScreen.image_back_buttonbg_selected,
        ),

    def backbutton_onleave(event):
        event.widget.config(bg="#D9D9D9"), optionsscreen_canvas.itemconfigure(
            OptionsScreen.back_buttonbg, image=OptionsScreen.image_back_buttonbg
        )

    back_button.bind("<Enter>", backbutton_onenter)
    back_button.bind("<Leave>", backbutton_onleave)

    # Placed Text
    description_title = optionsscreen_canvas.create_text(
        215.0,
        330.0,
        anchor="nw",
        text=explanationtitle,
        fill="#000000",
        font=("Encode Sans", 24 * -1),
    )

    description = Label(
        optionsscreen_canvas,
        anchor="nw",
        text=explanation,
        font=("Encode Sans", 17 * -1),
        wraplength=211,
        fg="#000000",
        bg="#FFFFFF",
    )
    description.place(x=296, y=382)


class FinalScreen:
    finalscore_feedback_text = ""

    image_scorebanner = PhotoImage(
        file=relative_to_assets("finalscreen/scorebanner.png")
    )
    image_scoreseperator = PhotoImage(
        file=relative_to_assets("finalscreen/scoreseperator.png")
    )
    image_scorebg = PhotoImage(file=relative_to_assets("finalscreen/scorebg.png"))
    image_buttonbanner = PhotoImage(
        file=relative_to_assets("finalscreen/buttonbanner.png")
    )
    image_feedbackbanner = PhotoImage(
        file=relative_to_assets("finalscreen/feedbackbanner.png")
    )
    image_buttonbg = PhotoImage(file=relative_to_assets("finalscreen/buttonbg.png"))
    image_buttonbg_selected = PhotoImage(
        file=relative_to_assets("finalscreen/buttonbg_selected.png")
    )
    image_continue_button = PhotoImage(
        file=relative_to_assets("finalscreen/continue_button.png")
    )

    bg_image = finalscreen_canvas.create_image(
        395.0, 255.0, image=UserScreen.image_bg_image
    )
    scorebanner = finalscreen_canvas.create_image(391.0, 197.0, image=image_scorebanner)
    scoreseperator_1 = finalscreen_canvas.create_image(
        392.0, 90.0, image=image_scoreseperator
    )
    scoreseperator_2 = finalscreen_canvas.create_image(
        392.0, 194.0, image=image_scoreseperator
    )
    scoreseperator_3 = finalscreen_canvas.create_image(
        392.0, 299.0, image=image_scoreseperator
    )
    scorebg_1 = finalscreen_canvas.create_image(391.0, 117.0, image=image_scorebg)
    scorebg_2 = finalscreen_canvas.create_image(391.0, 221.0, image=image_scorebg)
    scorebg_3 = finalscreen_canvas.create_image(391.0, 332.0, image=image_scorebg)
    buttonbanner = finalscreen_canvas.create_image(
        391.0, 436.0, image=image_buttonbanner
    )
    feedbackbanner = finalscreen_canvas.create_image(
        620.0, 436.0, image=image_feedbackbanner
    )
    buttonbg = finalscreen_canvas.create_image(620.0, 436.0, image=image_buttonbg)

    yourscore_text = finalscreen_canvas.create_text(
        390.0,
        118.0,
        anchor="center",
        text="",
        fill="#000000",
        font=("Encode Sans", 33 * -1),
    )
    incorrect_text = finalscreen_canvas.create_text(
        390.0,
        222.0,
        anchor="center",
        text="",
        fill="#000000",
        font=("Encode Sans", 33 * -1),
    )
    highscore_text = finalscreen_canvas.create_text(
        391.0,
        332.0,
        anchor="center",
        text="",
        fill="#000000",
        font=("Encode Sans", 33 * -1),
    )
    feedback_text = finalscreen_canvas.create_text(
        390.0,
        435.0,
        anchor="center",
        text="",
        fill="#000000",
        font=(
            "Encode Sans",
            19 * -1,
            "bold",
        ),
    )
    finalscreen_canvas.create_text(
        308.0,
        44.0,
        anchor="nw",
        text="You Scored",
        fill="#000000",
        font=("Encode Sans", 35 * -1),
    )
    finalscreen_canvas.create_text(
        310.0,
        250.0,
        anchor="nw",
        text="High Score",
        fill="#000000",
        font=("Encode Sans", 35 * -1),
    )
    finalscreen_canvas.create_text(
        325.0,
        146.0,
        anchor="nw",
        text="Incorrect",
        fill="#000000",
        font=("Encode Sans", 35 * -1),
    )

    def continue_button_pressed():
        Sound.sound_buttonpress.play()
        MainScreen.post_game_cleanup()
        finalscreen_canvas.pack_forget()
        mainscreen_canvas.pack()

    continue_button = Button(
        finalscreen_canvas,
        image=image_continue_button,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=lambda: FinalScreen.continue_button_pressed(),
        relief="flat",
    )
    continue_button.place(x=584.0, y=424.0, width=72.0, height=25.0)
    continue_button.config(activebackground="#C3C3C3")

    def continuebutton_onenter(event):
        event.widget.config(bg="#C3C3C3"), finalscreen_canvas.itemconfigure(
            FinalScreen.buttonbg, image=FinalScreen.image_buttonbg_selected
        ),

    def continuebutton_onleave(event):
        event.widget.config(bg="#D9D9D9"), finalscreen_canvas.itemconfigure(
            FinalScreen.buttonbg, image=FinalScreen.image_buttonbg
        )

    continue_button.bind("<Enter>", continuebutton_onenter)
    continue_button.bind("<Leave>", continuebutton_onleave)


class HistoryScreen:
    image_actionbuttonbg = PhotoImage(
        file=relative_to_assets("historyscreen/actionbuttonbg.png")
    )
    image_actionbuttonbg_selected = PhotoImage(
        file=relative_to_assets("historyscreen/actionbuttonbg_selected.png")
    )
    image_buttonbanner = PhotoImage(
        file=relative_to_assets("historyscreen/buttonbanner.png")
    )
    image_back_button = PhotoImage(
        file=relative_to_assets("historyscreen/back_button.png")
    )
    image_datasheet_bg = PhotoImage(
        file=relative_to_assets("historyscreen/datasheet_bg.png")
    )
    image_info_button = PhotoImage(
        file=relative_to_assets("historyscreen/info_button.png")
    )

    bg_image = historyscreen_canvas.create_image(
        395.0, 255.0, image=UserScreen.image_bg_image
    )
    buttonbanner_1 = historyscreen_canvas.create_image(
        89.0, 454.0, image=image_buttonbanner
    )
    buttonbanner_2 = historyscreen_canvas.create_image(
        709.0, 454.0, image=image_buttonbanner
    )
    actionbuttonbg_1 = historyscreen_canvas.create_image(
        89.0, 453.0, image=image_actionbuttonbg
    )
    actionbuttonbg_2 = historyscreen_canvas.create_image(
        710.0, 453.0, image=image_actionbuttonbg
    )
    datasheet_bg = historyscreen_canvas.create_image(
        399.0, 227.0, image=image_datasheet_bg
    )

    def back_button_pressed():
        Sound.sound_buttonpress.play()
        historyscreen_canvas.pack_forget()
        mainscreen_canvas.pack()

    back_button = Button(
        historyscreen_canvas,
        image=image_back_button,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=lambda: HistoryScreen.back_button_pressed(),
        relief="flat",
    )
    back_button.place(x=42.0, y=438.0, width=93.0, height=30.0)
    back_button.config(activebackground="#C3C3C3")

    def backbutton_onenter(event):
        event.widget.config(bg="#C3C3C3"), historyscreen_canvas.itemconfigure(
            HistoryScreen.actionbuttonbg_1,
            image=HistoryScreen.image_actionbuttonbg_selected,
        ),

    def backbutton_onleave(event):
        event.widget.config(bg="#D9D9D9"), historyscreen_canvas.itemconfigure(
            HistoryScreen.actionbuttonbg_1, image=HistoryScreen.image_actionbuttonbg
        )

    back_button.bind("<Enter>", backbutton_onenter)
    back_button.bind("<Leave>", backbutton_onleave)

    def info_button_pressed():
        Sound.sound_buttonpress.play()
        profilescreen_canvas.pack()
        historyscreen_canvas.pack_forget()
        ProfileScreen.personalize_screen(Data.userlevel)
        ProfileScreen.button_back.config(
            command=lambda: HistoryScreen.changed_back_button_pressed()
        )
        profilescreen_canvas.coords(ProfileScreen.history_bg, 1000, 1000)
        profilescreen_canvas.coords(ProfileScreen.history_banner, 1000, 1000)
        profilescreen_canvas.coords(ProfileScreen.edit_bg, 1000, 1000)
        profilescreen_canvas.coords(ProfileScreen.edit_banner, 1000, 1000)
        ProfileScreen.button_history.place_configure(x=1000, y=1000)
        ProfileScreen.button_edit.place_configure(x=1000, y=1000)

    def changed_back_button_pressed():
        Sound.sound_buttonpress.play()
        historyscreen_canvas.pack()
        profilescreen_canvas.pack_forget()
        profilescreen_canvas.coords(ProfileScreen.history_bg, 399.0, 451.0)
        profilescreen_canvas.coords(ProfileScreen.history_banner, 399.0, 452.0)
        profilescreen_canvas.coords(ProfileScreen.edit_bg, 601.0, 452.0)
        profilescreen_canvas.coords(ProfileScreen.edit_banner, 601.0, 451.0)
        ProfileScreen.button_history.place_configure(x=366.0, y=437.0)
        ProfileScreen.button_edit.place_configure(x=568.0, y=437.0)
        ProfileScreen.button_back.config(
            command=lambda: ProfileScreen.button_back_pressed()
        )

    info_button = Button(
        historyscreen_canvas,
        image=image_info_button,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=lambda: HistoryScreen.info_button_pressed(),
        relief="flat",
    )
    info_button.place(x=663.0, y=438.0, width=93.0, height=30.0)
    info_button.config(activebackground="#C3C3C3")

    def infobutton_onenter(event):
        event.widget.config(bg="#C3C3C3"), historyscreen_canvas.itemconfigure(
            HistoryScreen.actionbuttonbg_2,
            image=HistoryScreen.image_actionbuttonbg_selected,
        ),

    def infobutton_onleave(event):
        event.widget.config(bg="#D9D9D9"), historyscreen_canvas.itemconfigure(
            HistoryScreen.actionbuttonbg_2, image=HistoryScreen.image_actionbuttonbg
        )

    info_button.bind("<Enter>", infobutton_onenter)
    info_button.bind("<Leave>", infobutton_onleave)

    tree = ttk.Treeview(
        historyscreen_canvas,
        columns=("date", "time", "correct", "incorrect", "mode", "%"),
        show="headings",
    )

    tree.heading("date", text="Date")
    tree.heading("time", text="Time")
    tree.heading("correct", text="Correct")
    tree.heading("incorrect", text="Incorrect")
    tree.heading("mode", text="Mode")
    tree.heading("%", text="%")

    tree.column("date", width=90, stretch=False, anchor="center")
    tree.column("time", width=90, stretch="no", anchor="center")
    tree.column("correct", width=70, stretch="no", anchor="center")
    tree.column("incorrect", width=70, stretch="no", anchor="center")
    tree.column("mode", width=160, stretch="no", anchor="center")
    tree.column("%", width=70, stretch="no", anchor="center")

    def display_data(userlevel):
        from sv_ttk import use_light_theme

        use_light_theme()
        try:
            HistoryScreen.tree.delete(*HistoryScreen.tree.get_children())
        except:
            pass
        for game in Data.user_data[userlevel]["gamehistory"]:
            try:
                game_percentage = game["correct"] / (
                    game["incorrect"] + game["correct"]
                )
                HistoryScreen.tree.insert(
                    "",
                    "end",
                    values=(
                        game["date"],
                        game["time"],
                        game["correct"],
                        game["incorrect"],
                        game["mode"],
                        f"{round(game_percentage * 100, 2)}%",
                    ),
                )
            except:
                pass

    scrollbar = ttk.Scrollbar(
        historyscreen_canvas, orient="vertical", command=tree.yview
    )
    tree.configure(yscrollcommand=scrollbar.set)

    def disableEvent(event):
        return "break"

    tree.bind("<Button-1>", disableEvent)

    tree.place(x=110, y=67, height=317, width=560)
    scrollbar.place(x=673, y=67, height=317)


Data.check_for_users()
userscreen_canvas.pack()

window.geometry("800x500")
window.configure(bg=WINDOW_COLOR)
window.title("Tkinter Math Flash Cards")
window.iconbitmap("main.ico")

window.resizable(False, False)
window.mainloop()
