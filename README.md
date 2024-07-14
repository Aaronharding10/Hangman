# Hangman

Hangman is a classic and popular online word guessing game that can be enjoyed by players of all ages. The game begins with an option to start, read the rules or quit the game.

Once the game has started, the user is prompted to guess a letter, and if they are correct, a message will indicate the correct letter placement, and the gallows and previously guessed letters will be displayed. However, if the user guesses incorrectly, they will receive an incorrect message and the gallows will be updated with a penalty, moving them one step closer to losing the game.

Overall, Hangman is a fun and challenging game that requires both guessing skills and vocabulary knowledge, making it a great way to test your abilities and have fun at the same time.

![Home Screen](/images/home_screen.jpeg)

[View Hangman live project here](https://hangman-aaron-2f3dd915004d.herokuapp.com/)
- - -

## Table of Contents
### [How to play](#how-to-play-1)
### [Design](#design-1)
### [Logic Flowchart](#logic-flowchart-1)
### [User Experience (UX)](#user-experience-ux-1)
* [User Stories](#user-stories)
### [Features](#features-1)
* [Existing Features](#existing-features)
### [Features Left to Implement](#features-left-to-implement-1)

### [Technologies Used](#technologies-used-1)
### [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used-1)
### [Testing](#testing-1)
### [Manual Testing](#manual-testing-1)
### [Input validation testing](#input-validation-testing-1)
### [Fixed Bugs](#fixed-bugs-1)
### [Deployment](#deployment-1)
* [Deployment to Heroku](#deployment-to-heroku)
* [Forking the GitHub Repository](#forking-the-github-repository)
* [Local Clone](#local-clone)
### [Credits](#credits-1)
* [Code](#code)
* [Content](#content)
### [Acknowledgements](#acknowledgements-1)
---


## How to Play
The user has 3 options once the game is launched. 1 to start the game, 2 to quit and 3 to read the rules. Once the game starts the user will have 6 lives to try and guess the word that has been randomly selected from the list of chosen words. If the user guesses the word before all 6 lives are lost they win, if they fail to guess the word the hangman is complete and the user loses.

### Design

* A minimalistic design is used for the game.
* The gallows were created using a simple print message along with the lives left. 

## Logic flowchart

![Flowchart](/images/flowchart1.jpeg)

## User Experience (UX)


Hangman is a classic word-guessing game where players try to uncover a hidden word by suggesting letters. Correct guesses reveal the letter in the word, while incorrect guesses result in the drawing of a 'hangman' figure. The game is easy to learn and provides a good balance of challenge and reward. The goal is to guess the word before the hangman is fully drawn, providing a simple yet challenging test of word deduction skills. 



### User Stories
* First-time visitor goals
    * Read the rules and get to know the game. Get a clear understanding of the concept.
    * Once the user understands the objective they will more than likely want to play the game.
    * Fun engaging experience whilst playing the game.

* Returning visitor goals
    * Return to playing the game and possibly sharing with friends.
    * Compete with friends to see who can guess the word with the least guesses.
    * Explore any new features (if implemented).

* Frequent user goals
    * Improving their skills with speed and accuracy in guessing words.
    * Sharing the game with friends or inviting to play.
    
    
---

## Features
* The opening menu allows the user to select from a list of options such as 1.start game, 2.quit and 3.rules on how they would like to proceed.
* Word selection. The game randomly selects a word from the list of predefined words.
* Letter input. User can input their guess letter by letter to guess the hidden word.
* Incorrect guess tracking. Visually drawing a part of the hangman figure.
* Win or loss acknowledgment. Clearly advises when a a player has won or lost the game and resets back to the main menu. 
 

### Existing Features
* Intro screen
    * Displays logo and a welcome message.

![Intro screen](/images/home_screen.jpeg)    

* Display menu
    * User can choose to display rules or skip them using "y" or "n".

![Display menu](/images/testing_menu.jpeg)

* Display rules

![Display rules](/images/display_rules.jpeg)


* Promp user to make a guess

![Guess a letter](/images/guess_letter.jpeg)

* Correct Guess
    * If letter is guessed, letter is displayed within word.

![Correct guess](/images/test_correct_guess.jpeg)

* Incorrect Guess
    * If letter is not guessed, letter is listed in incorrect guesses.

![Incorrect guess](/images/test_incorrect_guess.jpeg)

* User guesses the word correctly
    * Message that confirms they have won.

![Won game](/images/test_win.jpeg)

* User is out of lives
    * Message that confirms they have lost the game.

![Lose](/images/test_gameover.jpeg)


## Features Left to Implement

* Additional words might be available via an import list.
* A difficulty system which allows the user to increase or decrease difficulty.
* Scoring system.
* Two player option.

---



---

## Technologies Used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)

---

## Frameworks, Libraries & Programs Used
* [Gitpod](https://www.gitpod.io/)
    * To write the code.
* [Github](https://github.com/)
    * Deployment of the website and storing the files online.
* [Draw.io](http://draw.io/)
    * To create a logic flowchart of the hangman game.
* [Heroku](https://www.heroku.com/)
    * To deploy the project.
* [CI Python Linter](https://pep8ci.herokuapp.com/)
    * Check code for any issues.)
   


## Testing 

CI Python Linter was used to test run.py and hangman_art_words.py

<details>
<summary> run.py CI Python Linter check
</summary>

![run.py linter check](/images/errors_linter.jpeg) 
</details>

<details>
<summary> hangman_art_words.py CI Python Linter check
</summary>

![run.py linter check](/images/linter_hangman.jpeg)
</details>




## Manual Testing

The game was manually tested extensively using the gitpod terminal and via Heroku once deployed. Testing was carried out on the menu display, rules, user input, the display of the hangman and incorrectly guessed words as well as the result of the game once the player wins or loses. 

| Feature | Expected Result | Steps Taken | Actual Result | Screenshot |
| ------- | -------------- | ----------- | ------------- | ---------- |
| Intro Screen   | To display logo and welcome message | None | As Expected | ![Intro Screen](/images/home_screen.jpeg) |
| Display Menu | To display the menu and let the user select their choice | A choice of 3 entries 1,2,3. | As Expected | ![Display menu](/images/testing_menu.jpeg) |
| Display Rules | To display rules by user selection | Select 3 via the main menu| As Expected | ![Display rules](/images/display_rules.jpeg) |
| Guess a letter   | Prompts user to guess a letter | Input a letter guess | As Expected | ![Guess a letter](/images/test_guess%20letter.jpeg)|
| Guess Correct   | To display correct, gallows with no penalty applied, a list of already guessed letters and updated hidden word | Guessed a correct letter | As Expected | ![Guess correct](/images/test_correct_guess.jpeg) |
| Guess Incorrect   | To display incorrect, gallows with penalty applied, a list of already guessed letters and updated hidden word | Guessed an incorrect letter | As Expected | ![Guess incorrect](/images/test_incorrect_guess.jpeg)|
| Guess Invalid   | To display a message saying to input a single letter | Invalid input such as e.g too many letters or a number | As Expected | ![Guess invalid](/images/test_invalid%20guess.jpeg) |
| Guessed Already   | To display a message saying guessed already | Input a letter that was already tried  | As Expected | ![Guess invalid](/images/test_guessed_already.jpeg) |
| Hangman gallows   | To display and update hangman gallows | Input a letter guess  | As Expected | ![Gallows](/images/test_gallows.jpeg) |
| Win   | To display win message | Guess the word in less than six tries | As Expected | ![Win game](/images/test_win.jpeg)|
| Lose   | To display lose message | Fail to guess the word in six tries | As Expected | ![Lose game](/images/test_gameover.jpeg) |




## Input validation testing

* Display main menu
    * Cannot continue with empty input
    * Must be one of the 3 options available

![Rules validation](/images/testing_menu.jpeg)



* Guess a letter
    * Cannot continue with empty input
    * Must be a single letter
    * Must be a letter

![Letter validation](/images/test_invalid%20guess.jpeg)

* Game over
    * Cannot continue with empty input
    * Once a game has been complete the main menu will appear to let the player choose how they would like to proceed.

![Play again validation](/images/test_menu.jpeg)
  

## Fixed Bugs

* The start_game function was amended several times once deployed to heroku to make sure all variables were inside the while loop. The game ran continuosly with no flow as per commits.
* Early on there was an issue with the game not displaying the correct guesses which was amended withih the guess_letter function to include the correctly guess letters along with the incorrectly guessed letters. 

## Deployment

### Deploying to Heroku
To deploy with Heroku, Code Institute Python Essentials Template was used so the python code can be viewed in a terminal in a browser
1. Log in to Heroku or create a new account
2. On the main page click "New" and select "Create new app"
3. Choose your unique app name and select your region
4. Click "Create app"
5. On the next page find "settings" and locate "Config Vars"
6. Click "Reveal Config Vars" and add "PORT" key and value "8000", click "Add"
7. Scroll down, locate "Buildpack" and click "Add", select "Python"
8. Repeat step 7. only this time add "Node.js", make sure "Python" is first
9. Scroll to the top and select "Deploy" tab
10. Select GitHub as deployment method and search for your repository and link them together
11. Scroll down and select either "Enable Automatic Deploys" or "Manual Deploy"
12. Deployed site [Hangman](https://hangman-aaron-2f3dd915004d.herokuapp.com/)

### Forking the GitHub Repository
By forking the repository, we make a copy of the original repository on our GitHub account to view and change without affecting the original repository by using these steps:

1. Log in to GitHub and locate [Github repository Hangman](https://github.com/Aaronharding10/Hangman)
2. At the top of the Repository(under the main navigation) locate "Fork" button.
3. Now you should have a copy of the original repository in your GitHub account.


### Local Clone
1. Log in to GitHub and locate [GitHub Repository Hangman](https://github.com/Aaronharding10/Hangman)
2. Under the repository name click "Clone or download"
3. Click on the code button, select clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone` and then paste The URL copied in the step 3.
7. Press Enter and your local clone will be created.


## Credits


### Code

* I gained understanding of python through code institute lessons.
* I gained more python knowledge through W3schools (https://www.w3schools.com/python/) 

### Content

* Hangman game, all content was written by the developer.


## Acknowledgements

 * My mentor Mitko for providing helpful guidance and feedback. 
 * The code institute slack community.