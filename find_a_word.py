import pytest

def find_a_word(scramble, word):
    scramble = scramble.lower()
    word = word.lower()

    idx = 0  # start at the beginning of the scramble
    for ch in word:
        idx = scramble.find(ch,idx)
        if idx == -1:
            return False
    return True


def test_find_a_word():

    assert find_a_word("Nabucodonosor","donor") == True
    assert find_a_word("Nabucodonosor","donut") == False