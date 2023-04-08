# My solution to JetBrains Academy Hangman Project
# Made by github.com/tukarp


import random


# printing hangman
def print_hangman(attempts):
    # hangman at 8 attempts left
    hangman_8 = """





                   ---
    """
    # hangman at 7 attempts left
    hangman_7 = """
                    |           
                    |           
                    |           
                    |           
                    |           
                   ---          
    """
    # hangman at 6 attempts left
    hangman_6 = """
                    --------- 
                    |       | 
                    |         
                    |         
                    |         
                    |         
                   ---        
    """
    # hangman at 5 attempts left
    hangman_5 = """
                    --------- 
                    |       | 
                    |       O 
                    |         
                    |         
                    |         
                   ---
    """
    # hangman at 4 attempts left
    hangman_4 = """
                    --------- 
                    |       | 
                    |       O 
                    |       | 
                    |       | 
                    |         
                   ---
    """
    # hangman at 3 attempts left
    hangman_3 = """
                    --------- 
                    |       | 
                    |       O 
                    |      /| 
                    |       | 
                    |         
                   ---
    """
    # hangman at 2 attempts left
    hangman_2 = """
                    ---------   
                    |       |   
                    |       O   
                    |      /|\  
                    |       |   
                    |           
                   ---          
    """
    # hangman at 1 attempt left
    hangman_1 = """
                    ---------   
                    |       |   
                    |       O   
                    |      /|\  
                    |       |   
                    |      /     
                   ---          
    """
    # hangman at 0 attempts left
    hangman_0 = """
                    ---------   
                    |       |   
                    |       O   
                    |      /|\  
                    |       |   
                    |      / \     
                   ---          
    """

    # list with hangman versions for every attempt
    hangman_list = [hangman_0, hangman_1, hangman_2, hangman_3, hangman_4, hangman_5, hangman_6, hangman_7, hangman_8]
    # printing hangman
    print(hangman_list[attempts])


# player choosing category for game
def choose_category():
    print("Choose category: fruits, vegetables, animals, car_brands, countries: ")
    while True:
        user_input = input()

        # returning numbers which will be indexes of list with categories
        if user_input == "fruits":
            return 0
        elif user_input == "vegetables":
            return 1
        elif user_input == "animals":
            return 2
        elif user_input == "car_brands":
            return 3
        elif user_input == "countries":
            return 4
        else:
            print("Choose a correct category")


# game
def game():
    # game setup
    # categories and their contents
    # fruits list
    fruits = ["banana", "strawberry", "grape", "apple", "watermelon",
              "orange", "blueberry", "lemon", "peach", "avocado", "cherry",
              "cantaloupe", "raspberry", "pear", "lime", "blackberry", "clementine",
              "mango", "plum"]
    # vegetables list
    vegetables = ["potato", "tomato", "onion", "carrot", "beetroot",
                  "broccoli", "cucumber", "salad", "lettuce", "celery", "mushroom",
                  "corn", "garlic", "spinach", "bean", "cabbage", "peas", "green onion",
                  "cauliflower", "asparagus"]
    # animals list
    animals = ["cat", "dog", "rabbit", "horse", "chicken", "pig", "cow"
               "sheep", "bird", "parrot", "frog", "spider", "bear", "snake", 
               "hamster", "monkey", "lion", "zebra", "shark", "fish"]
    # car brands list
    car_brands = ["chevrolet", "honda", "nissan", "ford", "fiat", "jeep",
                  "volkswagen", "volvo", "jaguar", "audi", "toyota", "tesla", "lexus",
                  "porsche", "bugatti", "bentley", "hyundai", "bmw", "mercedes", "seat"]
    # countries list
    countries = ["poland", "korea", "japan", "iceland", "england", "germany",
                 "ukraine", "france", "spain", "italy", "romania", "greece", "australia", "usa",
                 "canada", "mexico", "brazil", "argentina", "morocco", "egypt"]
    # categories list
    categories = [fruits, vegetables, animals, car_brands, countries]
    # choosing category
    player_category = choose_category()
    # list of guessed letters
    guesses_list = []

    # keeping track of results
    global games_won
    global games_lost

    # selecting a random word
    word_to_guess = random.choice(categories[player_category])
    guessing_word = ((len(word_to_guess)) * "-")
    win_check = word_to_guess
    attempts = 8

    # starting line
    print("H A N G M A N \n")

    # game loop
    while attempts > 0:
        # checking if player guessed the word
        if guessing_word == win_check:
            print(f"You guessed the word {guessing_word}!")
            print("You survived!")
            games_won += 1
            break

        # printing hangman
        print_hangman(attempts)

        # printing length of the word
        print(f"Length of the word is {len(guessing_word)}")

        # printing previous guesses
        if len(guesses_list) > 0:
            print(f"Previous guesses: {guesses_list}")

        # getting correct input
        guess = get_input(guessing_word)

        # checking the word
        # case for guessing the correct letter
        if guess in word_to_guess:
            # checking if multiple letters needs to be swapped
            good_guesses_counter = word_to_guess.count(guess)
            for i in range(good_guesses_counter):
                # swapping blank in word_to_guess with guessed letter
                index = word_to_guess.find(guess)
                word_to_guess = replace_string_at_index(word_to_guess, "-", index)
                guessing_word = replace_string_at_index(guessing_word, guess, index)
        # case for checking if player already guessed this letter
        elif guess in guesses_list:
            print("You've already guessed this letter!")
        else:
            # case for guessing wrong letter
            print("That letter doesn't appear in the word!")
            attempts -= 1

        # displaying the amount of attempts
        if attempts != 1:
            print(f"# {attempts} attempts")
        else:
            print(f"# {attempts} attempt")

        # adding guessed letter to list
        guesses_list.append(guess)
        print()

    # case for when player runs out of attempts
    else:
        # printing hangman
        print_hangman(attempts)
        print("You lost!")
        # printing word to guess
        print(f"The word was: {win_check}")
        # keeping track of results
        games_lost += 1


# getting correct input
def get_input(guessing_word):
    while True:
        # printing guessing_word and getting input
        print(guessing_word)
        letter = input("Input a letter: ")
        # case for when input isn't a 1 letter
        if len(letter) != 1:
            print("Please, input a single letter! \n")
        else:
            # case for when letter isn't a lower case letter or an ASCII symbol
            if letter.isupper() or not ((letter >= "a") and (letter <= "z")):
                print("Please, enter a lowercase letter from the English alphabet! \n")
            else:
                return letter


# printing results
def print_results(won, lost):
    # printing results for multiple or single won games
    if won == 1:
        print(f"You won: {won} time")
    else:
        print(f"You won: {won} times")
    # printing results for multiple or single lost games
    if lost == 1:
        print(f"You lost: {lost} time")
    else:
        print(f"You lost: {lost} times")


# replacing string at index wit given character
def replace_string_at_index(word, character, index):
    new_word = word[:index] + character + word[index + 1:]
    return new_word


# starting the game
def start_hangman():
    while True:
        # printing menu
        print("Menu")
        print("Type 'play' - to play the game")
        print("Type 'results' - to see the results")
        print("Type 'exit' - to exit the program")

        # getting input
        user_input = input()

        # choosing programs feature
        # case for starting the game
        if user_input == "play":
            game()
        # case for displaying the results
        elif user_input == "results":
            print_results(games_won, games_lost)
        # case for exiting program
        elif user_input == "exit":
            break
        # case for wrong input
        else:
            print("Choose a correct option")


# main
games_won = 0
games_lost = 0
start_hangman()
