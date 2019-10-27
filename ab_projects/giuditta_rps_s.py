#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 19:01:24 2019

@author: giudittaparolini
"""

import random


# Play the Rock-Paper-Scissors Game against the computer - Simple version with just one round

#Game heading
print ("Play the Rock-paper-Scissors Game")


# Playing unit

#Player input
player_inp = input("Enter your choice: rock(r), paper(p), scissors(s)")
print ("Player input is:", player_inp )

#Computer input
print ("The computer is now generating its own input")

lst = [1,2,3] #list of numbers for the random extraction

random_val = random.choice(lst)

def random(random_val): #function that associates a value (r,p,s) to the random number selected
    if random_val == 1:
        return_inp = "r"
    elif random_val == 2:
        return_inp = "p"
    else:
        return_inp = "s"
    return return_inp

computer_inp = str(random(random_val))

print ("The computer input is:", computer_inp)

print(player_inp, "vs", computer_inp)

def result(player_inp, computer_inp):#function that calculates the result of the game 
    if player_inp == computer_inp:
        result = "0-0"
    elif (player_inp == "r") & (computer_inp == "s"):
        result = "1-0"
    elif (player_inp == "r") & (computer_inp == "p"):
        result = "0-1"
    elif (player_inp == "p") & (computer_inp == "r"):
        result = "1-0"
    elif (player_inp == "p") & (computer_inp == "r"):
        result = "1-0"
    elif (player_inp == "p") & (computer_inp == "s"):
        result = "0-1"
    elif (player_inp == "s") & (computer_inp == "r"):
        result = "0-1"
    else:
        result = "1-0"

    return result

outcome = result(player_inp, computer_inp)

print ("The result is:", outcome)

def winner (outcome): #function that declares the winner
    if outcome == "1-0":
        print ("Player wins")
    elif outcome == "0-1":
        print ("Computer wins")
    else:
        print ("It is a draw")
        
winner(outcome)