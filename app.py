from elevator import Elevator
import random

alphabet = ['-A', '-B', '-C', '-D']
direction = ['up', 'down']
levels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
for letter in alphabet:
    elevator = Elevator(letter,
                        random.choice(direction),
                        random.choice(levels),
                        random.choice(levels),
                        random.choice(levels))




