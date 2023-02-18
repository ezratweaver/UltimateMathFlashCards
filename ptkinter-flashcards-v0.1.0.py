#randomly generated multiplication flash cards 
import random   #imports ability to call random intgers
import os       #imports operating system commands to clear the screen
import time     #imports time library for delay between feedback and next problem
e = 'error'     #defines 'E" as 'error' to call for later 

os.system('cls' if os.name == 'nt' else 'clear')                        #clears the screen

try:                                                                    #creates safety net for when the user trys to input a string and not an integer
    while True:
        RandomNumberOne = (random.randint(1, 15))                               #code that defines random numbers for beginning of the loop
        RandomNumberTwo = (random.randint(1, 15))

        print('  ' + str(RandomNumberOne))                                      #displays in presentable form the multiplication problem
        print('x ' + str(RandomNumberTwo))
    
        UserInputAnswer = (input('>'))                                           #asks user for input
        if UserInputAnswer == "quit":                                            #if the user says quit, breaks the loop and kills the program
            break

        FinishedMath = int(RandomNumberOne) * int(RandomNumberTwo)                              #after using the numbers as a string, defines them as an integer and calculates the answer
        if int(UserInputAnswer) == FinishedMath :                                        #if the math is correct continue
            os.system('cls' if os.name == 'nt' else 'clear')            #clear screen
            print("Correct! The answer is", str(FinishedMath))                                           #display feedback
            time.sleep(0.9)                                             #gives time for user to read feeback
            os.system('cls' if os.name == 'nt' else 'clear')            #clears screen
        else:                                                           #if the answer is not quit or the correct answer, excute this
            os.system('cls' if os.name == 'nt' else 'clear')            #clears screen
            print("Incorrect. The answer was", str(FinishedMath))                                          #displays feedback
            time.sleep(0.9)                                             #allows user to view feedback
            os.system('cls' if os.name == 'nt' else 'clear')            #clears screen
except ValueError as E:                                                 #if the user inputs something that is not an interger, displays an error program and kills the program
    print(e)                                                            #displays error message

