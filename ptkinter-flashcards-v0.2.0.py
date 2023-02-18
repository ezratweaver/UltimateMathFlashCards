#my original math flash card program programed into a GUI
import tkinter as tk      
import random
root = tk.Tk()
root.geometry("200x170")
root.resizable(False, False)
root.title('Math Flash Cards')

run = 1
def math_quiz():
    global run
    global math
    global number1
    global number2
    global text6
    global text7
    number1 = (random.randint(1, 10))                              
    number2 = (random.randint(1, 10))
    math = number1 * number2
    run = run - 1
    text6.config(text=number1)
    text7.config(text=number2)

def input(event):
    global run
    global answertxt 
    response = entry.get()
    try:
        if int(response) == math:
            answertxt = tk.Label(text='Correct')
            answertxt.grid(row=8, column=0)
            math_quiz()
        else:
            answertxt = tk.Label(text='Wrong')
            answertxt.grid(row=8, column=0)
            math_quiz()
    except ValueError as e:
        print(e)
    entry.delete(0, 'end')

entry = tk.Entry(root)
entry.grid(row=8, column=1)
entry.bind('<Return>', input)
text6 = tk.Label(root)
text7 = tk.Label(root)
text6.grid(row=6, column=1)
text7.grid(row=7, column=1)
math_quiz()
root.mainloop()
