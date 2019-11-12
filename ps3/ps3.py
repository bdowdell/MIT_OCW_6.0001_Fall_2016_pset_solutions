# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Ben Dowdell
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# Add the wildcard '*' to the SCRABBLE_LETTER_VALUES with score of 0
SCRABBLE_LETTER_VALUES['*'] = 0

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
        freq[x] = freq.get(x,0) + 1
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
    # Calculate first component of word score by summing the letter values
    sumLetters = 0
    try:
        for c in word.lower():
            sumLetters += SCRABBLE_LETTER_VALUES[c]
    except:
        print('Letter {} not in SCRABBLE_LETTER_VALUES dictionary.'.format(c))
        sumLetters = 0
    # Calculate second component of word score based on length of played word
    wordlen = len(word.lower())
    lenScore = (7 * wordlen) - 3*(n - wordlen)
    if lenScore > 1:
        score = sumLetters * lenScore
    else:
        score = sumLetters * 1
    return score

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

    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

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

    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    # add a wildcard to the hand in place of a vowel
    hand['*'] = hand.get('*', 0) +1

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
    # create a copy of the input hand
    new_hand = hand.copy()
    for c in word.lower():
        try:
            new_hand[c] -= 1
            if new_hand[c] == 0:
                del(new_hand[c])
        except:
            pass

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
    # Test first whether word is in word_list, with wildcard '*' handling
    if '*' in word.lower():
        possible_words = []
        for c in VOWELS:
            possible_words.append(word.lower()[:word.index('*')] +
                                       c + word.lower()[word.index('*')+1:])
        num_valid = 0
        for item in possible_words:
            if item in word_list:
                num_valid += 1
        if num_valid >= 1:
            in_word_list = True
        else:
            return False
    elif word.lower() in word_list:
        in_word_list = True
    else:
        return False # it doesn't matter whether the word can be built from the hand

    # Test whether word is entirely composed of letters in hand
    word_dict = get_frequency_dict(word.lower())
    for key in word_dict.keys():
        if hand.get(key,0) >= word_dict[key]:
            in_hand = True
        else:
            return False

    # Test whether both conditions are satisfied
    if in_word_list and in_hand:
        return True
    else:
        return False

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    hand_len = 0
    for i in hand.values():
        hand_len += i
    return hand_len


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
# Keep track of the total score
    total_score = 0

    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:
        # Display the hand
        print('Current Hand: ', end=' '), display_hand(hand)
        # Ask user for input
        player_word = input('Enter a word, or "!!" to indicate that you are finished: ')

        # If the input is two exclamation points:
        if player_word == '!!':
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(player_word, hand, word_list):
                # Tell the user how many points the word earned,
                # and the updated total score
                n = calculate_handlen(hand)
                word_score = get_word_score(player_word, n)
                total_score += word_score
                print('"{}" earned {} points.  Total: {} points'.format(
                        player_word, word_score, total_score))
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print('That is not a valid word.  Please choose another word.')
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, player_word)
            print() # separator line
    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print() # add an empty line
    if calculate_handlen(hand) == 0:
        print('Ran out of letters.  Total score for hand: {} points'.format(
                total_score))
        print('-'*60)
    else: # user must have entered '!!'
        print('Game terminated by user.  Total score for hand: {} points'.format(
                total_score))
        print('-'*60)
    # Return the total score as result of function
    return total_score



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
    # Start by defining the pool of letters from which to randomly select
    # Remove all letters in hand so that regardless of user choice,
    # none of the origional hand letters can be re-selected
    full_list = list(VOWELS + CONSONANTS)
    keys = hand.keys()
    swap_list = [c for c in full_list if c not in keys]
    swap_str = ''.join(swap_list)

    # randomly select the new letter from the filtered pool of letters
    x = random.choice(swap_str)

    # copy hand
    subbed_hand = hand.copy()

    # replace the user selected letter in hand with the random selection
    subbed_hand[x] = subbed_hand[letter]
    del(subbed_hand[letter])

    return subbed_hand


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
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

    # initialize game_score to track score across hands
    game_score = 0

    # Only one substitution per game can be made
    subs_remaining = 1

    # Only one hand per game may be replayed
    replays_remaining = 1

    def _get_num_hands():
        """Ask the user to input the number of hands to play
        returns a string"""
        return input('Enter total number of hands: ')

    def _verify_num_hands(num_hands):
        """Verify whether num_hands is a valid value
        Returns bool"""
        try:
            if len(num_hands) == 1 and type(int(num_hands)) == int:
                return True
            else:
                raise ValueError
        except:
            return False

    def _ask_for_substitution():
        """Ask the user if they want to substitute a letter
        Returns a string"""
        return input('Would you like to substitute a letter (yes/no)? ')

    def _verify_substitution_input(subs_choice):
        """Verify whether subs_choice is a valid value
        Returns bool"""
        try:
            if subs_choice.lower() == 'yes' or subs_choice.lower() == 'no':
                return True
            else:
                raise ValueError
        except:
            return False

    def _get_sub_letter():
        """Ask the user what letter to substitute
        Returns a string"""
        return input('Which letter would you like to replace? ')

    def _verify_sub_letter(sub_letter):
        """Validate that input letter is alpha and single
        Returns a bool"""
        try:
            if sub_letter.lower().isalpha() and len(sub_letter.lower()) == 1:
                return True
            else:
                raise ValueError
        except:
            return False

    def _check_subs_remaining(subs_left):
        """Assumes subs_left is an integer
        Returns a bool"""
        if subs_left == 1:
            return True
        else:
            return False

    def _check_replays_remaining(replays_left):
        """Assumes replays_left is an integer
        Returns a bool"""
        if replays_left == 1:
            return True
        else:
            return False

    # Get the number of hands to play from the user & verify the input
    num_hands = _get_num_hands()
    print()
    while True:
        if _verify_num_hands(num_hands):
            num_hands = int(num_hands)
            break
        else:
            print('Invalid entry for number of hands.')
            num_hands = _get_num_hands()

    # Continue play until all hands dealt
    while num_hands > 0:
        # Deal the initial hand
        hand = deal_hand(HAND_SIZE)
        # Ask whether the player wants to substitute a letter
        if _check_subs_remaining(subs_remaining):
            # Display the initial hand
            print('Current hand: ', end=' '), display_hand(hand)
            subs_choice = _ask_for_substitution()
            while True:
                if _verify_substitution_input(subs_choice):
                    if subs_choice.lower() == 'yes':
                        sub_letter = _get_sub_letter()
                        while True:
                            if _verify_sub_letter(sub_letter):
                                hand = substitute_hand(hand, sub_letter.lower())
                                subs_remaining = 0
                                break
                            else:
                                print('Invalid entry for subbed letter.')
                                sub_letter = _get_sub_letter()
                        break # _verify_substitution_input loop
                    elif subs_choice.lower() == 'no':
                        break
                else:
                    print('Invalid entry for substitution.  Should be yes or no')
                    subs_choice = _ask_for_substitution()
        print() # blank line
        # play hand until no letters left or user terminates
        hand_score = play_hand(hand, word_list)
        game_score += hand_score
        num_hands -= 1
    return print('Game over!  Final score: {} points'.format(game_score))


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
