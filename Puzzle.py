#Cole Law
#2018-04-20
#Bleakfalls Puzzle
# The program picks a random word from list and then "jumbles" it
# The player has to guess the correct word

import random

#sequence of words for puzzle to choose from
WORDS = ("bleak", "falls", "easy", "difficult", "enemy", "whitedraugr")

#Start of puzzle
print(
"""
           You Encounter a locked door!

   Solution: Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)

#Asks user if they want to do the puzzle
play=input("Do you want to test your wisdom? (yes or no)")
while play=="yes":
    # picks one word randomly
    word = random.choice(WORDS)
    # creates a variable to use later to check correctness
    correct = word

    # creates a jumbled version of the word
    jumble =""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
#Checks if user guesses correcttly or not.
#Offers hint if incorrect
    print("The jumble is:", jumble)
    wisdom=100
    guess = input("\nYour guess: ")
    while guess != correct and guess != "":
        print("Nothing happens.")
        hint=input("Does your small mind need a hint?")
        if hint=="yes":
            wisdom=int(wisdom)-10
            if correct=="bleak":
                print("Part of the dungeon name...")
            elif correct=="falls":
                print("Part of the dungeon name...")
            elif correct== "easy":
                print("This one is so simple!")
            elif correct=="difficult":
                print("This is a hard one... its very ________________")
            elif correct=="enemy":
                print("You fight these...")
            elif correct=="whitedraugr":
                print("Bleak Falls Barrow Boss")
            print("Such a simple puzzle yet you needed the hint...")
        guess = input("Your guess: ")
#If answered correctly then user is given their wisdom stat.(Currently not used inn game)
    if guess == correct:
        print("A latch clicks on the door and it opens!\n")
        print("Wisdom: "+str(wisdom))
        break
    elif guess== "":
        print("The lock does nothing...")
        play=input("Do you want to try again? (yes or no)")


print("Thanks for Puzzling.")

input("\n\nPress the enter key to exit.")