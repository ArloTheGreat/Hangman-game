#------------------LISTS-----------------


import random
words = ("print", "words", "lucky", "space", "enter", "happy", "slope", "speed","brain","alone","cakes","dance","extra","farms","gamer","igloo","jeans","knock","laugh","messy","noble","ocean", "paint","queen", "radio", "salad", "table", "ultra", "voice", "wacky", "young", "zebra" ) 
<<<<<<< HEAD
(random.choice(words))
=======
>>>>>>> 388ba3ac12b7f026daf3a474cea2006134e97c67



answer = "yes"

guessed_words = []




#------------------FUNCTIONS-----------------

# ----- Display the used letters, the word, the filler spaces and the correct guesses.





#--------------------MAIN--------------------


while answer == "yes":

# - Lives - #
    lives = 10




    # -- Getting a random word from the 5 letter list
    differentword = random.choice(words)



# --- GAME PROCESS --- #
    while lives > 0:
        while True:
            length = guess = input("Please guess a letter:")

            length = len(guess)

            try:
                int(guess)
                print("\nPlease type in a letter. There's no numbers in a word!")
            except:
                print("")
            if guess.isalpha():
                if guess in guessed_words:
                    print("You have already guessed this letter")
                elif length > 1:
                    print("Please guess 1 letter at a time\n")
                elif length == 0 or guess == " ":
                    print("You haven't guessed a letter\n")

                else:
                    guessed_words.append(guess)
                    break
        




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
        answer = input("Would you like to play again? Yes or No\n"). lower()
        if answer == "Yes":
            print("")
        #loop back to the start(idk how rn)
        elif answer == "no":
            print ("Thank you for playing.")
