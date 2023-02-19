from pathlib import Path
from random import randint
from os import chdir, path, system, name, environ
from pygame import mixer
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox


def resource_path(relative):
    return path.join(
        environ.get(
            "_MEIPASS2",
            path.abspath(".")
        ),
        relative
    )

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(resource_path("assets/frame0")) 
system('cls' if name == 'nt' else 'clear')
print('Loading Assets...')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

mixer.init()
soundCorrect = mixer.Sound(resource_path('assets/sounds/correct.wav'))
soundWrong = mixer.Sound(resource_path('assets/sounds/wrong.wav'))
soundCountdown = mixer.Sound(resource_path('assets/sounds/countdown.wav'))
soundCountdownStart = mixer.Sound(resource_path('assets/sounds/countdownstart.wav'))
soundTimesup = mixer.Sound(resource_path('assets/sounds/timesup.wav'))
soundClockticking = mixer.Sound(resource_path('assets/sounds/clockticking.wav'))
soundWrong.set_volume(0.3)

def generateNewProblem():
    global flashCard1
    global flashCard2
    global flashCard1Canv
    global flashCard2Canv   
    global correctAnswer
    global failedProblem
    global wrongFlashCard1
    global wrongFlashCard2
    global questionsDone
    global currentProblem
    global numberOfQuestionsDelay 
    global previousProblem
    flashCard1 = (randint(1, 12))                              
    flashCard2 = (randint(1, 12))
    currentProblem = (flashCard1, flashCard2)
    isProblemDuplicate()
    canvas.itemconfig(flashCard1Canv, text=flashCard1)
    canvas.itemconfig(flashCard2Canv, text=flashCard2)
    if questionsDone == numberOfQuestionsDelay:
        canvas.itemconfig(flashCard1Canv, text=wrongFlashCard1)
        canvas.itemconfig(flashCard2Canv, text=wrongFlashCard2)
        failedProblem = False
        questionsDone = 0
        correctAnswer = wrongFlashCard1 * wrongFlashCard2
    else:
        correctAnswer = flashCard1 * flashCard2

failedProblem = False
questionsDone = 0
numberOfQuestionsDelay = None
previousProblem = None

def isProblemDuplicate():
    global previousProblem
    global currentProblem
    if previousProblem == currentProblem:
        generateNewProblem()

def userPressedEnter(event):
    global quizFeedback
    global correctAnswer
    global currentScore
    global failedProblem
    global questionsDone
    global numberOfQuestionsDelay
    global flashCard1
    global flashCard2
    global wrongFlashCard1
    global wrongFlashCard2
    global previousProblem
    userAnswer = userEntrybox.get()
    previousProblem = (flashCard1, flashCard2)
    try:
        if failedProblem == True:
            questionsDone = questionsDone + 1
        if int(userAnswer) == correctAnswer:
            quizFeedback = 'Correct!'
            soundCorrect.play()
            currentScore = currentScore + 1
            if currentScore > 9:
                canvas.coords(currentScoreCanv, 147, 151.5)   
        else:
            quizFeedback = ' Wrong!'
            soundWrong.play()
            if currentScore > 0:
                currentScore = currentScore - 1
            if currentScore > 9:
                canvas.coords(currentScoreCanv, 147, 151.5)
            numberOfQuestionsDelay = (randint(2, 3))
            wrongFlashCard1 = flashCard1
            wrongFlashCard2 = flashCard2
            failedProblem = True
            questionsDone = 0

            
        canvas.itemconfig(currentScoreCanv, text=currentScore)
        canvas.itemconfig(correctAnswerCanv, text=correctAnswer)
        canvas.itemconfig(quizFeedbackCanv, text=quizFeedback)
        generateNewProblem()
    except:
        dontDoAnything = True
    userEntrybox.delete(0, 'end')


def startButtonPressed():
    global currentScore
    global currenthighScore
    global minutes, seconds
    global isStartButtonPressed
    global isCountDownDone
    global highscoreRAW
    highscoreRAW = open('assets/highscore.txt', 'r')
    currenthighScore = highscoreRAW.read()
    currentScore = 0
    canvas.itemconfig(currentScoreCanv, text=currentScore)
    canvas.coords(currentScoreCanv, 156.0, 151.5)
    canvas.itemconfig(highScoreCanv, text=currenthighScore)
    if int(currenthighScore) > 9:
        canvas.coords(highScoreCanv, 150.0, 238.0)
    minutes, seconds = 0, 4 #<--------------------------- Countdown Timer 
    isStartButtonPressed = True
    startButton.place(x=576, y=1006)
    isCountDownDone = False
    startCountdown()
    countDownSounds()


def startCountdown():
    global minutes, seconds
    global isCountDownDone
    global StartCountDown
    global isStartButtonPressed
    if isStartButtonPressed:
        StartCountDown = True
        isStartButtonPressed = False
    if isCountDownDone == True:
        minutes, seconds = 2, 1 #<--------------------------- Actual Timer
        startTimer()
        generateNewProblem()
    else:
        startTimer()


def countDownSounds():
    global countDownCounter
    def countDownLoop():
        global countDownCounter
        soundCountdown.play()
        countDownCounter = countDownCounter + 1
        if countDownCounter < 4:
            window.after(1000, countDownLoop)
        if countDownCounter == 4:
            soundCountdownStart.play() #<------------- This should be soundStart.play() however pygame is having a hard time differentiating these
            countDownCounter = 0  #                 audio files and is playing a sound that isnt even there.
            return()
    countDownCounter = 0
    countDownLoop()

