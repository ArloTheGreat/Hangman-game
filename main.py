#------------------LISTS-----------------


import random

words = ("print", "words", "lucky", "space", "exits", "fetch", 
         "slope", "plain","brain","alone","cakes","dance","extra","farms","gamer","froze",
         "jeans","bangs","laugh","mudge","noble","ocean", "paint","kings", "radio", "crane", "table", "ultra", "voice", "wacky", "young", "zebra" ) 


(random.choice(words))





answer = "yes"






#------------------FUNCTIONS-----------------

# ----- Display the used letters, the word, the filler spaces and the correct guesses.


#--------------------MAIN--------------------



#_____Introduction to the game-----
def intro():
    name = input("Whats your name?")
    print("\nHaiii, Walcome to the game,",name)
    print("This game about hangman")
    print("Here is how you play hangman:")
    print("The participants playing have 10 chances to guess a random 5 letter word.\n")
    print("I hope you have fun!\n")


while answer == "yes":
 


    # - Values - #


 # - Lives - #

    lives = 10
    placehold_score = 0
    guessed_words = []
    actual_word = []

    # -- Getting a random word from the 5 letter list -- #
    differentword = random.choice(words)
    actual_word.append(differentword)
    lettered = list(actual_word[0])
    placeholder = "_" * len(differentword) 
    placeholdlist = list(placeholder)

    print(*actual_word)





# --- GAME PROCESS --- #
    intro()

    while lives > 0:
        while True:


            print(*placeholdlist)

            guess = input("Please guess a letter:").lower()


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
            
        print("You have guessed: ",*guessed_words, "\n")
        if guess in differentword:
            print("Correct! That is in the word")
            placehold_score += 1
            for i in range(len(differentword)):
                if differentword[i] == guess:
                    placeholdlist[i] = guess
        elif guess not in differentword:
            lives -= 1
            print("Incorrect, you got this! Try again\n")
    
#Hangman step depending on the
#we need to check placeholder score if this is nonzero the user has just won the game and we shouldnt output the hangman
        if placehold_score == 5:

            print("Yay! Good job you won the game.")

            answer = input("Would you like to play again? Yes or No\n"). lower()
            if answer == "yes":
                print("")
            elif answer == "no":
                print ("Thank you for playing.")
                break


        if lives == 9:
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
            print("|____________")
        elif lives == 7:
            print("____________")
            print("|      ")
            print("|    ")
            print("|      ")
            print("|     ")
            print("|       ")
            print("|             ")
            print("|____________")
        elif lives == 6:
            print("____________")
            print("|      |")
            print("|    ")
            print("|      ")
            print("|      ")
            print("|      ")
            print("|             ")
            print("|____________")
        elif lives == 5:
            print("____________")
            print("|      |")
            print("|    ('-')")
            print("|     ")
            print("|     ")
            print("|      ")
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
            print("|____________")
        elif lives == 3:
            print("____________")
            print("|      |")
            print("|    ('-')")
            print("|     /| ")
            print("|    / |   ")
            print("|        ")
            print("|         ")
            print("|____________")
        elif lives == 2:
            print("____________")
            print("|      |")
            print("|    ('-')")
            print("|     /|\ ")
            print("|    / | \  ")
            print("|        ")
            print("|        ")
            print("|____________")
        elif lives == 1:
            print("____________")
            print("|      |")
            print("|    ('-')")
            print("|     /|\ ")
            print("|    / | \  ")
            print("|     /   ")
            print("|    /    ")
            print("|____________")
        elif lives == 0:
            print("____________")
            print("|      |")
            print("|    (X-X)")
            print("|     /|\ ")
            print("|    / | \  ")
            print("|     / \  ")
            print("|    /   \  ")
            print("|____________")
    #if the player has no lives left, display the end message, and ask if they want to play again.
        if lives == 0:
            print("Hello player, you lost in this game.")
            print("Why can you lose in this game?")
            print("Would you like to find a solution?")
            print("There are still many games that you haven't won, try another time!!!")
            print("The game is over, remember your defeat")
            answer = input("Would you like to play again? Yes or No\n"). lower()
            if answer == "yes":
                print("")
            #loop back to the start(idk how rn)
            elif answer == "no":
                print ("Thank you for playing.")
                break
        