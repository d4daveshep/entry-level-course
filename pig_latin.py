# Exercise 2.2 from Python Workout
# Write a pig latin converter

import pytest


def convert(english):

    pig_latin = ""
    if english[0] in "aeiou":
        pig_latin = english + "way"
    else:
        pig_latin = english[1:] + english[0] + "ay"
    return pig_latin


def test():
    
    assert convert("air") == "airway"
    assert convert("eat") == "eatway"
    assert convert("python") == "ythonpay"
    assert convert("computer") == "omputercay"