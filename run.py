import random
import time

"""
Variables
"""

Correct_guessed_letters = []

Incorrect_guessed_letters = []

Randomly_chosen_word = ""

Lives_left = 6

Game_over = False



def choose_word():
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


def draw_word(chosen_word, Correct_guessed_letters):
    """
    Shows correct guessed letters and underscores for letters that have yet to be guessed. 
    Uses a for loop to iterate over the word and prints out accordingly. Taken from "Love sandwiches" project.
    """

    for letter in Randomly_chosen_word:
        if letter in Correct_guessed_letters:
            print(letter, end = " ")
        else:
                print("_", end = " ")
    print("")


def show_rules():
    """
    Displays the rules of the game when requested by the player
    """
    print("""
    ----Rules of the game----
    1. A random word will be chosen from the list of Hangman words.
    2. The player must guess the word by choosing letters.
    3. The player has 6 lives and each time the player chooses an incorrect letter, they lose a life. 
    4. The player can only guess 1 letter at a time.
    5. A Hangman drawing will be displayed before the player makes their guess. Any previously incorrectly guessed letters
    will be available for the player to see before they make their guess. 
    6. If the word is guessed correctly before all 6 lives are lost, the player wins. 
    7. If the player loses all 6 lives before guessing the word correctly, the player loses. 
    """)

def draw_hangman(Lives_left):
    """
    Displays the hangman drawing based on the number of lives left
    """

    if Lives_left == 6:
        print("+------------+")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif Lives_left == 5:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif Lives_left == 4:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif Lives_left == 3:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           /")
        print("|")
        print("|")
        print("+-------+")
    elif Lives_left == 2:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")
    elif Lives_left == 1:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")
    elif Lives_left == 0:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|           /|\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")     













