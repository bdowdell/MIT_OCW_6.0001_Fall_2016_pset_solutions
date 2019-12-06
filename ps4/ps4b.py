# Problem Set 4B
# Name: Ben Dowdell
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        self.shift_dict = dict()
        for i in range(0, len(string.ascii_lowercase)):
            key = string.ascii_lowercase[i]
            if i + shift < len(string.ascii_lowercase):
                self.shift_dict[key] = self.shift_dict.get(
                        key,
                        string.ascii_lowercase[i + shift])
            else:
                self.shift_dict[key] = self.shift_dict.get(
                        key,
                        string.ascii_lowercase[i + shift
                                               - len(string.ascii_lowercase)])

        for i in range(0, len(string.ascii_uppercase)):
            key = string.ascii_uppercase[i]
            if i + shift < len(string.ascii_uppercase):
                self.shift_dict[key] = self.shift_dict.get(
                        key,
                        string.ascii_uppercase[i + shift])
            else:
                self.shift_dict[key] = self.shift_dict.get(
                        key,
                        string.ascii_uppercase[i + shift
                                               - len(string.ascii_uppercase)])

        return self.shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = self.build_shift_dict(shift)
        self.shifted_message_text = ''

        for c in self.get_message_text():
            if c in string.ascii_letters:
                self.shifted_message_text += shift_dict[c]
            else:
                self.shifted_message_text += c

        return self.shifted_message_text


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        # Call the superclass constructor
        Message.__init__(self, text)
        # Instantiate class attributes unique to PlaintextMessage
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift.

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        # set new value for self.shift
        self.shift = shift
        # re-initialize the class with the new shift
        self.__init__(self.get_message_text(), self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # Call the superclass constructor to initialize inherited attributes
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create
        the maximum number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # collect all possible cipher shifts
        decrypt_list = list()
        for i in range(0, len(string.ascii_lowercase)):
            decrypt_list.append(self.apply_shift(i))

        # test each decrypted line for valid English words
        valid_line = list()
        for line in decrypt_list:
            valid_line.append([word for word in line.split() if is_word(
                    self.get_valid_words(), word)])

        # collect line indexes with len > 0
        valid_index = list()
        for line in valid_line:
            if len(line) > 0:
                valid_index.append(valid_line.index(line))

        # Take the maximum value of valid_index as the best shift
        self.best_shift_value = max(valid_index)

        return self.best_shift_value, self.apply_shift(self.best_shift_value)

if __name__ == '__main__':

    # Test Case 1 (PlaintextMessage)
    print('\nTest Case 1: PlaintextMessage\n')
    plaintext_test1 = PlaintextMessage('hello', 3)
    print('Input:', ('hello', 3))
    print('Expected Output: khoor')
    print('Actual Output:', plaintext_test1.get_message_text_encrypted())

    # Test Case 2 (PlaintextMessage)
    print('\nTest Case 2: PlaintextMessage\n')
    plaintext_test2 = PlaintextMessage('HeLlo, WOrld!', 3)
    print('Input:', ('HeLlo, WOrld!', 3))
    print('Expected Output: KhOor, ZRuog!')
    print('Actual Output: ', plaintext_test2.get_message_text_encrypted())

    # Test Case 1 (CiphertextMessage)
    print('\nTest Case 1: CiphertextMessage\n')
    ciphertext_test1 = CiphertextMessage('khoor')
    print('Input: khoor')
    print('Expected Output:', (23, 'hello'))
    print('Actual Output:', ciphertext_test1.decrypt_message())

    # Test Case 2 (CiphertextMessage)
    print('\nTest Case 2: CiphertextMessage\n')
    ciphertext_test2 = CiphertextMessage('KhOor, ZRuog!')
    print('Input: KhOor, ZRuog!')
    print('Expected Output:', (23, 'HeLlo, WOrld!'))
    print('Actual Output:', ciphertext_test2.decrypt_message())

    #TODO: best shift value and unencrypted story


    pass #delete this line and replace with your code here
