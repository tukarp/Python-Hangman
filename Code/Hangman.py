# My Hangman Game
# Made by github.com/tukarp


# importing library
import random


# Hangman class
class Hangman:
    # initialize variables and methods
    def __init__(self):
        # game setup
        # main variables
        self.games_won = 0      # games won
        self.games_lost = 0     # games lost
        self.attempts = None    # attempts
        self.user_input = None  # user input



        # guessing variables
        self.category = None            # player chosen category for random guessing_word
        self.word_to_guess = None       # random word to guess from chosen category
        self.guessing_word = None       # guessing_word that changes when players guesses a letter
        self.win_check = None           # word to compare to check if player has won
        self.guess = None               # current player guess
        self.letters_to_swap = None     # letters to swap in guessing_word counter
        self.index = None               # index the letter need to be swapped at in guessing_word
        self.guesses_list = None        # list of players earlier guesses



        # hangman drawing at different attempts left
        # hangman at 8 attempts left
        self.HANGMAN_8 = """





                               ---
                """

        # hangman at 7 attempts left
        self.HANGMAN_7 = """
                                |           
                                |           
                                |           
                                |           
                                |           
                               ---          
                """

        # hangman at 6 attempts left
        self.HANGMAN_6 = """
                                --------- 
                                |       | 
                                |         
                                |         
                                |         
                                |         
                               ---        
                """

        # hangman at 5 attempts left
        self.HANGMAN_5 = """
                                --------- 
                                |       | 
                                |       O 
                                |         
                                |         
                                |         
                               ---
                """

        # hangman at 4 attempts left
        self.HANGMAN_4 = """
                                --------- 
                                |       | 
                                |       O 
                                |       | 
                                |       | 
                                |         
                               ---
                """

        # hangman at 3 attempts left
        self.HANGMAN_3 = """
                                --------- 
                                |       | 
                                |       O 
                                |      /| 
                                |       | 
                                |         
                               ---
                """

        # hangman at 2 attempts left
        self.HANGMAN_2 = """
                                ---------   
                                |       |   
                                |       O   
                                |      /|\  
                                |       |   
                                |           
                               ---          
                """

        # hangman at 1 attempt left
        self.HANGMAN_1 = """
                                ---------   
                                |       |   
                                |       O   
                                |      /|\  
                                |       |   
                                |      /     
                               ---          
                """

        # hangman at 0 attempts left
        self.HANGMAN_0 = """
                                ---------   
                                |       |   
                                |       O   
                                |      /|\  
                                |       |   
                                |      / \     
                               ---          
                """

        # list with hangman versions for every attempt
        self.HANGMAN_LIST = [self.HANGMAN_0, self.HANGMAN_1, self.HANGMAN_2, self.HANGMAN_3, self.HANGMAN_4,
                             self.HANGMAN_5, self.HANGMAN_6, self.HANGMAN_7, self.HANGMAN_8]



        # guessing categories and their contents
        # fruits guessing list
        self.FRUITS_LIST = ["banana", "strawberry", "grape", "apple", "watermelon",
                            "orange", "blueberry", "lemon", "peach", "avocado", "cherry",
                            "cantaloupe", "raspberry", "pear", "lime", "blackberry", "clementine",
                            "mango", "plum"]

        # vegetables guessing list
        self.VEGETABLES_LIST = ["potato", "tomato", "onion", "carrot", "beetroot", "broccoli",
                                "cucumber", "salad", "lettuce", "celery", "mushroom", "corn", "garlic",
                                "spinach", "bean", "cabbage", "peas", "green onion", "cauliflower", "asparagus"]

        # animals guessing list
        self.ANIMALS_LIST = ["cat", "dog", "rabbit", "horse", "chicken", "pig",
                             "cow", "sheep", "bird", "parrot", "frog", "spider", "bear",
                             "snake", "hamster", "monkey", "lion", "zebra", "shark", "fish"]

        # car brands guessing list
        self.CAR_BRANDS_LIST = ["chevrolet", "honda", "nissan", "ford", "fiat", "jeep",
                                "volkswagen", "volvo", "jaguar", "audi", "toyota", "tesla", "lexus",
                                "porsche", "bugatti", "bentley", "hyundai", "bmw", "mercedes", "seat"]

        # countries guessing list
        self.COUNTRIES_LIST = ["poland", "korea", "japan", "iceland", "england", "germany",
                            "ukraine", "france", "spain", "italy", "romania", "greece", "usa",
                            "australia",  "canada", "mexico", "brazil", "argentina", "morocco", "egypt"]

        # categories list
        self.categories = [self.FRUITS_LIST, self.VEGETABLES_LIST, self.ANIMALS_LIST, self.CAR_BRANDS_LIST, self.COUNTRIES_LIST]



        # starting game
        self.menu()


    # game menu method
    def menu(self):
        # menu loop
        while True:
            # printing menu
            print("Menu")
            print("Type 'play' - to play the game")
            print("Type 'results' - to see the results")
            print("Type 'exit' - to exit the program")

            # getting user input
            self.user_input = input()

            # choosing programs feature
            # case for starting the game
            if self.user_input == "play":
                self.game()
            # case for displaying the results
            elif self.user_input == "results":
                self.print_results()
            # case for exiting program
            elif self.user_input == "exit":
                break
            # case for wrong input
            else:
                print("Choose a correct option")


    # game loop
    def game(self):
        # player choosing a category
        self.category = self.choose_category()

        # initializing player attempts
        self.attempts = 8

        # initializing list of players earlier guesses
        self.guesses_list = []

        # selecting a random word to guess from chosen category
        self.word_to_guess = random.choice(self.categories[self.category])

        # initializing a guessing_word that changes when players guesses a letter
        self.guessing_word = ((len(self.word_to_guess)) * "-")

        # initializing word to compare to check if player has won
        self.win_check = self.word_to_guess

        # starting game text
        print("H A N G M A N")
        print(f"# {self.attempts} attempts")

        # game loop
        while self.attempts > 0:
            # checking if player guessed the word
            if self.guessing_word == self.win_check:
                # printing guessing_word message
                print(f"You guessed the word {self.guessing_word}!")

                # printing "You survived!" message
                print("You survived!")

                # keeping track of games won
                self.games_won += 1

                # breaking loop
                break

            # printing hangman
            self.print_hangman()

            # printing length of the word
            print(f"Length of the word is {len(self.guessing_word)}")

            # if list isn't empty
            if len(self.guesses_list) > 0:
                # printing previous guesses
                print(f"Previous guesses: {self.guesses_list}")

            # getting correct input
            self.guess = self.get_input()

            # checking the word
            # case for guessing the correct letter in guessing_word
            if self.guess in self.word_to_guess:
                # checking if multiple letters needs to be swapped in guessing_word
                self.letters_to_swap = self.word_to_guess.count(self.guess)

                # swapping characters in word_to_guess and guessing_word as many times as needed
                for i in range(self.letters_to_swap):
                    # swapping blank in word_to_guess with guessed letter
                    self.index = self.word_to_guess.find(self.guess)  # getting the index of word_to_guess to swap the letter in guessing_word
                    self.word_to_guess = self.replace_string_at_index(self.word_to_guess, "-", self.index)  # replacing guessed letter with blank in word_to_guess
                    self.guessing_word = self.replace_string_at_index(self.guessing_word, self.guess, self.index)  # replacing blank with guessed letter in guessing_word
            # case for checking if player already guessed this letter
            elif self.guess in self.guesses_list:
                # printing that player is already guessed this letter
                print("You've already guessed this letter!")
            else:
                # case for guessing wrong letter
                print("That letter doesn't appear in the word!")
                # subtract attempts after wrong guess
                self.attempts -= 1

            # displaying the amount of attempts
            # if attempts isn't equal to 1
            if self.attempts != 1:
                print(f"# {self.attempts} attempts")
            else:
                print(f"# {self.attempts} attempt")

            # adding guessed letter to list
            self.guesses_list.append(self.guess)

        # case for when player runs out of attempts
        else:
            # printing hangman
            self.print_hangman()

            # printing "You lost!" message
            print("You lost!")

            # printing word to guess
            print(f"The word was: {self.win_check}")

            # keeping track of results
            self.games_lost += 1


    # player choosing category for game
    def choose_category(self):
        # printing available categories
        print(f"Choose category: fruits, vegetables, animals, car_brands, countries: ")

        # getting correct input loop
        while True:
            # getting user input
            self.user_input = input()

            # returning numbers which will be indexes of list with categories
            # case for fruits
            if self.user_input == "fruits":
                return 0
            # case for vegetables
            elif self.user_input == "vegetables":
                return 1
            # case for animals
            elif self.user_input == "animals":
                return 2
            # case car_brands
            elif self.user_input == "car_brands":
                return 3
            # case for countries
            elif self.user_input == "countries":
                return 4
            # case for wrong input
            else:
                print("Choose a correct category")


    # getting correct input from player
    def get_input(self):
        # getting correct input loop
        while True:
            # printing guessing_word
            print(self.guessing_word)

            # getting user input
            self.user_input = input("Input a letter: ")

            # case for when input isn't a single letter
            if len(self.user_input) != 1:
                print("Please, input a single letter! \n")
            # case when input is single letter
            else:
                # case for when letter isn't a lower case letter or an ASCII symbol
                if self.user_input.isupper() or not ((self.user_input >= "a") and (self.user_input <= "z")):
                    print("Please, enter a lowercase letter from the English alphabet! \n")
                # case for correct input
                else:
                    return self.user_input


    # printing results for multiple or single won games
    def print_results(self):
        # case for single game won
        if self.games_won == 1:
            print(f"You won: {self.games_won} time")
        # case for multiple games won
        else:
            print(f"You won: {self.games_won} times")

        # printing results for single lost game
        if self.games_lost == 1:
            print(f"You lost: {self.games_lost} time")
        # printing results for multiple lost game
        else:
            print(f"You lost: {self.games_lost} times")


    # replacing string at given index with given character
    @staticmethod
    def replace_string_at_index(word, character, index):
        new_word = word[:index] + character + word[index + 1:]
        return new_word


    # printing hangman based on current attempts
    def print_hangman(self):
        # printing hangman
        print(self.HANGMAN_LIST[self.attempts])


# main function
def main():
    Hangman()


# main
if __name__ == "__main__":
    main()
