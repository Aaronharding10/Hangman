import random
import time

"""
Variables
"""

Correct_guessed_letters

Incorrect_guessed_letters

Random_word

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
