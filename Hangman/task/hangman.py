import random

import string

print("H A N G M A N")
print("")

attempts = 8

words = ["python", "java", "swift", "javascript"]

the_word = random.choice(words)

guess = len(the_word) * "-"

word_holder = []

win = 0

lost = 0


def index_finder(choice, guessing):
    indexes = []

    for i in range(len(the_word)):
        if the_word[i] == choice:
            indexes.append(i)

    for i in indexes:
        guessing = guessing[0:i] + the_word[i] + guessing[i + 1:]

    return guessing


while True:

    players_decision = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to "
                             "quit: ")

    if players_decision == "play":

        while attempts != 0:

            print(guess)
            users_choice = input("Input a letter: ")
            if len(users_choice) != 1:
                print("Please, input a single letter.")
                print("")
            elif users_choice not in string.ascii_lowercase:
                print("Please, enter a lowercase letter from the English alphabet.")
                print("")
            else:
                if users_choice in the_word and users_choice not in word_holder:
                    word_holder.append(users_choice)
                    guess = index_finder(users_choice, guess)
                    print("") if guess != the_word else None

                elif users_choice in word_holder:
                    print("You've already guessed this letter.")
                    print("")

                else:
                    word_holder.append(users_choice)
                    attempts -= 1
                    print("That letter doesn't appear in the word.")
                    print("")
                if the_word == guess:
                    print(f"You guessed the word {the_word}!\nYou survived!")
                    win += 1
                    break
                elif attempts == 0:
                    print("You lost!")
                    print("")
                    lost += 1
                else:
                    pass

        the_word = random.choice(words)
        guess = len(the_word) * "-"
        word_holder = []

    elif players_decision == "results":
        print(f"You won: {win} times.")
        print(f"You lost: {lost} times.")

    elif players_decision == "exit":
        break

    else:
        pass


