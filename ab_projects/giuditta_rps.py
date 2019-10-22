#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 19:01:24 2019

@author: giudittaparolini
"""

import random


# Play the Rock-Paper-Scissors Game against the computer

#Game heading
print ("Play the Rock-paper-Scissors Game")

#Ask the player to input the number of rounds for the game
rounds = float(input("How many rounds would you like to play?"))
rounds_int = round(rounds) #the input is rounded to the nearest integer. If the player inputs a non-numerical value by mistake python throws a ValueError

print("This game will have", rounds_int, "round(s)") #the total number of rounds is printed to the console for convenience


# Playing unit

#Player input
player_inp = input("Enter your choice: rock(r), paper(p), scissors(s)")
print ("Player input is:", player_inp )

#Computer input
print ("The computer is now generating its own input")

lst = [1,2,3]

random_val = random.choice(lst)

def random(random_val):
    if random_val == 1:
        return_inp = "r"
    elif random_val == 2:
        return_inp = "p"
    else:
        return_inp = "s"
    return return_inp

computer_inp = random (random_val)

print ("The computer input is:", computer_inp)

#print player_inp vs computer input



def compare(player_inp, computer_inp):
    if player_inp == r & computer_inp == s:
        result = "r"
    elif random_val == 2:
        return_inp = "p"
    else:
        return_inp = "s"
    return return_inp


