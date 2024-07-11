import random
import time


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
