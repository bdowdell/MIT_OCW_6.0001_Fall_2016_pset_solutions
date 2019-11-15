from ps3 import *

#
# Test code
#


def test_get_word_score():
    """
    Unit test for get_word_score
    """
    failure = False
    # dictionary of words and scores
    words = {
        ("", 7): 0,
        ("it", 7): 2,
        ("was", 7): 54,
        ("weed", 6): 176,
        ("scored", 7): 351,
        ("WaYbILl", 7): 735,
        ("Outgnaw", 7): 539,
        ("fork", 7): 209,
        ("FORK", 4): 308,
        ("App!e", 7): 0,
    }
    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_get_word_score()")
            print(
                "\tExpected",
                words[(word, n)],
                "points but got '"
                + str(score)
                + "' for word '"
                + word
                + "', n="
                + str(n),
            )
            failure = True
    if not failure:
        print("SUCCESS: test_get_word_score()")


# end of test_get_word_score


def test_update_hand():
    """
    Unit test for update_hand
    """
    # test 1
    handOrig = {"a": 1, "q": 1, "l": 2, "m": 1, "u": 1, "i": 1}
    handCopy = handOrig.copy()
    word = "quail"

    hand2 = update_hand(handCopy, word)
    expected_hand1 = {"l": 1, "m": 1}
    expected_hand2 = {"a": 0, "q": 0, "l": 1, "m": 1, "u": 0, "i": 0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('" + word + "', " + str(handOrig) + ")")
        print(
            "\tReturned: ",
            hand2,
            "\n\t-- but expected:",
            expected_hand1,
            "or",
            expected_hand2,
        )

        return  # exit function
    if handCopy != handOrig:
        print("FAILURE: test_update_hand('" + word + "', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)

        return  # exit function

    # test 2
    handOrig = {"e": 1, "v": 2, "n": 1, "i": 1, "l": 2}
    handCopy = handOrig.copy()
    word = "Evil"

    hand2 = update_hand(handCopy, word)
    expected_hand1 = {"v": 1, "n": 1, "l": 1}
    expected_hand2 = {"e": 0, "v": 1, "n": 1, "i": 0, "l": 1}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('" + word + "', " + str(handOrig) + ")")
        print(
            "\tReturned: ",
            hand2,
            "\n\t-- but expected:",
            expected_hand1,
            "or",
            expected_hand2,
        )

        return  # exit function

    if handCopy != handOrig:
        print("FAILURE: test_update_hand('" + word + "', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)

        return  # exit function

    # test 3
    handOrig = {"h": 1, "e": 1, "l": 2, "o": 1}
    handCopy = handOrig.copy()
    word = "HELLO"

    hand2 = update_hand(handCopy, word)
    expected_hand1 = {}
    expected_hand2 = {"h": 0, "e": 0, "l": 0, "o": 0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('" + word + "', " + str(handOrig) + ")")
        print(
            "\tReturned: ",
            hand2,
            "\n\t-- but expected:",
            expected_hand1,
            "or",
            expected_hand2,
        )

        return  # exit function

    if handCopy != handOrig:
        print("FAILURE: test_update_hand('" + word + "', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)

        return  # exit function

    # test 4
    handOrig = {"j": 2, "o": 1, "l": 1, "w": 1, "n": 2}
    handCopy = handOrig.copy()
    word = "jolly"  # testing for words that cannot be created with hand

    hand2 = update_hand(handCopy, word)
    expected_hand1 = {"j": 1, "w": 1, "n": 2}
    expected_hand2 = {"j": 1, "o": 0, "l": 0, "w": 1, "n": 2}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('" + word + "', " + str(handOrig) + ")")
        print(
            "\tReturned: ",
            hand2,
            "\n\t-- but expected:",
            expected_hand1,
            "or",
            expected_hand2,
        )

        return  # exit function

    if handCopy != handOrig:
        print("FAILURE: test_update_hand('" + word + "', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)

        return  # exit function

    print("SUCCESS: test_update_hand()")


# end of test_update_hand


def test_is_valid_word(word_list):
    """
    Unit test for is_valid_word
    """
    failure = False
    # test 1
    word = "hello"
    handOrig = get_frequency_dict(word)
    handCopy = handOrig.copy()

    if not is_valid_word(word, handCopy, word_list):
        print("FAILURE: test_is_valid_word()")
        print(
            "\tExpected True, but got False for word: '" + word + "' and hand:",
            handOrig,
        )

        failure = True

    # Test a second time to see if word_list or hand has been modified
    if not is_valid_word(word, handCopy, word_list):
        print("FAILURE: test_is_valid_word()")

        if handCopy != handOrig:
            print(
                "\tTesting word",
                word,
                "for a second time - be sure you're not modifying hand.",
            )
            print("\tAt this point, hand ought to be", handOrig, "but it is", handCopy)

        else:
            print(
                "\tTesting word",
                word,
                "for a second time - have you modified word_list?",
            )
            wordInWL = word in word_list
            print("The word", word, "should be in word_list - is it?", wordInWL)

        print(
            "\tExpected True, but got False for word: '" + word + "' and hand:",
            handCopy,
        )

        failure = True

    # test 2
    hand = {"r": 1, "a": 3, "p": 2, "e": 1, "t": 1, "u": 1}
    word = "Rapture"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 3
    hand = {"n": 1, "h": 1, "o": 1, "y": 1, "d": 1, "w": 1, "e": 2}
    word = "honey"

    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

    # test 4
    hand = {"r": 1, "a": 3, "p": 2, "t": 1, "u": 2}
    word = "honey"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 5
    hand = {"e": 1, "v": 2, "n": 1, "i": 1, "l": 2}
    word = "EVIL"

    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

    # test 6
    word = "Even"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        print(
            "\t(If this is the only failure, make sure is_valid_word() isn't mutating its inputs)"
        )

        failure = True

    if not failure:
        print("SUCCESS: test_is_valid_word()")


# end of test_is_valid_word


def test_wildcard(word_list):
    """
    Unit test for is_valid_word
    """
    failure = False

    # test 1
    hand = {"a": 1, "r": 1, "e": 1, "j": 2, "m": 1, "*": 1}
    word = "e*m"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 2
    hand = {"n": 1, "h": 1, "*": 1, "y": 1, "d": 1, "w": 1, "e": 2}
    word = "honey"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 3
    hand = {"n": 1, "h": 1, "*": 1, "y": 1, "d": 1, "w": 1, "e": 2}
    word = "h*ney"

    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

    # test 4
    hand = {"c": 1, "o": 1, "*": 1, "w": 1, "s": 1, "z": 1, "y": 2}
    word = "c*wz"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 5 Mixed Case input
    hand = {"y": 1, "o": 1, "*": 1, "t": 1, "h": 1, "n": 2}
    word = "Yo*Th"

    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

    # dictionary of words and scores WITH wildcards
    words = {("h*ney", 7): 290, ("c*ws", 6): 176, ("wa*ls", 7): 203, ("Yo*Th", 7): 290}
    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_get_word_score() with wildcards")
            print(
                "\tExpected",
                words[(word, n)],
                "points but got '"
                + str(score)
                + "' for word '"
                + word
                + "', n="
                + str(n),
            )
            failure = True

    if not failure:
        print("SUCCESS: test_wildcard()")


def test__verify_num_hands():
    """
    unit test for _verify_num_hands
    """
    failure = False
    num_hands = {
        "3": True,
        "33": False,
        "7": True,
        "a": False,
        "aa": False,
        "three": False,
    }

    for key in num_hands.keys():
        if not (_verify_num_hands(key) == num_hands[key]):
            print("FAILURE: test__verify_num_hands()")
            print("\tExpected", num_hands[key], "but got ", not num_hands[key])
            failure = True

    if not failure:
        print("SUCCESS: test__verify_num_hands()")


def test__verify_substitution_input():
    """
    unit test for _verify_substitution_input
    """
    failure = False
    subs_choice = {
        "yes": True,
        "no": True,
        "YES": True,
        "NO": True,
        "yesa": False,
        "nosa": False,
        "HAppY": False,
        "7": False,
        "1": False,
    }

    for key in subs_choice.keys():
        if not (_verify_substitution_input(key) == subs_choice[key]):
            print("FAILURE: test__verify_substitution_input")
            print("\tExpected", subs_choice[key], "but got ", not subs_choice[key])
            failure = True

    if not failure:
        print("SUCCESS: test__verify_substitution_input()")


def test__verify_sub_letter():
    """unit test for _verify_sub_letter(sub_letter)"""
    failure = False
    sub_letter = {
        "c": True,
        "x": True,
        "a": True,
        "E": True,
        "as": False,
        "AV": False,
        "23": False,
        "!@": False,
        "": False,
        " ": False,
    }

    for key in sub_letter.keys():
        if not (_verify_sub_letter(key) == sub_letter[key]):
            print("FAILURE: test__verify_sub_letter")
            print("\tExpected", sub_letter[key], "but got ", not sub_letter[key])
            failure = True

    if not failure:
        print("SUCCESS: test__verify_sub_letter()")


def test__check_subs_remaining():
    """unit test for _check_subs_remaining"""
    failure = False
    subs_left = {
        "1": True,
        "0": False,
        "2": False,
    }

    for key in subs_left.keys():
        if not (_check_subs_remaining(int(key)) == subs_left[key]):
            print("FAILURE: test__check_subs_remaining")
            print("\tExpected", subs_left[key], "but got ", not subs_left[key])
            failure = True

    if not failure:
        print("SUCCESS: test__check_subs_remaining()")


def test__check_replays_remaining():
    """unit test for _check_replays_remaining"""
    failure = False
    replays_left = {
        "1": True,
        "0": False,
        "2": False,
    }

    for key in replays_left.keys():
        if not (_check_replays_remaining(int(key)) == replays_left[key]):
            print("FAILURE: test__check_replays_remaining")
            print("\tExpected", replays_left[key], "but got ", not replays_left[key])
            failure = True

    if not failure:
        print("SUCCESS: test__check_replays_remaining()")


def test__verify_replay_input():
    """unit test for _verify_replay_input(replay_choice)"""
    failure = False
    replay_choice = {
        "yes": True,
        "no": True,
        "YES": True,
        "NO": True,
        "yesa": False,
        "nosa": False,
        "HAppY": False,
        "7": False,
        "1": False,
    }

    for key in replay_choice.keys():
        if not (_verify_replay_input(key) == replay_choice[key]):
            print("FAILURE: test__verify_replay_input")
            print("\tExpected", replay_choice[key], "but got ", not replay_choice[key])
            failure = True

    if not failure:
        print("SUCCESS: test__verify_replay_input()")


word_list = load_words()
print("----------------------------------------------------------------------")
print("Testing get_word_score...")
test_get_word_score()
print("----------------------------------------------------------------------")
print("Testing update_hand...")
test_update_hand()
print("----------------------------------------------------------------------")
print("Testing is_valid_word...")
test_is_valid_word(word_list)
print("----------------------------------------------------------------------")
print("Testing wildcards...")
test_wildcard(word_list)
print("----------------------------------------------------------------------")
print("Testing _verify_num_hands ...")
test__verify_num_hands()
print("----------------------------------------------------------------------")
print("Testing _verify_substitution_input ...")
test__verify_substitution_input()
print("----------------------------------------------------------------------")
print("Testing _verify_sub_letter ...")
test__verify_sub_letter()
print("----------------------------------------------------------------------")
print("Testing _check_subs_remaining ...")
test__check_subs_remaining()
print("----------------------------------------------------------------------")
print("Testing _check_replays_remaining ...")
test__check_replays_remaining()
print("----------------------------------------------------------------------")
print("Testing _verify_replay_input ...")
test__verify_replay_input()
print("----------------------------------------------------------------------")
print("All done!")
