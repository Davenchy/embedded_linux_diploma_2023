#!/usr/bin/env python3
# check if letter is a vowel

def is_vowel(letter):
    return letter.lower() in ['a', 'e', 'i', 'o', 'u']


while 1:
    letter = input("> Enter a letter [nothing to quit]: ")
    if not letter:
        break

    if is_vowel(letter[0]):
        print("Vowel")
    else:
        print("Consonant")