def startTimer():
    global minutes, seconds
    global isCountDownDone 
    global StartCountDown
    if minutes == 00 and seconds == 1 and StartCountDown == True:
        StartCountDown = False
        isCountDownDone = True
        startCountdown()
        return
    if minutes == 00 and seconds == 1 and isCountDownDone == True:
        isCountDownDone = False
        timerCompleted()
        return

    if seconds == 00:
        minutes -= 1
        seconds = 60

    seconds -= 1


    canvas.itemconfig(TimerCanvas, text=f'{minutes:02}:{seconds:02}')

    window.after(1000, startTimer)


def timerCompleted():
    global flashCard1
    global flashCard2
    global currentScore
    global correctAnswer
    global startButton
    canvas.itemconfig(TimerCanvas, text='00:00')
    soundTimesup.play()
    messagebox.showinfo('Your Score', 'You Scored: ' + str(currentScore), icon='info')
    clearScreen()
    if int(currenthighScore) < int(currentScore):
        messagebox.showinfo('New High Score', 'You Got A New High Score!\nYour Score: '
         + str(currentScore) + '\nPrevious Score: ' + str(currenthighScore), icon='info')
        HighScoreTXT = open('assets/highscore.txt', 'w')
        HighScoreTXT.write(str(currentScore))
    startButton.place(x=576, y=206)

def clearScreen():
    canvas.itemconfig(highScoreCanv, text='',)
    canvas.itemconfig(currentScoreCanv, text='')
    canvas.itemconfig(quizFeedbackCanv, text='')
    canvas.itemconfig(flashCard1Canv, text='')
    canvas.itemconfig(flashCard2Canv, text='')
    canvas.itemconfig(correctAnswerCanv, text='')
    canvas.itemconfig(TimerCanvas, text='')
    userEntrybox.delete(0, 'end')
    mixer.pause()
window = Tk()

window.geometry("758x466+540+150")
window.configure(bg = "#FFFFFF")
window.title("Ezra's Math Flashcards v0.2.3.1")
window.iconbitmap(resource_path("math.ico"))


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 466,
    width = 758,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    780.0,
    466.0,
    fill="#177CD9",
    outline="")

system('cls' if name == 'nt' else 'clear')
print('Building GUI...')

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    377.7706298828125,
    242.9862060546875,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    391.0,
    219.0,
    image=image_image_2
)


image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    606.0,
    136.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    606.0,
    219.0,
    image=image_image_4
)


image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    606.0,
    315.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    393.0,
    379.0,
    image=image_image_6
)

flashCard1Canv = canvas.create_text(
    342.0,
    185.0,
    anchor="nw",
    text='',
    fill="#000000",
    font=("Helvetica", 70 * -1)
)

correctAnswerCanv = canvas.create_text(
    566.0,
    290.0,
    anchor="nw",
    text='',
    fill="#000000",
    font=("Helvetica", 45 * -1)
)

flashCard2Canv = canvas.create_text(
    342.0,
    117.0,
    anchor="nw",
    text='',
    fill="#000000",
    font=("Helvetica", 70 * -1)
)

quizFeedbackCanv = canvas.create_text(
    334.0,
    361.0,
    anchor="nw",
    text='',
    fill="#000000",
    font=("Helvetica", 32 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    396.0,
    263.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    445.0,
    237.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    369.0,
    290.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    606.0,
    219.5,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    608.0,
    137.0,
    image=image_image_11
)
TimerCanvas = canvas.create_text(
    559.0,
    114.0,
    anchor="nw",
    text='',
    fill="#000000",
    font=("Helvetica", 40 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    369.0,
    290.5,
    image=entry_image_1
)
userEntrybox = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Inter", 20 * -1),
    highlightthickness=0
)
userEntrybox.bind('<Return>', userPressedEnter)
userEntrybox.place(
    x=347.0,
    y=279.0,
    width=44.0,
    height=21.0
)

startButton_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
startButton = Button(
    image=startButton_image_1,
    borderwidth=0,
    highlightthickness=0,
    bg="#D9D9D9",
    command=startButtonPressed,
    relief="flat"
)
startButton.place(
    x=575.0,
    y=204.5,
    width=61.0,
    height=30.0
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    167.0,
    193.0,
    image=image_image_12
)

canvas.create_text(
    81.0,
    109.0,
    anchor="nw",
    text="Current Score",
    fill="#000000",
    font=("Helvetica", 27 * -1)
)

canvas.create_text(
    103.0,
    194.0,
    anchor="nw",
    text="High Score",
    fill="#000000",
    font=("Helvetica", 27 * -1)
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    165.0,
    143.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    165.0,
    228.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    165.0,
    255.0,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    165.0,
    169.0,
    image=image_image_16
)

currentScoreCanv = canvas.create_text(
    156.0,
    151.5,
    anchor="nw",
    text='',
    fill="#000000",
    font=("Helvetica", 27 * -1)
)
highScoreCanv = canvas.create_text(
    156.0, 
    238.0,
    anchor="nw",
    text='',
    fill="#000000",
    font=("Helvetica", 27 * -1)
)
system('cls' if name == 'nt' else 'clear')
print('Running...')

window.resizable(False, False)
window.mainloop()
system('cls' if name == 'nt' else 'clear')