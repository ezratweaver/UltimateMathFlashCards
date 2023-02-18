from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import random
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0") 
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
    

def math_quiz():
    global run
    global math
    global QuizNumber1
    global QuizNumber2
    global canvasnumber1
    global canvasnumber2    
    QuizNumber1 = (random.randint(1, 10))                              
    QuizNumber2 = (random.randint(1, 10))
    canvas.itemconfig(canvasnumber1, text=QuizNumber1)
    canvas.itemconfig(canvasnumber2, text=QuizNumber2)

def input(event):
    global run
    global answertxt
    global MathAnswerOutput
    QuizMathAnswer = QuizNumber1 * QuizNumber2
    response = entry_1.get()
    try:
        if int(response) == QuizMathAnswer:
            MathAnswerOutput = 'Correct!'
            canvas.itemconfig(MathAnswerCanvas, text=MathAnswerOutput,fill="#000000",font=("Inter", 15 * -1))
        else:
            MathAnswerOutput = 'Wrong!'
            canvas.itemconfig(MathAnswerCanvas, text=MathAnswerOutput,fill="#000000",font=("Inter", 15 * -1))
        math_quiz()
    except ValueError as e:
        print(e)
    entry_1.delete(0, 'end')


QuizNumber1 = (random.randint(1, 10))                              
QuizNumber2 = (random.randint(1, 10))


#GUI CODE
window = Tk()
window.title("Ezra's Math Flashcards 2.1")
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
    272.0,
    133.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    272.0,
    282.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    font=("Inter", 15 * -1),
    highlightthickness=0
)
entry_1.bind('<Return>', input)
entry_1.place(
    x=212.0,
    y=263.0,
    width=120.0,
    height=36.0
)

canvasnumber1 = canvas.create_text(
        219.0,
        55.0,
        anchor="nw",
        text=QuizNumber1,
        fill="#000000",
        font=("Inter", 25 * -1)
    )

canvasnumber2 = canvas.create_text(
        219.0,
        80.199951171875,
        anchor="nw",
        text=QuizNumber2,
        fill="#000000",
        font=("Inter", 25 * -1)
    )

canvas.create_text(
    250.0,
    80.199951171875,
    anchor="nw",
    text='x',
    fill="#000000",
    font=("Inter", 25 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    272.0,
    194.0,
    image=image_image_2
)

MathAnswerCanvas = canvas.create_text(
        241.0,
        186.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 15 * -1)
    )
window.resizable(False, False)
window.mainloop()

math_quiz()
