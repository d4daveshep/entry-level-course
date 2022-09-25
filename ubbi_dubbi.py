# Exercise 2.4 from Python Workout
# Write a UBBI DUBBI translater

import pytest

VOWELS = "aeiou"

def ubbi_dubbi(english_word: str) -> str:
    ubbi = []
    for char in english_word:
        if char in VOWELS:
            ubbi.append(f"ub{char}")
        else:
            ubbi.append(char)
    return "".join(ubbi)


def test():
    assert ubbi_dubbi("milk") == "mubilk"
    assert ubbi_dubbi("program") == "prubogrubam"
    assert ubbi_dubbi("octopus") == "uboctubopubus"
    assert ubbi_dubbi("elephant") == "ubelubephubant"
