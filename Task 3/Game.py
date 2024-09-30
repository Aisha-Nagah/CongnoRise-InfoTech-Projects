# Hanged Man game
# Aisha Nagah
import random

word_list = ['python', 'hangman', 'code', 'computer', 'developer', 'program']
def get_random_word(word_list):
    return random.choice(word_list)

def display_word_state(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def display_hangman(incorrect_guesses):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """
    ]
    return stages[incorrect_guesses]

def check_win(word, guessed_letters):
    return set(word).issubset(guessed_letters)

def play_hangman():
    print("Welcome to the Hanged Man game!")
    
    word = get_random_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6


    while incorrect_guesses < max_incorrect_guesses:

        print(display_word_state(word, guessed_letters))
        
    
        print(display_hangman(incorrect_guesses))
           
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed this letter!")
        elif guess in word:
            guessed_letters.add(guess)
            print("Guess right!")
        else:
            incorrect_guesses += 1
            print("Wrong guess!")
        

        if check_win(word, guessed_letters):
            print(f"Congrats! You won! The word is: {word}")
            break
    else:
        print(display_hangman(incorrect_guesses))
        print(f"Unfortunately, you lost! The word was: {word}")

play_hangman()