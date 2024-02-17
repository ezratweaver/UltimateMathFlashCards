import os
from sys import argv
from tkinter import Tk, PhotoImage, font

# exe_dir = os.path.dirname(os.path.abspath(argv[0]))
# os.chdir(exe_dir)

if os.path.basename(os.getcwd()) == "screens":
    os.chdir("../assets")

WINDOW_COLOR = "#3556FB"

BUTTONS_FOLDER = "buttons"
USERSCREEN_FOLDER = "user_screen"
TEXTSCREEN_FOLDER = "text_screen"
PROFILESCREEN_FOLDER = "profile_screen"

ENTER_EVENT_ID = 7
LEAVE_EVENT_ID = 8

root = Tk()
root.geometry("800x500")
root.title("")
root.resizable(False, False)


def button_event_map(event, canvas,
                     image_variable, new_image):
    """
    Modifies the appearance of an image on a canvas based on the given event.

    Args:
        event (Event): The event object triggered by the user.
        canvas (Canvas): The tk Canvas() object where the image is displayed.
        image_variable (int): Variable of the image object displaying image
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
        canvas.bind("<Enter>", lambda event: button_event_map(event, canvas, 1, my_image))
        canvas.bind("<Leave>", lambda event: button_event_map(event, canvas, 1, my_image))

    """
    color = "#C3C3C3"
    if int(event.type) == ENTER_EVENT_ID:
        color = "#C3C3C3"
    if int(event.type) == LEAVE_EVENT_ID:
        color = "#D9D9D9"
    event.widget.config(bg=color, activebackground=color)
    canvas.itemconfigure(image_variable, image=new_image)


def add_image(subfolder: str, filename: str):
    """
    Load image asset from 'assets/subfolder/filename.png' and return PhotoImage obj.

    Parameters:
        subfolder (str): Subfolder name inside 'assets' directory.
        filename (str): Name of the image file to load (extension must be .png).

    Returns:
        PhotoImage: Loaded image asset as a PhotoImage object.

    """
    return PhotoImage(file=f"images/{subfolder}/{filename}.png")


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


def grab_all_images(subfolder: str) -> dict:
    """
    Retrieve PNG assets from the specified subfolder.

    Args:
        subfolder (str): The name of the subfolder within the 'assets' directory.

    Returns:
        dict: A dictionary mapping asset file names (without file extension)
                to PhotoImage objects

    """
    dictionary = {}
    asset_directory = f"images/{subfolder}"
    for filename in os.listdir(asset_directory):
        if filename.endswith('.png'):
            file_path = os.path.join(asset_directory, filename)
            dictionary[filename[:-4]] = PhotoImage(file=file_path)
    return dictionary


def bind_hover_animation(canvas: Tk, button_bgs: dict, buttons: dict,
                         bg_image: PhotoImage, bg_image_selected: PhotoImage) -> None:
    """Binds hover events to buttons on a canvas, modifying their images.

    This function assigns event bindings to the buttons on a canvas to dynamically
    modify their background images when the mouse enters or leaves the button area.
    It utilizes the button_event_map function to handle the image modifications.

    Description:
        This function iterates over the buttons dictionary and binds "<Enter>" and 
        "<Leave>" events to each button. When the mouse enters the button area, the
        associated button_event_map function is called with the event, canvas, button
        background image, and the selected background image. This modifies the 
        appearance of the button to indicate the hover effect. When the mouse leaves the
        button area, the button_event_map function is called again to revert the appearance
        back to the original state.

    Requires:
        button_event_map()

    Args:
        canvas (tkinter.Canvas): The canvas on which the buttons are placed.
        button_bgs (dict): A dictionary mapping button keys to their respective
                                background images.
        buttons (dict): A dictionary mapping button keys to tkinter.Button objects.
        bg_image (PIL.Image.Image): The background image for the buttons when
                                        not selected.
        bg_image_selected (PIL.Image.Image): The background image for the buttons
                                                when selected.

    Returns:
        None

    Example:
        bind_hover_animation(canvas, button_bgs, buttons, bg_image, bg_image_selected)

    """
    for key, button in buttons.items():
        button.bind("<Enter>", lambda event, x=key:
        button_event_map(event, canvas,
                         button_bgs[x], bg_image_selected))
        button.bind("<Leave>", lambda event, x=key:
        button_event_map(event, canvas,
                         button_bgs[x], bg_image))


userscreen_banners = {
    1: PhotoImage(file="images/user_screen/userlist_1.png"),
    2: PhotoImage(file="images/user_screen/userlist_2.png"),
    3: PhotoImage(file="images/user_screen/userlist_3.png"),
    4: PhotoImage(file="images/user_screen/userlist_4.png"),
    5: PhotoImage(file="images/user_screen/userlist_5.png"),
    6: PhotoImage(file="images/user_screen/userlist_6.png"),
}
userscreen_useradd = add_image(
    USERSCREEN_FOLDER, "useradd")
userscreen_userprofile = add_image(
    USERSCREEN_FOLDER, "userprofile")

buttons = grab_all_images(BUTTONS_FOLDER)
textscreen = grab_all_images(TEXTSCREEN_FOLDER)
profilescreen = grab_all_images(PROFILESCREEN_FOLDER)

if __name__ == "__main__":
    print("Script ran without errors.")
