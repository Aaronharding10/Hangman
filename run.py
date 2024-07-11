import random
import time

"""
Variables
"""

correct_guessed_letters = []

incorrect_guessed_letters = []

randomly_chosen_word = ""

lives_left = 6

game_over = False



def random_word():
    """
    Will choose a random word from the list of acceptable words below
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


def draw_word(random_word, correct_guessed_letters):
    """
    Prints the word using underscores to allow the player to take their first guess.
    Uses a for loop to iterate over the random word and prints out accordingly. Taken from "Love sandwiches" project.
    """

    for letter in randomly_chosen_word:
        if letter in correct_guessed_letters:
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

def draw_hangman(lives_left):
    """
    Displays the hangman drawing based on the number of lives left
    """

    if lives_left == 6:
        print("+------------+")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 5:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 4:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 3:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           /")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 2:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 1:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")
    elif lives_left == 0:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|           /|\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")     



def get_valid_letter (correct_guessed_letters, incorrect_guessed_letters):
    """
    Function to make sure the player selects a valid letter and 1 only. It uses a while loop to make sure the input is alphabetic and 1 only.
    It also checks to see if the input has been guessed previously by checking the correct_guessed_letters and incorrect_guessed_letters.
    It will then let the player know using f strings and print, taken from "Love sandwiches" project.
    """
    while True: 
        letter = input("Enter letter: \n").strip().upper()

        if len(letter) != 1:
            print("Letter must be 1 character only")
        elif not letter.isalpha():
            print("Letter must be a-z")
        elif letter in correct_guessed_letters or letter in incorrect_guessed_letters:
            print(f"You have already guessed the letter '{letter},' please try again")
        else:
            return letter


def guess_letter(letter, randomly_chosen_word, correct_guessed_letters, incorrect_guessed_letters, lives_left):
    """
    Function to check if the entered letter is correct or incorrect and update game as a result
    """
    if letter in randomly_chosen_word:
        correct_guessed_letters.append(letter)
    else: 
        incorrect_guessed_letters.append(letter)
        lives_left -= 1
    return lives_left

def check_game_over (randomly_chosen_word, correct_guessed_letters, lives_left):
   """
   Function to check and see if the player has won or lost
   """

    game_over = False

    if lives_left <= 0:
       game_over = True
       draw_hangman(lives_left)
       print(f"You lost, the word was {randomly_chosen_word}! Better look next time")
    else:
       guessed_all_letters = True
       for letter in randomly_chosen_word:
           if letter not in correct_guessed_letters:
               guessed_all_letters = False
               break
       if guessed_all_letters:
           game_over = True
           print("Congratulations, you have won!")


def start_game():




def main():

    """
    The start of the game, displays menu for player to start the game, view the rules or quit the game. 
    """

    while True:
        print("1. Start game")
        print("2. Quit")
        print("Rules")
        choice = input("Please select an option to continue: \n")

        if choice == '1':
            start_game()
        elif choice == '2': 
            print("Thank you for playing Hangman")
            break
        elif choice == '3': 
            display_rules()
        else:
            print("Invalid selection, please try again")


