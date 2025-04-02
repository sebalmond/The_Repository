ÌæÆ Children's Hangman Game ÌæÆ
	A simple, child-friendly implementation of the classic Hangman word guessing game using Python. This game features ASCII art to visualize the hangman's progress and simple word choices appropriate for children.
Ì≥ã Features

	-Child-friendly word list with simple, age-appropriate words
	-Visual ASCII art showing the hangman's progress
	-Clear and colorful interface with emoji feedback
	-Win/loss statistics tracking
	-Simple, intuitive gameplay

Ì∂ºÔ∏è Screenshots
Copy    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========

c _ k _

Guessed letters: a c e i k o

Tries left: 1

Wins: 2 | Losses: 0
Ì∫Ä How to Play

	1.Run the game with python hangman.py
	2.The game will display a hidden word with blanks
	3.Guess one letter at a time
	4.If your guess is correct, the letter will be revealed in the word
	5.If your guess is wrong, part of the hangman will be drawn
	6.Win by guessing all letters before the hangman is complete (6 wrong guesses)

Ì≤ª Requirements

	-Python 3.6 or higher
	-No external libraries required

Ì≥ù Code Structure

	-hangman.py: Main game file containing the Hangman class and game logic
Class methods:

	-__init__: Initializes game data including word list and ASCII art
	-clear_screen: Clears terminal for better visibility
	-display_welcome: Shows welcome message
	-get_random_word: Selects a random word from the list
	-display_game_state: Shows current game progress
	-get_guess: Gets and validates user input
	-play_again: Asks if the player wants to continue
	-display_result: Shows game outcome
	-play_game: Main game loop



Ì¥ß Customization
You can easily customize the game by:

	-Adding more words to the word_list in the __init__ method
	-Changing the MAX_TRIES value for difficulty adjustment
	-Modifying the ASCII art in hangman_pics

ÌøÜ Future Improvements

	-Add difficulty levels with longer words
	-Implement word categories (animals, colors, etc.)
	-Add sound effects
	-Create a graphical user interface
