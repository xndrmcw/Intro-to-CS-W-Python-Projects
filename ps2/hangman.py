# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    count = 0
    success = False
    for i in secret_word:
        if i not in letters_guessed:
            success = False
            break
        else:
            success = True
    return success




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    empty_word = ''
    for i in secret_word:
        if i in letters_guessed:
            empty_word += i
        else:
            empty_word += '_ '
    return empty_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    new_alphabet = ''
    for i in alphabet:
        if i not in letters_guessed:
            new_alphabet += i
    return new_alphabet


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = ''
    length_word = len(secret_word)
    guesses_left = 6
    warnings = 3
    vowels = 'a', 'e', 'i', 'o', 'u'
    print("Welcome to the game Hangman!\n"
          "I am thinking of a word that is", length_word, 'letters long.')
    print("You have", warnings, 'warnings left.')
    print('-'*10)
    print("You have", guesses_left, 'guesses left.')
    print("Available letters:", get_available_letters(letters_guessed))
    while not is_word_guessed(secret_word, letters_guessed):
        if guesses_left <= 0:
            print("You're out of guesses! Better luck next time.")
            print("The word was:", secret_word)
            break
        user_guess = str.lower(input("Guess a letter: "))
        if not str.isalpha(user_guess):
            warnings -= 1
            if warnings >= 0:
                print("That's not a valid input! You have", warnings, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed), "\n" + "-"*10)
            else:
                print("That's not a valid input! You have 0 warnings left:",
                      get_guessed_word(secret_word, letters_guessed), "\n" + "-"*10)
                guesses_left -= 1
        elif user_guess in letters_guessed:
            warnings -= 1
            if warnings >= 0:
                print("You already guessed that letter! You have", warnings, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed), "\n" + "-" * 10)
            else:
                print("You already guessed that letter! You have 0 warnings left:",
                      get_guessed_word(secret_word, letters_guessed), "\n" + "-" * 10)
                guesses_left -= 1
        else:
            letters_guessed += user_guess
            if user_guess in secret_word:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            elif user_guess not in secret_word and user_guess in vowels:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                guesses_left -= 2
            elif user_guess not in secret_word and user_guess not in vowels:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                guesses_left -= 1
            print("You have", guesses_left, 'guesses left.')
            print("Available letters:", get_available_letters(letters_guessed))
            print("-"*10)
    if is_word_guessed(secret_word, letters_guessed):
        score = guesses_left * length_word
        print("Congratulations! You won.\n"
              "Your total score for this game was:", score)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # if guessed letters of my_words match other_word, return True
    word_match = False
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word[i] == other_word[i]:
            word_match = True
        elif my_word[i] == "_":
            continue
        else:
            word_match = False
            break
    return word_match


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ', '')
    # iterate through wordlist to find words that have the same letters that we've guessed in myword
    matches = []
    num_underscores = 0
    for i in my_word:
        if not i.isalpha():
            num_underscores += 1
    len_word_no_underscores = len(my_word) - num_underscores
    num_matches = 0
    for i in wordlist:
        if len(i) == len(my_word):
            for j in range(0, len(i)):
                if i[j] == my_word[j]:
                    num_matches += 1
                    if num_matches == len_word_no_underscores:
                        matches.append(i)
                        num_matches = 0
                    continue
                elif my_word[j] == "_":
                    continue
                else:
                    num_matches = 0
    if not matches:
        print("There aren't any matches!")
    print(matches)


show_possible_matches("a_ pl_ ")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = ''
    length_word = len(secret_word)
    guesses_left = 6
    warnings = 3
    vowels = 'a', 'e', 'i', 'o', 'u'
    print("Welcome to the game Hangman!\n"
          "I am thinking of a word that is", length_word, 'letters long.')
    print("You have", warnings, 'warnings left.')
    print('-' * 10)
    print("You have", guesses_left, 'guesses left.')
    print("Available letters:", get_available_letters(letters_guessed))
    while not is_word_guessed(secret_word, letters_guessed):
        if guesses_left <= 0:
            print("You're out of guesses! Better luck next time.")
            print("The word was:", secret_word)
            break
        user_guess = str.lower(input("Guess a letter: "))
        if not str.isalpha(user_guess):
            if user_guess == "*":
                empty_word = get_guessed_word(secret_word,letters_guessed)
                show_possible_matches(empty_word)
            else:
                warnings -= 1
                if warnings >= 0:
                    print("That's not a valid input! You have", warnings, "warnings left:",
                          get_guessed_word(secret_word, letters_guessed), "\n" + "-" * 10)
                else:
                    print("That's not a valid input! You have 0 warnings left:",
                          get_guessed_word(secret_word, letters_guessed), "\n" + "-" * 10)
                    guesses_left -= 1
        elif user_guess in letters_guessed:
            if user_guess == "*":
                empty_word = get_guessed_word(secret_word, letters_guessed)
                show_possible_matches(empty_word)
            else:
                warnings -= 1
                if warnings >= 0:
                    print("You already guessed that letter! You have", warnings, "warnings left:",
                          get_guessed_word(secret_word, letters_guessed), "\n" + "-" * 10)
                else:
                    print("You already guessed that letter! You have 0 warnings left:",
                          get_guessed_word(secret_word, letters_guessed), "\n" + "-" * 10)
                    guesses_left -= 1
        else:
            letters_guessed += user_guess
            if user_guess in secret_word:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            elif user_guess not in secret_word and user_guess in vowels:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                guesses_left -= 2
            elif user_guess not in secret_word and user_guess not in vowels:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                guesses_left -= 1
            print("You have", guesses_left, 'guesses left.')
            print("Available letters:", get_available_letters(letters_guessed))
            print("-" * 10)
    if is_word_guessed(secret_word, letters_guessed):
        score = guesses_left * length_word
        print("Congratulations! You won.\n"
              "Your total score for this game was:", score)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
#     # pass
#
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
