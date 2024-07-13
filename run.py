import random
import time

Variables
"""
correct_guessed_letters = []

incorrect_guessed_letters = []

randomly_chosen_word = ""

lives_left = 6

game_over = False
"""


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


def draw_word(randomly_chosen_word, correct_guessed_letters):
    """
    Prints the word using underscores to allow the player to take first guess.
    Uses a for loop to iterate over the random word and prints out accordingly.
    Taken from "Love sandwiches" project.
    """

    for letter in randomly_chosen_word:
        if letter in correct_guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")


def show_rules():
    """
    Displays the rules of the game when requested by the player
    """
    print("""
    ----Rules of the game----
    1. A random word will be chosen from the list of Hangman words.
    2. The player must guess the word by choosing letters.
    3. The player has 6 lives.
    Each time the player chooses an incorrect letter, they lose a life.
    4. The player can only guess 1 letter at a time.
    5. A Hangman drawing will be displayed before the player makes their guess.
    Any previously incorrectly guessed letters.
    will be available for the player to see before they make their guess.
    6. If the word is guessed correctly before all 6 lives are lost,
    player wins.
    7. If the player loses all 6 lives before guessing the word correctly,
    the player loses.
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


def get_valid_letter(correct_guessed_letters, incorrect_guessed_letters):
    """
    Function to make sure the user enters one valid letter
    """
    while True:
        letter = input("Enter letter: \n").strip().upper()

        if len(letter) != 1:
            print("Letter must be 1 character only")
        elif not letter.isalpha():
            print("Letter must be a-z")
        elif (
            letter in correct_guessed_letters or
            letter in incorrect_guessed_letters
        ):
            print(f"You have already guessed the letter '{letter}', "
                  "please try again")
        else:
            return letter


def guess_letter(randomly_chosen_word, correct_guessed_letters,
                 incorrect_guessed_letters, lives_left):
    """
    Function to check if the letter is correct or incorrect and update game
    """
    letter = get_valid_letter(correct_guessed_letters,
                              incorrect_guessed_letters)
    if letter in randomly_chosen_word:
        correct_guessed_letters.append(letter)
    else:
        incorrect_guessed_letters.append(letter)
        lives_left -= 1
    return lives_left


def check_game_over(randomly_chosen_word, correct_guessed_letters, lives_left):
    """
    Function to check and see if the player has won or lost
    by looping through the randomly chosen word
    """

    all_letters_guessed = True
    for letter in randomly_chosen_word:
        if letter not in correct_guessed_letters:
            all_letters_guessed = False
            break

    if all_letters_guessed:
        print(f"Congrats! You've guessed the word: {randomly_chosen_word}")
        return True
    elif lives_left <= 0:
        print(f"Game over! The word was: {randomly_chosen_word}")
        return True

    return False


def start_game():
    """
    Function to start the game and run game loop.
    Declares the global variables and enters a while
    loop until game over equals true
    """
    global correct_guessed_letters
    global incorrect_guessed_letters
    global randomly_chosen_word
    global lives_left
    global game_over
    correct_guessed_letters = []
    incorrect_guessed_letters = []
    randomly_chosen_word = random_word()
    lives_left = 6
    game_over = False

    while not game_over:
        draw_hangman(lives_left)
        draw_word(randomly_chosen_word, correct_guessed_letters)
        print("Incorrect guesses: ", " ".join(incorrect_guessed_letters))
    lives_left = guess_letter(
        randomly_chosen_word, correct_guessed_letters,
        incorrect_guessed_letters, lives_left)
    game_over = check_game_over(
        randomly_chosen_word, correct_guessed_letters, lives_left)


def main():
    """
    The start of the game, displays menu for player to start the game,
    view the rules or quit the game.
    """
    while True:
        print("1. Start game")
        print("2. Quit")
        print("3. Rules")
        choice = input("Please select an option to continue: \n")

        if choice == '1':
            start_game()
        elif choice == '2':
            print("Thank you for playing Hangman")
            break
        elif choice == '3':
            show_rules()
        else:
            print("Invalid selection, please try again")


if __name__ == "__main__":
    main()
