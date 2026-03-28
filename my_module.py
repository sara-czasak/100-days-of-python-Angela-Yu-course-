import random


def change_color():
    ''' Generates a random RBG color.'''
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b