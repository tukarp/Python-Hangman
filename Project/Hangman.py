# My Hangman Game
# Made by github.com/tukarp


# Importing library
import random


# Initializing logo
LOGO = """                                                                                  
                        _  _                                                      
                       | || |__ _ _ _  __ _ _ __  __ _ _ _                        
                       | __ / _` | ' \/ _` | '  \/ _` | ' \                       
                       |_||_\__,_|_||_\__, |_|_|_\__,_|_||_|                      
                                      |___/                                       
                                                                                  """


# Hangman class
class Hangman:
    # Initialize variables and methods
    def __init__(self):
        # Game setup
        # Main variables
        self.games_won = 0      # Games won
        self.games_lost = 0     # Games lost
        self.attempts = None    # Attempts
        self.user_input = None  # User input



        # Guessing variables
        self.category = None            # Player chosen category for random guessing word
        self.word_to_guess = None       # Random word to guess from chosen category
        self.guessing_word = None       # Guessing word that changes when players guesses a letter
        self.win_check = None           # Word to compare to check if player has won
        self.guess = None               # Current player guess
        self.letters_to_swap = None     # Letters to swap in guessing word counter
        self.index = None               # Index the letter need to be swapped at in guessing word
        self.guesses_list = None        # List of players earlier guesses



        # Hangman drawing at different attempts left
        # Hangman at 8 attempts left
        self.HANGMAN_8 = """|                                                                                |
|                                                                                |
|                                                                                |
|                                                                                |
|                                                                                |
|                                                                                |
|                                                                                |
|                                  ---                                           |
[================================================================================]"""

        # Hangman at 7 attempts left
        self.HANGMAN_7 = """|                                                                                |
|                                                                                |
|                                   |                                            |
|                                   |                                            |
|                                   |                                            |
|                                   |                                            |
|                                   |                                            |
|                                  ---                                           |
[================================================================================]"""

        # Hangman at 6 attempts left
        self.HANGMAN_6 = """|                                                                                |
|                                   ----------                                   |
|                                   |        |                                   |
|                                   |                                            |
|                                   |                                            |
|                                   |                                            |
|                                   |                                            |
|                                  ---                                           |
[================================================================================]"""

        # Hangman at 5 attempts left
        self.HANGMAN_5 = """|                                                                                |
|                                   ----------                                   |
|                                   |        |                                   |
|                                   |        O                                   |
|                                   |                                            |
|                                   |                                            |
|                                   |                                            |
|                                  ---                                           |
[================================================================================]"""

        # Hangman at 4 attempts left
        self.HANGMAN_4 = """|                                                                                |
|                                   ----------                                   |
|                                   |        |                                   |
|                                   |        O                                   |
|                                   |        |                                   |
|                                   |        |                                   |
|                                   |                                            |
|                                  ---                                           |
[================================================================================]"""

        # Hangman at 3 attempts left
        self.HANGMAN_3 = """|                                                                                |
|                                   ----------                                   |
|                                   |        |                                   |
|                                   |        O                                   |
|                                   |       /|                                   |
|                                   |        |                                   |
|                                   |                                            |
|                                  ---                                           |
[================================================================================]"""

        # Hangman at 2 attempts left
        self.HANGMAN_2 = """|                                                                                |
|                                   ----------                                   |
|                                   |        |                                   |
|                                   |        O                                   |
|                                   |       /|\                                  |
|                                   |        |                                   |
|                                   |                                            |
|                                  ---                                           |
[================================================================================]"""

        # Hangman at 1 attempt left
        self.HANGMAN_1 = """|                                                                                |
|                                   ----------                                   |
|                                   |        |                                   |
|                                   |        O                                   |
|                                   |       /|\                                  |
|                                   |        |                                   |
|                                   |       /                                    |
|                                  ---                                           |
[================================================================================]"""

        # Hangman at 0 attempts left
        self.HANGMAN_0 = """|                                                                                |
|                                   ----------                                   |
|                                   |        |                                   |
|                                   |        O                                   |
|                                   |       /|\                                  |
|                                   |        |                                   |
|                                   |       / \                                  |
|                                  ---                                           |
[================================================================================]"""



        # List with hangman versions for every attempt
        self.HANGMAN_LIST = [self.HANGMAN_0, self.HANGMAN_1, self.HANGMAN_2, self.HANGMAN_3, self.HANGMAN_4,
                             self.HANGMAN_5, self.HANGMAN_6, self.HANGMAN_7, self.HANGMAN_8]



        # Guessing categories and their contents
        # Fruits guessing list
        self.FRUITS_LIST = ["banana", "strawberry", "grape", "apple", "watermelon",
                            "orange", "blueberry", "lemon", "peach", "avocado", "cherry",
                            "cantaloupe", "raspberry", "pear", "lime", "blackberry", "clementine",
                            "mango", "plum"]

        # Vegetables guessing list
        self.VEGETABLES_LIST = ["potato", "tomato", "onion", "carrot", "beetroot", "broccoli",
                                "cucumber", "salad", "lettuce", "celery", "mushroom", "corn", "garlic",
                                "spinach", "bean", "cabbage", "peas", "green onion", "cauliflower", "asparagus"]

        # Animals guessing list
        self.ANIMALS_LIST = ["cat", "dog", "rabbit", "horse", "chicken", "pig",
                             "cow", "sheep", "bird", "parrot", "frog", "spider", "bear",
                             "snake", "hamster", "monkey", "lion", "zebra", "shark", "fish"]

        # Car brands guessing list
        self.CAR_BRANDS_LIST = ["chevrolet", "honda", "nissan", "ford", "fiat", "jeep",
                                "volkswagen", "volvo", "jaguar", "audi", "toyota", "tesla", "lexus",
                                "porsche", "bugatti", "bentley", "hyundai", "bmw", "mercedes", "seat"]

        # Countries guessing list
        self.COUNTRIES_LIST = ["poland", "korea", "japan", "iceland", "england", "germany",
                            "ukraine", "france", "spain", "italy", "romania", "greece", "usa",
                            "australia",  "canada", "mexico", "brazil", "argentina", "morocco", "egypt"]

        # Categories list
        self.categories = [self.FRUITS_LIST, self.VEGETABLES_LIST, self.ANIMALS_LIST, self.CAR_BRANDS_LIST, self.COUNTRIES_LIST]



        # Printing logo
        print(LOGO)

        # Starting game
        self.menu()


    # Game menu method
    def menu(self):
        # Menu loop
        while True:
            # Printing menu
            print("[================================================================================]")
            print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Menu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
            print("|================================================================================|")
            print("| Type 'play' - to play the game                                                 |")
            print("| Type 'results' - to see the results                                            |")
            print("| Type 'exit' - to exit the program                                              |")
            print("[================================================================================]")

            # Getting user input
            self.user_input = input("| Choose an option: ")

            # Choosing programs feature
            # Case for starting the game
            if self.user_input == "play":
                # Calling game method
                self.game()
            # Case for displaying the results
            elif self.user_input == "results":
                # Calling print results method
                self.print_results()
            # Case for exiting program
            elif self.user_input == "exit":
                # Exiting program
                break
            # Case for wrong input
            else:
                # Printing error message
                print("Choose a correct option")


    # Game loop
    def game(self):
        # Player choosing a category
        self.category = self.choose_category()

        # Initializing player attempts
        self.attempts = 8

        # Initializing list of players earlier guesses
        self.guesses_list = []

        # Selecting a random word to guess from chosen category
        self.word_to_guess = random.choice(self.categories[self.category])

        # Initializing a guessing word that changes when players guesses a letter
        self.guessing_word = ((len(self.word_to_guess)) * "-")

        # Initializing word to compare to check if player has won
        self.win_check = self.word_to_guess

        # Starting game text
        print("[================================================================================]")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ H A N G M A N ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|================================================================================|")
        print(f"| # {self.attempts} attempts                                                                   |")

        # Game loop
        while self.attempts > 0:
            # Printing hangman
            self.print_hangman()

            # Printing length of the word
            print(f"| Length of the word is {len(self.guessing_word)}")

            # If list isn't empty
            if len(self.guesses_list) > 0:
                # Printing previous guesses
                print(f"| Previous guesses: {self.guesses_list}")

            # Getting correct input
            self.guess = self.get_input()

            # Checking the word
            # Case for guessing the correct letter in guessing word
            if self.guess in self.word_to_guess:
                # Checking if multiple letters needs to be swapped in guessing word
                self.letters_to_swap = self.word_to_guess.count(self.guess)

                # Swapping characters in word to guess and guessing word as many times as needed
                for i in range(self.letters_to_swap):
                    # Swapping blank in word_to_guess with guessed letter
                    self.index = self.word_to_guess.find(self.guess)  # Getting the index of word to guess to swap the letter in guessing word
                    self.word_to_guess = self.replace_string_at_index(self.word_to_guess, "-", self.index)  # Replacing guessed letter with blank in word to guess
                    self.guessing_word = self.replace_string_at_index(self.guessing_word, self.guess, self.index)  # Replacing blank with guessed letter in guessing word
            # Case for checking if player already guessed this letter
            elif self.guess in self.guesses_list:
                # Printing that player is already guessed this letter
                print("| You've already guessed this letter!")
            else:
                # Case for guessing wrong letter
                print("| That letter doesn't appear in the word!")
                # Subtract attempts after wrong guess
                self.attempts -= 1

            # Printing User interface line
            print("[================================================================================]")

            # Checking if player guessed the word
            if self.guessing_word == self.win_check:
                # Checking if player won with 1 attempt left
                if self.attempts != 1:
                    # Printing "You survived!" message for more than 1 attempt left
                    print(f"| You survived with {self.attempts} attempts left!")
                else:
                    # Printing "You survived!" message for 1 attempt left
                    print(f"| You survived with {self.attempts} attempt left!")

                # Printing guessing word message
                print(f"| You guessed the word '{self.guessing_word}'!")

                # Keeping track of games won
                self.games_won += 1

                # Breaking loop
                break

            # Displaying the amount of attempts
            # If attempts isn't equal to 1
            if self.attempts != 1:
                # Printing attempts
                print(f"| # {self.attempts} attempts                                                                   |")
            else:
                # Printing attempt
                print(f"| # {self.attempts} attempt                                                                    |")

            # Adding guessed letter to list
            self.guesses_list.append(self.guess)

        # Case for when player runs out of attempts
        else:
            # Printing hangman
            self.print_hangman()

            # Printing "You lost!" message
            print("| You lost!")

            # Printing word to guess
            print(f"| The word was '{self.win_check}'!")

            # Keeping track of results
            self.games_lost += 1


    # Player choosing category for game
    def choose_category(self):
        # Printing menu for choosing category
        print("[================================================================================]")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Choose category ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("[================================================================================]")
        print("| 1. fruits                                                                      |")
        print("| 2. vegetables                                                                  |")
        print("| 3. animals                                                                     |")
        print("| 4. car brands                                                                  |")
        print("| 5. countries                                                                   |")
        print("[================================================================================]")

        # Getting correct input loop
        while True:
            # Getting user input
            self.user_input = input("| Choose a category: ")

            # Returning numbers which will be indexes of list with categories
            # Case for fruits
            if self.user_input == "fruits" or self.user_input == "1":
                # Returning fruits index in categories list
                return 0
            # Case for vegetables
            elif self.user_input == "vegetables" or self.user_input == "2":
                # Returning vegetables index in categories list
                return 1
            # Case for animals
            elif self.user_input == "animals" or self.user_input == "3":
                # Returning animals index in categories list
                return 2
            # Case car brands
            elif self.user_input == "car brands" or self.user_input == "4":
                # Returning car brands index in categories list
                return 3
            # Case for countries
            elif self.user_input == "countries" or self.user_input == "5":
                # Returning countries index in categories list
                return 4
            # Case for wrong input
            else:
                # Printing error message
                print("| Choose a correct category")


    # Getting correct input from player
    def get_input(self):
        # Getting correct input loop
        while True:
            # Printing guessing word
            print(f"| Guessing word: [{self.guessing_word}]")

            # Getting user input
            self.user_input = input("| Input a letter: ")

            # Case for when input isn't a single letter
            if len(self.user_input) != 1:
                # Printing error message for input not being a single letter
                print("| Please, input a single letter!")
            # Case when input is single letter
            else:
                # Case for when letter isn't a lower case letter or an ASCII symbol
                if self.user_input.isupper() or not ((self.user_input >= "a") and (self.user_input <= "z")):
                    # Printing error message for symbol not being lowercase letter from the English alphabet
                    print("| Please, enter a lowercase letter from the English alphabet!")
                # Case for correct input
                else:
                    # Returning user input
                    return self.user_input


    # Printing results for multiple or single won games
    def print_results(self):
        # Printing results
        print("[================================================================================]")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Results ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|================================================================================|")

        # Case for single game won
        if self.games_won == 1:
            # Printing results for single game won
            print(f"| You won: {self.games_won} time                                                                |")
            # Case for multiple games won
        else:
            # Printing results for multiple games won
            print(f"| You won: {self.games_won} times                                                               |")

        # Printing results for single lost game
        if self.games_lost == 1:
            # Printing results for single lost game
            print(f"| You lost: {self.games_lost} time                                                               |")
        # Printing results for multiple lost game
        else:
            # Printing results for multiple lost game
            print(f"| You lost: {self.games_lost} times                                                              |")


    # Printing hangman based on current attempts
    def print_hangman(self):
        # Printing hangman
        print(self.HANGMAN_LIST[self.attempts])


    # Replacing string at given index with given character
    @staticmethod
    def replace_string_at_index(word, character, index):
        # Creating new word with replaced character
        new_word = word[:index] + character + word[index + 1:]
        # Returning new word
        return new_word


# Main function
if __name__ == "__main__":
    # Create Hangman game object
    Hangman()
