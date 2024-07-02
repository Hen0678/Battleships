
# Battleships

[View the live project here](https://my-battleship-game-86778a82a963.herokuapp.com/)

## Overview
This classic game of Battleships is my 3rd portfolio project and focuses on the Python programming language.  

The game is played on a 6 x 6 grid. The computer will place 5 ships on random squares within the grid. The player has 10 guesses to try and sink the 5 ships. 

The game is customisable and additional ships and/or play turns can be easily amended. 

After each guess the player will be told how many missles they have left. If the player guesses a previously guessed location then a message will prompt the player to select another location.  

Player's will be notified when they hit a ship and this will also be marked with an 'x' on the game board. 

![responsive-page](assets/media/responsive_image.png)

## User Experience (UX) 

### First Time Visitors
As a user of this site, I want to: 

* Easily understand the main purpose of the game.
* Want to play a game which is quick and easy.
* I want a game that is visually appealing and fun.
* I want to be able to easily track score.

### Returning Visitors
* As a returning visitor I want to be able to be able to enjoy the same game.

### Frequent user
* I want to see if I can continue to post personal best scores.

## Features

### Main page 

* From the Python terminal press Run Program. From here you will first guess a row number (1 - 6) and then a column letter (A - F).

![main-page](assets/media/homescreen.png)

* A miss will be highlighted to the player and a 'o' symbol will appear on the game board.

![incorrect_guess](assets/media/game_screen_after_incorrect.png)

* A hit will be highlighted to the player and a 'x' symbol will appear on the game board. 

![correct_guess](assets/media/correct_guess.png)

* A message will be displayed to the player when all their missles have been used up.

![game_over](assets/media/game_over.png)

### Additional features to include 
The list of additional features to be added later include:

* Options to play a 1 vs 1 against the computer.
* A 'play again' function.
* Options to customise how many ships need to be hit to win the game.

## Technologies used
The following technologies were used for this site:

* GitPod Enterprise was used for coding the site and version control.
* GitHub as the repository for the projects code.
* Heroku was used to host the application.
* CI Python Linter validation for Python code

## Testing

###
|Features|Test Conducted|Expected Outcome|Test Outcome|
|:----|:----|:----|:----|
|Correct message displayed when missile misses ship|Miss - recalibrate your coordinates|![message](assets/media/miss_message.png)|Pass|
|Correct message displayed when missile hits ship|HIT!!!|![message](assets/media/hit_message.png)|Pass|
|Message displayed when the player guesses an already guessed square|Already guessed here - guess elsewhere|![message](assets/media/already_guessed_message.png)|Pass|
|Number of missles left|Reduces by 1|![message](assets/media/missles_left_2.png)![message](assets/media/missles_left_3.png)|Pass|
|Game over message|You are out of missles - game over!|![message](assets/media/game_over.png)|Pass|

### Code validation
|Page Tested|Screenshot of Errors|Solution Applied|Screenshot of Clear Validator Output|Test Outcome|
|:----|:----|:----|:----|:----|
|run.py|![assets/media/initial_validation_test.png](assets/media/initial_validation_test.png)|Made each amend as highlighted|![index.run.py-retest](assets/media/python_code_re-validation_test.png)|Pass|

### Bugs
|Bug|Image|Solution applied|Image|
|:----|:----|:----|:----|
|When printing the game boards the output was not as expected|![image](assets/media/game_board_error.png)|The Print statements were added directly below the print_board function. To rectify this they were added below the make_ships function|![image](assets/media/game_board_fix.png)|
|Error in the code when checking if all missles have been used up|![image](assets/media/missile_error_message.png)|The code was missing an "="|![image](assets/media/missile_error_message_fix.png)|
|No space after entering a row number and column letter|![image](assets/media/row_and_column_error.png)|There were no spaces after the row and column inputs. To rectify this a space was added|![image](assets/media/row_and_column_fix.png)|

## Deployment 
### Deploying the site
After creating the website in GitPod Enterprise, the site was deployed to Heroku to host. To deploy the project, use the following steps:
* In the GitHub repository, navigate to the Settings tab at the top of the page.
* Select Pages on the left hand side of the page
* Under "Build and deployment" there is a Source dropdown. Select Deploy from a branch and then Save.
* Once the main branch has been selected and saved, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
* The live link to the site can be found here - https://hen0678.github.io/Rock-Paper-Scissors-Lizard-Spock/

### Cloning the site

* Go to https://github.com/Hen0678/Rock-Paper-Scissors-Lizard-Spock. 
* Click the Code button. 
* Select Copy URL to Clipboard.
* Open a GitBash terminal and navigate to the directory where you want to locate the clone.
* On the command line, type "git clone" then paste in the copied URL and press the Enter key to begin the clone process.

## Credits

### Code
* Knowledge Mavens - How to Code Battleship in Python 














 
