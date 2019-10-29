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
    i = 0
    for char in secret_word:
        if char in letters_guessed:
            i += 1
    if i == len(secret_word):
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ''
    for i in range(0,len(secret_word)):
        if secret_word[i] in letters_guessed:
            guessed_word += secret_word[i]
        else:
            guessed_word += '_ '
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    available_letters = ''
    for i in range(0, len(all_letters)):
        if all_letters[i] in letters_guessed:
            pass
        else:
            available_letters += all_letters[i]
    return available_letters



def validate_guess(guess, letters_guessed):
    '''
    guess: string, the user-input guess.
    letters_guessed: list (of letters), which letters have been guessed so far
    Checks whether the user input a single alphabetical character
    returns: boolean, True if a single alphabetical character supplied, False otherwise
    '''
    # check first that the input is an alpha character
    if guess.isalpha() and len(guess) == 1:
        if guess.lower() not in letters_guessed:
            return True
    else:
        return False
        


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
    print()
    print('Welcome to the game Hangman!')
    print()
    print('The rules are simple.  Guess one letter at a time.')
    print('If the letter is in the secret word, you will not lose a guess.')
    print('Guess incorrectly and you will lose a guess!')
    print('An invalid guess (non-alpha or more than one character) will result in loss of warning.')
    print('Lose all three warnings and you will start losing guesses.')
    print()
    print('I am thinking of a word that is',len(secret_word),'letters long')
    print('-'*8)
   
    # Initialize the game with 3 warnings
    num_warnings = 3
    print('You have',num_warnings,'warnings left.')
    
    # Initialize the game with 6 guesses
    num_guesses = 6
    
    # create an empty list to hold the guessed letters
    letters_guessed = []
    
    # continue to take guesses from users until either:
    # 1) secret_word is guessed, or
    # 2) the numbers of guesses runs out
    while not is_word_guessed(secret_word, letters_guessed) and num_guesses!=0:
        
        # Print a message that lets the user know how many guesses remain
        # If num_guesses == 1, then correct the output message
        if num_guesses > 1:
            print('You have',num_guesses,'guesses left.')
        else:
            print('You have',num_guesses,'guess left.')
        
        # Print a list of the remaning guessable letters
        print('Available letters:',get_available_letters(letters_guessed))
        
        # get a letter from the user
        guess = input('Please guess a letter: ')
        
        # validate the user input and check for remaining warnings
        while not validate_guess(guess, letters_guessed):
            num_warnings -= 1
            if num_warnings > 0:
                print('Oops!  That is not a valid guess.  You have',num_warnings,'warning(s) left:',
                      get_guessed_word(secret_word, letters_guessed))
            elif num_warnings == 0:
                print('You are out of warnings.  Further invalid guesses will result in loss of guess:',
                      get_guessed_word(secret_word, letters_guessed))
            else:
                num_guesses -= 1
                if num_guesses == 0:
                    return print('Oh no! You lost... better luck next time. The secret word was',secret_word)
                else:
                    print('Oops! That is not a valid guess and you are out of warnings.',
                          get_guessed_word(secret_word, letters_guessed))
            print('-'*8)
            print('You have',num_guesses,'guess(es) left.')
            print('Available letters:',get_available_letters(letters_guessed))
            guess = input('Please guess a letter: ')
        
        # guess is validated, append to letters_guessed as a lowercase letter
        letters_guessed.append(guess.lower())
        
        # test whether the guessed letter is in secret_word
        if guess in secret_word:
            print('Good guess!:',
                  get_guessed_word(secret_word, letters_guessed))
            print('-'*8)
        else:
            print('Oops! That letter is not in my word:',
                  get_guessed_word(secret_word, letters_guessed))
            # remove a guess from the user
            num_guesses -= 1
            print('-'*8)
    if is_word_guessed(secret_word, letters_guessed):
        return print('You won the game!  Your score is',num_guesses*len(secret_word))
    else:
        return print('Oh no! You lost... better luck next time. The secret word was',secret_word)



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
    pass



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
    pass



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
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
