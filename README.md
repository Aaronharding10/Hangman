# Hangman

Hangman is a classic and popular online word guessing game that can be enjoyed by players of all ages. The game begins with an option to start, read the rules or quit the game.

Once the game has started, the user is prompted to guess a letter, and if they are correct, a message will indicate the correct letter placement, and the gallows and previously guessed letters will be displayed. However, if the user guesses incorrectly, they will receive an incorrect message and the gallows will be updated with a penalty, moving them one step closer to losing the game.

Overall, Hangman is a fun and challenging game that requires both guessing skills and vocabulary knowledge, making it a great way to test your abilities and have fun at the same time.

![Home Screen]

[View Hangman live project here]
- - -

## Table of Contents
### [How to play](#how-to-play-1)
### [Logic Flowchart](#logic-flowchart-1)
### [User Experience (UX)](#user-experience-ux-1)
* [User Stories](#user-stories)
### [Features](#features-1)
* [Existing Features](#existing-features)
### [Features Left to Implement](#features-left-to-implement-1)
### [Design](#design-1)
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


## Logic flowchart



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



## Features Left to Implement

* Additional words might be available via an import list.
* A difficulty system which allows the user to increase or decrease difficulty.
* Scoring system.
* Two player option.

---

## Design

* Colors
    



---

## Technologies Used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

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

![run.py linter check] 
</details>

<details>
<summary> hangman_art_words.py CI Python Linter check
</summary>


</details>




## Manual Testing



## Input validation testing

* Display rules
  

## Fixed Bugs

* 

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

### Forking the GitHub Repository
By forking the repository, we make a copy of the original repository on our GitHub account to view and change without affecting the original repository by using these steps:

1. Log in to GitHub and locate 
2. At the top of the Repository(under the main navigation) locate "Fork" button.
3. Now you should have a copy of the original repository in your GitHub account.


### Local Clone
1. Log in to GitHub and locate 
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
* 
* 

### Content

* Hangman game, all content was written by the developer.


## Acknowledgements

 * My mentor Mitko for providing helpful guidance and feedback. 
 * The code institute slack community.