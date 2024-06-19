#--------------------VALUES-------------------

lives = 10




#------------------FUNCTIONS-----------------

import random
words = ("print", "words", "lucky", "space", "enter", "happy", "slope", "" ) 





#------------------FUNCTIONS-----------------

# ----- Display the used letters, the word, the filler spaces and the correct guesses.







#--------------------MAIN--------------------

print("Hello Word")


differentword = random.choice(words)



if lives > 0:




    # ----- GAME PROCESS
    length = guess = input("Guess a letter:")

    length = len(guess)

    if length > 1 or length <= 0:
        print("No")

#Hangman step depending on the
if lives == 10:
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
elif lives == 9:
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ____________")
elif lives == 8:
    print("")
    print("|    ")
    print("|  ")
    print("|     ")
    print("|    ")
    print("|   ")
    print("|")
    print("|             ")
    print("|____________")
elif lives == 7:
    print("____________")
    print("|      ")
    print("|    ")
    print("|      ")
    print("|     ")
    print("|       ")
    print("|    ")
    print("|             ")
    print("|____________")
elif lives == 6:
    print("____________")
    print("|      |")
    print("|    ")
    print("|      ")
    print("|      ")
    print("|      ")
    print("|     ")
    print("|             ")
    print("|____________")
elif lives == 5:
    print("____________")
    print("|      |")
    print("|    ('-')")
    print("|     ")
    print("|     ")
    print("|      ")
    print("|     ")
    print("|             ")
    print("|____________")
elif lives == 4:
    print("____________")
    print("|      |")
    print("|    ('-')")
    print("|      |")
    print("|      |   ")
    print("|      ")
    print("|     ")
    print("|             ")
    print("|____________")
elif lives == 3:
    print("____________")
    print("|      |")
    print("|    ('-')")
    print("|     /| ")
    print("|    / |   ")
    print("|        ")
    print("|         ")
    print("|             ")
    print("|____________")
elif lives == 2:
    print("____________")
    print("|      |")
    print("|    ('-')")
    print("|     /|\ ")
    print("|    / | \  ")
    print("|        ")
    print("|        ")
    print("|             ")
    print("|____________")
elif lives == 1:
    print("____________")
    print("|      |")
    print("|    ('-')")
    print("|     /|\ ")
    print("|    / | \  ")
    print("|     /   ")
    print("|    /    ")
    print("|             ")
    print("|____________")
elif lives == 0:
    print("____________")
    print("|      |")
    print("|    (X-X)")
    print("|     /|\ ")
    print("|    / | \  ")
    print("|     / \  ")
    print("|    /   \  ")
    print("|             ")
    print("|____________")
