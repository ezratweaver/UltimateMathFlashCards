#THIS REQUIRES PYGAME AND TKINTER TO RUN!!!!


from pathlib import Path
from tkinter import Tk, Canvas, Entry, PhotoImage
import random
import os
import pygame
os.chdir(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0") 


pygame.mixer.init()
CorrectSound = pygame.mixer.Sound('assets/sounds/correct.wav')
WrongSound = pygame.mixer.Sound('assets/sounds/wrong.wav')
WrongSound.set_volume(0.3)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

os.system("CD")

def math_quiz():
    global QuizNumber1
    global QuizNumber2
    global canvasnumber1
    global canvasnumber2    
    QuizNumber1 = (random.randint(1, 12))                              
    QuizNumber2 = (random.randint(1, 12))
    canvas.itemconfig(canvasnumber1, text=QuizNumber1)
    canvas.itemconfig(canvasnumber2, text=QuizNumber2)


def input(event):
    global MathAnswerOutput
    global QuizMathAnswer
    QuizMathAnswer = QuizNumber1 * QuizNumber2
    canvas.itemconfig(CanvasMathAnswer, text=QuizMathAnswer)
    UserResponse = entry_1.get()
    try:
        if int(UserResponse) == QuizMathAnswer:
            MathAnswerOutput = 'Correct!'
            CorrectSound.play()
            canvas.itemconfig(MathAnswerCanvas, text=MathAnswerOutput,fill="#000000",font=("Inter", 32 * -1))
        else:
            MathAnswerOutput = ' Wrong!'
            WrongSound.play()
            canvas.itemconfig(MathAnswerCanvas, text=MathAnswerOutput,fill="#000000",font=("Inter", 32 * -1))
        math_quiz()
    except ValueError as e:
        print(e)
    entry_1.delete(0, 'end')

QuizNumber1 = (random.randint(1, 10))                              
QuizNumber2 = (random.randint(1, 10))

window = Tk()
window.title("Ezra's Math Flashcards 2.2")
window.geometry("545x363")
window.configure(bg = "#FFFFFF")
window.iconbitmap("math.ico")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 363,
    width = 545,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    552.0,
    363.0,
    fill="#1084EF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    275.0,
    185.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    272.0,
    133.0,
    image=image_image_2
)

canvasnumber1 = canvas.create_text(
    238.0,
    58.0,
    anchor="nw",
    text=QuizNumber1,
    fill="#000000",
    font=("Inter", 45 * -1)
)

canvasnumber2 = canvas.create_text(
    238.0,
    107.0,
    anchor="nw",
    text=QuizNumber2,
    fill="#000000",
    font=("Inter", 45 * -1)
)

canvas.create_text(
    301.0,
    115.0,
    anchor="nw",
    text="X",
    fill="#000000",
    font=("Inter", 33 * -1)
)

canvas.create_rectangle(
    233.0,
    159.0,
    327.0,
    163.0,
    fill="#000000",
    outline="")

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    272.0,
    255.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    383.0,
    255.0,
    image=image_image_4
)
MathAnswerOutput = ''
MathAnswerCanvas = canvas.create_text(
    213.0,
    237.0,
    anchor="nw",
    text=MathAnswerOutput,
    fill="#000000",
    font=("Inter", 32 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    260.0,
    186.0,
    image=image_image_5
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    260.0,
    186.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Inter", 20 * -1),
    highlightthickness=0
)
entry_1.bind('<Return>', input)
entry_1.place(
    x=243.0,
    y=172.0,
    width=32.0,
    height=27.0
)
QuizMathAnswer = ''
CanvasMathAnswer = canvas.create_text(
    356.0,
    238.0,
    anchor="nw",
    text=QuizMathAnswer,
    fill="#000000",
    font=("Inter", 32 * -1)
)
window.resizable(False, False)
window.mainloop()
