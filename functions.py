# This will be all the functions needed to run this program

import random


def spongeBobTextConversion(input_text):
    characters = []  # To store the changed characters
    for letter in input_text:  # To loop through each character in the given text
        if random.randint(1, 2) == 1:  # This will randomly occur, about half the time
            letter = letter.lower()
        else:
            letter = letter.upper()
        characters.append(letter)  # This will put the modified characters back into the list

    i = 0  # The initial character index position will be set here
    while i < len(characters) - 2:  # To cycle through all the characters in the text entry
        if characters[i].isupper() and characters[i+1].isupper():  # To check if there is multiple consecutive uppercase characters
            characters[i+2] = characters[i+2].lower()  # Change the next one to lowercase if so
        elif characters[i].islower() and characters[i+1].islower():  # To check for too many lower characters
            characters[i+2] = characters[i+2].upper()  # To change the next one to uppercase
        i += 1

    text_converted = ''.join(characters)  # To join the character list back into a single string
    return text_converted
