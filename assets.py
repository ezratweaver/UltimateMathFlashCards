from tkinter import Tk, PhotoImage, font
from os import path, chdir, listdir
from sys import argv

exe_dir = path.dirname(path.abspath(argv[0]))
chdir(exe_dir)

WINDOW_COLOR = "#3556FB"

BUTTONS_FOLDER = "buttons"
USERSCREEN_FOLDER = "userscreen"
TEXTSCREEN_FOLDER = "textscreen"
PROFILESCREEN_FOLDER = "profilescreen"

ENTER_EVENT_ID = 7
LEAVE_EVENT_ID = 8

root = Tk()
root.geometry("800x500")
root.title("")
root.resizable(False, False)

def image_modify(event, canvas,
                    image_variable, new_image):
    """
    Modifies the appearance of an image on a canvas based on the given event.

    Args:
        event (Event): The event object triggered by the user.
        canvas (Canvas): The canvas object where the image is displayed.
        image_variable (int): The variable assigned to the image on the canvas
        new_image (PhotoImage): The new image to be displayed.

    Returns:
        None

    Description:
            This function modifies the appearance of an image on a canvas based on the 
        given event. If the event type is an ENTER_EVENT_ID, the image's background
        color and active background color are set to "#C3C3C3". If the event type is a 
        LEAVE_EVENT_ID, the image's background color and active background color are set
        to "#D9D9D9". The function then updates the image on the canvas with the 
        new_image provided.

    Example:
        # Binding events and modifying the image
        canvas.bind("<Enter>", lambda event: image_modify(event, canvas, 1, my_image))
        canvas.bind("<Leave>", lambda event: image_modify(event, canvas, 1, my_image))

    """
    if int(event.type) == ENTER_EVENT_ID:
        color = "#C3C3C3"
    if int(event.type) == LEAVE_EVENT_ID:
        color = "#D9D9D9"
    event.widget.config(bg=color, activebackground=color)
    canvas.itemconfigure(image_variable, image=new_image)

def add_asset(subfolder:str, filename:str):
    """
    Load image asset from 'assets/subfolder/filename.png' and return PhotoImage obj.

    Parameters:
        subfolder (str): Subfolder name inside 'assets' directory.
        filename (str): Name of the image file to load (extension must be .png).

    Returns:
        PhotoImage: Loaded image asset as a PhotoImage object.

    """
    return PhotoImage(file=f"assets/{subfolder}/{filename}.png")

def get_font_size(text: str, button: object, inputfont: object, root: object) -> int:
    """
    Calculate the optimal font size for a given text to fit within the 
        dimensions of a button.

    This function determines the appropriate font size that allows the specified `text` 
    to fit comfortably within the dimensions of the `button` widget. It takes into 
    account the current font settings specified by the `inputfont` object.

    Args:
        text (str): The content of the text.
        button (object): The tkinter button object for which the font size 
                            needs to be calculated.
        inputfont (object): The tkinter font object representing the initial
                            font settings.
        root (object): The tkinter root object.

    Returns:
        int: The optimal font size that ensures the `text` fits within the 
                dimensions of the `button`.

    """
    instance_font = font.Font(font=inputfont)
    root.update()
    button_height = button.winfo_height() 
    button_width = button.winfo_width() - 5
    font_height = instance_font.metrics("linespace")
    font_width = instance_font.measure(text) 
    font_size = int(instance_font.cget("size"))
    while font_height > button_height or font_width > button_width:
        font_height = instance_font.metrics("linespace")
        font_width = instance_font.measure(text)
        font_size = font_size - 1
        instance_font.configure(size=font_size)
    return font_size

def grab_all_assets(subfolder: str) -> dict:
    """
    Retrieve PNG assets from the specified subfolder.

    Args:
        subfolder (str): The name of the subfolder within the 'assets' directory.

    Returns:
        dict: A dictionary mapping asset names (without extension) to PhotoImage objects

    """
    dictionary = {}
    asset_directory = f"assets/{subfolder}"
    for filename in listdir(asset_directory):
        if filename.endswith('.png'):
            file_path = path.join(asset_directory, filename)
            dictionary[filename[:-4]] = PhotoImage(file=file_path)
    return dictionary

def bind_buttons(canvas, button_bgs, buttons, bg_image, bg_image_selected):
    for key, button in buttons.items():
            button.bind("<Enter>", lambda event, x=key:
                image_modify(event, canvas,
                button_bgs[x], bg_image_selected))
            button.bind("<Leave>", lambda event, x=key:
                image_modify(event, canvas,
                button_bgs[x], bg_image))

userscreen_banners = {
    1: PhotoImage(file="assets/userscreen/userlist_1.png"),
    2: PhotoImage(file="assets/userscreen/userlist_2.png"),
    3: PhotoImage(file="assets/userscreen/userlist_3.png"),
    4: PhotoImage(file="assets/userscreen/userlist_4.png"),
    5: PhotoImage(file="assets/userscreen/userlist_5.png"),
    6: PhotoImage(file="assets/userscreen/userlist_6.png"),
}
userscreen_useradd = add_asset(
    USERSCREEN_FOLDER, "useradd")
userscreen_userprofile = add_asset(
    USERSCREEN_FOLDER, "userprofile")

buttons = grab_all_assets(BUTTONS_FOLDER)
textscreen = grab_all_assets(TEXTSCREEN_FOLDER)
profilescreen = grab_all_assets(PROFILESCREEN_FOLDER)

if __name__ == "__main__":
    print(profilescreen)
