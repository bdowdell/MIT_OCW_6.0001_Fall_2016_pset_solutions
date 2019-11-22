# Problem Set 4A
# Name: Ben Dowdell
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # =============================================================================
    #   I needed some help on this one.
    #
    #   I found a good resource here:
    #   https://medium.com/@aberg2014/recursively-generating-string-permutations-381b4ad9588
    #
    #   The example in this explanation is written in JavaScript
    #   I translatd the solution to Python!
    # =============================================================================

    # Base Case: sequence has one character to return
    if len(sequence) == 1:
        return sequence

    # initialize empty list to hold permutations
    perm_list = list()

    # Loop over each letter in sequence
    # Grabs the letter at index i in sequence
    # Passes remaining letters in sequence to get_permutations
    # Recursively finds the permutations of the remaining letters
    # Builds the permutations by looping, concatenating the current_letter
    # Returns a list of all permutations
    for i in range(0, len(sequence)):
        current_letter = sequence[i]
        remaining_letters = sequence[0:i] + sequence[i+1:]
        perms_remaining_letters = get_permutations(remaining_letters)

        for perm in perms_remaining_letters:
            perm_list.append(current_letter + perm)

    return perm_list


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length n)

    # TEST 1
    print('-'*2,'TEST #1','-'*20)
    test1_input = 'dog'
    test1_expected_output = [
            'dog',
            'dgo',
            'odg',
            'ogd',
            'gdo',
            'god',
    ]
    print('Input: ', test1_input)
    print('Expected Output: ', test1_expected_output)
    test1_output = get_permutations(test1_input)
    if test1_expected_output == test1_output:
        print('Success! Output: ', test1_output)
    else:
        print('Failure!  Expected: ',test1_expected_output,
              'But got: ', test1_output)

    print()

    # TEST 2
    print('-'*2,'TEST #2','-'*20)
    test2_input = 'cat'
    test2_expected_output = [
            'cat',
            'cta',
            'act',
            'atc',
            'tca',
            'tac',
    ]
    print('Input: ', test2_input)
    print('Expected Output: ', test2_expected_output)
    test2_output = get_permutations(test2_input)
    if test2_expected_output == test2_output:
        print('Success! Output: ', test2_output)
    else:
        print('Failure!  Expected: ', test2_expected_output,
              'But got: ', test2_output)

    print()

    # TEST 3
    print('-'*2, 'TEST #3', '-'*20)
    test3_input = 'mar'
    test3_expected_output = [
            'mar',
            'mra',
            'amr',
            'arm',
            'rma',
            'ram',
    ]
    print('Input: ', test3_input)
    print('Expected Output: ', test3_expected_output)
    test3_output = get_permutations(test3_input)
    if test3_expected_output == test3_output:
        print('Success! Output: ', test3_output)
    else:
        print('Failure!  Expected: ', test3_expected_output,
              'But got: ', test3_output)

    print('\n\nCOMPLETE.')

