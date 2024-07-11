import random
import time

"""
Variables
"""

Correct_guessed_letters

Incorrect_guessed_letters

Randomly_chosen_word = get_word

Lives_left = 6

Game_over = False



def get_word():
    """
    Will choose a random word from our list of acceptable words below
    """

    acceptable_words = [
    "Admire",
    "Wealth",
    "Posture",
    "Archive",
    "Matrix",
    "Design",
    "Candle",
    "Cast",
    "Growth",
    "Panic",
    "Youth",
    "Urge",
    "Faint",
    "Employ"
]

    random.seed(time.time())
    return random.choice(acceptable_words).upper()


def draw_word(Randomly_chosen_word, Correct_guessed_letters):
    """
    Shows correct guessed letters and underscores for letters that have yet to be guessed. 
    Uses a for loop to iterate over the word and prints out accordingly. Taken from "Love sanwiches" project.
    """

    for letter in Randomly_chosen_word:
        if letter in Correct_guessed_letters:
            print(letter, end = " ")
        else:
                print("_", end = " ")
    print("")












