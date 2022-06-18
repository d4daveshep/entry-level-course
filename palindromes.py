import pytest


def is_palindrome_1(text):
    text = text.upper()
    text = text.replace(" ", "")
    text_chars = list(text)
    reverse_chars = []
    for i in text_chars:
        reverse_chars.insert(0, i)
    return text_chars == reverse_chars


def is_palindrome_2(text):
    text = text.upper()
    text = text.replace(" ", "")
    text_chars = list(text)
    reverse_chars = text_chars[:]
    reverse_chars.reverse()
    return text_chars == reverse_chars


def test_is_palindrome():
    assert is_palindrome_2("kayak")
    assert not is_palindrome_2("lemon")
    assert is_palindrome_2("Ten animals I slam in a net")
    assert not is_palindrome_2("Eleven animals I slam in a net")
