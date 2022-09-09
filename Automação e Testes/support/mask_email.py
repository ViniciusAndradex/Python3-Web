from string import ascii_letters
from random import choice


def mask_generator():
    c = 0
    mail = ""
    while c <= 15:
        mail += choice(ascii_letters)
        if c == 8:
            mail += '@'
        elif c == 12:
            mail += '.'
        c += 1 
    return mail
    