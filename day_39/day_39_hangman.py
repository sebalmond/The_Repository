import random
import os
import time

class Hangman:
    def __init__(self):
        self.word_list = [
            "cat", "dog", "sun", "hat", "car", "star", "book", "fish", 
            "ball", "tree", "bird", "cake", "frog", "bear", "duck", 
            "milk", "sing", "jump", "moon", "rose", "ship", "lion", 
            "bee", "kite", "lamp", "rain", "snow", "door", "home"
        ]
        self.MAX_TRIES = 6
        self.hangman_pics = [
            '''
                +---+
                |   |
                    |
                    |
                    |
                    |
              =========''',
            '''
                +---+
                |   |
                O   |
                    |
                    |
                    |
              =========''',
            '''
                +---+
                |   |
                O   |
                |   |
                    |
                    |
              =========''',
            '''
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
              =========''',
            '''
                +---+
                |   |
                O   |
               /|\\  |
                    |
                    |
              =========''',
            '''
                +---+
                |   |
                O   |
               /|\\  |
               /    |
                    |
              =========''',
            '''
                +---+
                |   |
                O   |
               /|\\  |
               / \\  |
                    |
              ========='''
        ]
        self.wins = 0
        self.losses = 0
    
    def clear_screen(self):
        # Clear the screen based on operating system
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_welcome(self):
        welcome_text = """
        🎮 WELCOME TO HANGMAN 🎮
        
        Try to guess the hidden word before the hangman is complete!
        You have 6 tries to guess the word.
        
        Let's play!
        """
        print(welcome_text)
        time.sleep(2)
    
    def display_stats(self):
        print(f"\nWins: {self.wins} | Losses: {self.losses}\n")
    
    def get_random_word(self):
        # Select a random word from the word list
        return random.choice(self.word_list)
    
    def display_game_state(self, secret_word, guessed_letters, tries):
        self.clear_screen()
        
        # Display the hangman picture based on wrong tries
        print(self.hangman_pics[tries])
        
        # Display the word with blanks for unguessed letters
        displayed_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        
        print("\n" + displayed_word)
        
        # Display guessed letters
        print("\nGuessed letters:", " ".join(sorted(guessed_letters)))
        
        # Display tries left
        tries_left = self.MAX_TRIES - tries
        print(f"Tries left: {tries_left}")
        
        # Display stats
        self.display_stats()
    
    def get_guess(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1:
                print("Please enter a single letter.")
            elif not guess.isalpha():
                print("Please enter a letter from A-Z.")
            else:
                return guess
    
    def play_again(self):
        return input("Play again? (yes/no): ").lower().startswith('y')
    
    def display_result(self, won, secret_word):
        if won:
            self.wins += 1
            print(f"\n🎉 Congratulations! You guessed the word: {secret_word} 🎉")
        else:
            self.losses += 1
            print(f"\n😢 Sorry! The word was: {secret_word} 😢")
        
        self.display_stats()
    
    def play_game(self):
        self.display_welcome()
        
        while True:
            secret_word = self.get_random_word()
            guessed_letters = set()
            tries = 0
            
            while tries < self.MAX_TRIES:
                self.display_game_state(secret_word, guessed_letters, tries)
                
                guess = self.get_guess()
                
                if guess in guessed_letters:
                    print(f"You've already guessed '{guess}'. Try a different letter.")
                    time.sleep(1)
                    continue
                
                guessed_letters.add(guess)
                
                if guess not in secret_word:
                    tries += 1
                    print(f"'{guess}' is not in the word.")
                    time.sleep(1)
                
                # Check if all letters are guessed
                won = all(letter in guessed_letters for letter in secret_word)
                if won:
                    self.display_game_state(secret_word, guessed_letters, tries)
                    self.display_result(True, secret_word)
                    break
            
            if tries >= self.MAX_TRIES:
                self.display_game_state(secret_word, guessed_letters, tries)
                self.display_result(False, secret_word)
            
            if not self.play_again():
                break
        
        print("Thanks for playing Hangman! Goodbye!")

if __name__ == "__main__":
    game = Hangman()
    game.play_game()