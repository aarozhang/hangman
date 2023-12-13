# Hangman game
import logging
import random


def get_random_word():
    f = open("words.txt", "r")
    words = f.read().split("\n")
    return random.choice(words)


def main():
    word = get_random_word()
    chances = len(word) + 2
    board = ["_"] * len(word)
    solved = False
    guessed_letters = set()

    print(f"Let's play hangman! You have {chances} chances.")
    print(" ".join(board) + "\n")

    while chances > 0 and not solved:
        try:
            user_input = str(input("Enter a letter to guess: "))
        except Exception as e:
            logging.exception(e)
            print('User input error. Please only enter a letter!')

        print('\n')
        user_input.lower()

        # Check user input
        if not user_input.isalpha():
            print('Bad input. Please enter a letter.')
            continue
        elif len(user_input) > 1:
            print("Bad input. Please enter only ONE letter.")
            continue
        elif user_input in guessed_letters:
            print("You already guessed that letter.")
            continue
        else:
            guessed_letters.add(user_input)

        # Check if letter in word
        if user_input in word:
            print('Nice guess!')
            for i in range(len(word)):
                if word[i] == user_input:
                    board[i] = word[i]
        else:
            chances -= 1
            print(f"{user_input} is not in the word.")

        # Check if solved
        if "".join(board) == word:
            print("Congrats, you solved the word!")
            print(" ".join(board) + "\n")
            solved = True
        elif chances == 0:
            print("Oops, you're out of guesses!")
            print(" ".join(board) + "\n")
        else:
            print(f"You have {chances} chance(s) left!")
            print(" ".join(board) + "\n")

    print("Thanks for playing!")


main()
