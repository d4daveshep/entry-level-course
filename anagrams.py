import pytest


def is_anagram(text1, text2):
    text1 = text1.upper().replace(" ", "")
    text2 = text2.upper().replace(" ", "")

    for ch in text1:
        if ch not in text2:
            return False
    return True


def test_is_anagram():
    assert is_anagram("Listen", "Silent")
    assert not is_anagram("modern", "norman")
