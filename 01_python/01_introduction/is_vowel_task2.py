#!/usr/bin/env python3
# check if letter is a vowel

def is_vowel(letter):
    """Check if letter is a vowel

    Args:
        letter (str): the letter to check

    Returns: bool

    Examples:

        >>> is_vowel('a')
        True

        >>> is_vowel('b')
        False

        >>> is_vowel('A')
        True

        >>> is_vowel(50)
        Traceback (most recent call last):
        TypeError: Letter must be a string

        >>> is_vowel(True)
        Traceback (most recent call last):
        TypeError: Letter must be a string

        >>> is_vowel('')
        Traceback (most recent call last):
        ValueError: Letter must be at least one character
        """
    if type(letter) is not str:
        raise TypeError("Letter must be a string")
    if len(letter) < 1:
        raise ValueError("Letter must be at least one character")
    return letter[0].lower() in ['a', 'e', 'i', 'o', 'u']


if __name__ == '__main__':
    while 1:
        letter = input("> Enter a letter [nothing to quit]: ")
        if not letter:
            break

        if is_vowel(letter):
            print("Vowel")
        else:
            print("Consonant")
