import pytest


# Caesar cipher.
def caesar_cipher(text, shift):
    cipher = ""
    for char in text:
        if not char.isalpha():
            cipher += char
            continue
        # char = char.upper()
        code = ord(char) + shift
        if char.isupper():
            if code > ord('Z'):
                code -= 26
        else:
            if code > ord('z'):
                code -= 26

        cipher += chr(code)
    return cipher


def test_caesar_cipher():
    assert (caesar_cipher("abcxyzABCxyz 123", 2) == "cdezabCDEzab 123")
    assert (caesar_cipher("The die is cast", 25) == "Sgd chd hr bzrs")
