#--------------------VALUES-------------------

lives = 10




#------------------FUNCTIONS-----------------

import random
words = ("print", "words", "lucky", "space", "enter", "happy", "slope", "speed","brain","alone","cakes","dance","extra","farms","gamer","igloo","jeans","knock","laugh","messy","noble","ocean", "paint","queen", "radio", "salad", "table", "ultra", "voice", "wacky", "young", "zebra" ) 
print (random.choice(words))





#------------------FUNCTIONS-----------------

# ----- Display the used letters, the word, the filler spaces and the correct guesses.







#--------------------MAIN--------------------

print("Hello Word")

# -- Getting a random word from the 5 letter list
differentword = random.choice(words)


# - Lives - #
lives == 10


while lives > 0:

    # ----- GAME PROCESS
    while True:
        length = guess = input("Please guess a letter:")

        length = len(guess)

        if length > 1:
            print("Please guess 1 letter at a time")
        elif length == 0:
            print("Please guess a letter")

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
    print(" ")
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
#if the player has no lives left, display the end message, and ask if they want to play again.
if lives == 0:
    print ("_____end message____")
    answer = input("Would you like to play again? Yes or No"). lower()
    if answer == "Yes".lower():
    #loop back to the start(idk how rn)
    elif answer == "no".lower():
        print ("Thank you for playing.")