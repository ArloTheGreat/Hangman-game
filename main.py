#--------------------VALUES-------------------
lives = 10




#------------------FUNCTIONS-----------------
import random
words = ("print", "words", "lucky", "space", "enter", "happy", "slope", "" ) 




#--------------------MAIN--------------------

print("Hello Word")

#Hangman step depending on the
if lives == 10:
    print("____________")
    print("|      |")
    print("|    ('-')")
    print("|     /|\ ")
    print("|    / | \  ")
    print("|     / \  ")
    print("|    /   \  ")
    print("|             ")
    print("|____________")
elif lives == 9:
    print("eggs")