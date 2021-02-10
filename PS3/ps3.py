# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 10

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters,
    or the empty string "". You may not assume that the string will only contain
    lowercase letters, so you will have to handle uppercase and mixed case strings
    appropriately.

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

    # Convert to lower case, then for each letter in the word, refer to the values and add to a running total
    word = str.lower(word)
    component_one = 0
    for i in word:
        component_one += SCRABBLE_LETTER_VALUES[i]
    # Second part, calculating the larger of 1 or the formula 7*wordlen - 3*(n-wordlen)
    wordlen = len(word)
    scoring_formula = 7 * wordlen - 3 * (n - wordlen)
    component_two = 0
    if scoring_formula > 1:
        component_two += scoring_formula
    else:
        component_two += 1
    # Returns the product of the two components
    return component_two * component_one


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    # goes letter by letter and prints the letter in the range of the value
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')  # print all on the same line
    print()  # print an empty line


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    n = n - 1
    num_vowels = int(math.ceil(n / 3))

    wild_card = "*"
    hand[wild_card] = hand.get(wild_card, 0) + 1
    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    word = str.lower(word)
    # Creates a copy of the original hand
    new_hand = hand.copy()
    # Iterates through the letters of the word - for each letter, creates an entry in the dict
    for i in word:
        if new_hand.get(i) == 0:
            continue
        else:
            new_hand[i] = new_hand.get(i, 0) - 1
    return new_hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    # Defines two booleans, default and wildcard_exception for later use. default, by default, is True.
    # Unless there's a problem, we'll assume the word is valid.

    default = True
    wildcard_exception = False

    # Case normalize.
    word = str.lower(word)

    # Makes a copy of the hand, so we can use .get without messing with hand or word_list.
    new_hand = hand.copy()

    # Goes through the list of vowels, and subs them in for the wild card. If there's a word that works,
    # We set wildcard_exception to be true, which allows us to leave the word with a * in it, and initiate our
    # if statement below.
    for i in VOWELS:
        if word.replace('*', i) in word_list:
            wildcard_exception = True
            break
    # Checks if the word is in the word list. If it is, great, do nothing. If it's not, check if one of the
    # wildcard words is. If not, default is false.
    if word not in word_list:
        if not wildcard_exception:
            default = False
    # For each letter in the word, we're going to check if it's in the copy of our hand. if it is, we're
    # going to remove it from our new_hand. If the count of the letter we're using falls below 0, we'll know
    # that it's not a valid word. Additionally, if the letter doesn't exist in new_hand, the word is invalid,
    # and default is assigned to the value False.
    for i in word:
        if i in new_hand:
            if new_hand.get(i) > 0:
                new_hand[i] = new_hand.get(i, 0) - 1
            elif new_hand.get(i) <= 0:
                default = False
        else:
            default = False
    return default

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """

    n = 0
    for i in hand.values():
        n += i
    return n


def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:
    # Display the hand
        display_hand(hand)
    # Ask user for input
        word = input('Enter word, or "!!" to indicate that you are finished: ')
    # If the input is two exclamation points:
        if word == "!!":
    # End the game (break out of the loop)
            break
    # Otherwise (the input is not two exclamation points):
        else:
    # If the word is valid:
            if is_valid_word(word, hand, word_list):
    # Tell the user how many points the word earned,
    # and the updated total score
                total_score += get_word_score(word, calculate_handlen(hand))
                print(word, "earned", get_word_score(word, calculate_handlen(hand)), 'points!\nTotal:',
                      total_score, "points\n")
    # Otherwise (the word is not valid):
    # Reject invalid word (print a message)
            else:
                print("That is not a valid word. Please try again.\n")
    # update the user's hand by removing the letters of their inputted word
        hand = update_hand(hand, word)
    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print(f"Hand over! Total score for that round: {total_score}")
    # Return the total score as result of function
    return(total_score)
#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    # Establishes some basic, useful things. Creates a copy of hand, and establishes
    new_hand = hand.copy()
    num_to_be_added = 0
    letters_in_hand = ''
    for i in hand.keys():
        letters_in_hand += i
    # Checks if the letter to be removed is in the hand. If it is, add the number of times the letter was in the
    # dict to a running total, and remove it from the hand.
    if letter in new_hand:
        num_to_be_added += new_hand.get(letter)
        new_hand.pop(letter)

        # Creates 'alphabet,' a list of all the letters. Then, generates random letter choices. If the random
        # letter is in the original hand, just generate a new letter. If we get a letter that's not in the
        # original hand, we'll add it to our new hand, with a value equivalent to our "num to be added" count
        # from before.
        alphabet = VOWELS + CONSONANTS
        for i in range(len(alphabet)):
            new_letter = random.choice(alphabet)
            if new_letter not in letters_in_hand:
                new_hand.update({new_letter: num_to_be_added})
                break
    return new_hand


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitute option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    # Asks user for # of hands they'd like to play, and establishes total game score, and sub_avail + replay_avail
    # which we'll use to check if the user has already used a subtitution or replay.
    num_hands = int(input("How many hands would you like to play? "))
    tot_game_score = 0
    sub_avail = True
    replay_avail = True

    # We'll run this loop the number of times the user inputted, establishing a score_original and score_replay
    # at 0, we'll see why later
    for i in range(num_hands):
        score_original = 0
        score_replay = 0
        print("Current hand: ")
        # deals the user a hand
        hand = deal_hand(HAND_SIZE)
        # Checks if there's a substitution available: if there is, asks the user if they want to sub, and then
        # plays the hand.
        if sub_avail:
            display_hand(hand)
            substitute_decision = input("Would you like to substitute a letter? ")
            if substitute_decision == 'yes':
                letter = input("Enter the letter you want to substitute: ")
                hand = substitute_hand(hand, letter)
                sub_avail = False
                score_original += play_hand(hand, word_list)
        # if there's no substitution available, runs the play_hand function like normal.
        else:
            score_original += play_hand(hand, word_list)
        # at the end of the round, asks the user if they'd like to replay. If yes, just run play_hand again,
        # with the substituted hand.
        if replay_avail:
            replay_decision = input("Would you like to replay the hand? ")
            if replay_decision == 'yes':
                score_replay += play_hand(hand, word_list)
                replay_avail = False
        # checks to see which score is higher: the original, or the replayed. whichever is higher, we'll add to
        # the running total.
        if score_replay > score_original:
            tot_game_score += score_replay
        else:
            tot_game_score += score_original
        print("-" * 10)
    print(f"Total Score Over All Hands: {tot_game_score}")


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
#if __name__ == '__main__':
word_list = load_words()
play_game(word_list)

