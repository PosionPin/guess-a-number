#Chase Dunlap
#9/27/17
#A program where the player thinks of a number and the computer tries to predict it.

import math
import random


# helper functions

def get_name():
    print(" ")
    pn = input("What's your name?    ")
    print(" ")
    return pn

def pick_lowz(player_name):
    print(" ")

    while True:
        pick_low = input("What do you want the low to be, " + player_name + "?     ")
        if pick_low.isnumeric():
            print(" ")
            print("Thanks")
            print(" ")
            return pick_low
        else:
            print(" ")
            print("Please type a number")
            print(" ")
            
def pick_highz(player_name):
    while True:
        pick_high = input ("What do you want the high to be, " + player_name + "?     ")
        if pick_high.isnumeric():
            print(" ")
            print("Thanks")
            return pick_high
        else:
            print(" ")
            print("Please type a number")
            print(" ")

def show_start_screen():
    print(""" ██████╗ ██╗   ██╗███████╗███████╗███████╗       █████╗       ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗      █████╗    ██╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝      ██╔══██╗      ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗    ██╔══██╗   ██║
██║  ███╗██║   ██║█████╗  ███████╗███████╗█████╗███████║█████╗██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝    ███████║   ██║
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║╚════╝██╔══██║╚════╝██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗    ██╔══██║   ██║
╚██████╔╝╚██████╔╝███████╗███████║███████║      ██║  ██║      ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    ██║  ██║██╗██║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝      ╚═╝  ╚═╝      ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝╚═╝""")

def show_credits():
    print(" ")
    print(""" ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗██████╗     ██████╗ ██╗   ██╗        ██████╗██╗  ██╗ █████╗ ███████╗███████╗
██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝██╗    ██╔════╝██║  ██║██╔══██╗██╔════╝██╔════╝
██║     ██████╔╝█████╗  ███████║   ██║   █████╗  ██║  ██║    ██████╔╝ ╚████╔╝ ╚═╝    ██║     ███████║███████║███████╗█████╗  
██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝  ██║  ██║    ██╔══██╗  ╚██╔╝  ██╗    ██║     ██╔══██║██╔══██║╚════██║██╔══╝  
╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗██████╔╝    ██████╔╝   ██║   ╚═╝    ╚██████╗██║  ██║██║  ██║███████║███████╗
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝     ╚═════╝    ╚═╝           ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝""")
    
def get_guess(current_low, current_high):
    g = (int(current_low) + int(current_high)) // 2
    return g

def get_tries(pick_low, pick_high):
    tries = math.ceil(math.log(((int(pick_high) - int(pick_low))-1),2))
    return tries

def pick_number(player_name, pick_low, pick_high):
    print(" ")
    print(player_name + ", think of a number between " + str(pick_low) + " to " + str(pick_high) + ".")
    print(" ")
    input("Press enter when your ready ")

def state_tries(tries, turns):
    print(" ")
    print("I have " + str(turns) + " out of " + str(tries) + " tries left.")

def check_guess(tries, guess, player_name):
    print(" ")
    print("Is " + str(guess) + " your number, " + player_name + "?")
    print(" ")
    r = input(player_name + ", if it was correct put 'yes'. If it was to high put 'lower'. If it was to low put 'higher'.    ")
    r = r.lower()

    if r == 'yes' or r == 'y':
        return 0
    elif r == 'lower' or r == 'l':
        return -1
    elif r == 'higher' or r == 'h':
        return 1
    else:
        print(" ")
        print("Please type 'yes' if it was correct, 'lower' if it was too high, or 'higher' if it was too low")


def show_result():
    pass

def play_again(player_name, tries, turns):
    while True:
        print(" ")
        if tries == turns:
            print("Play by the rules next time meanie:(")
        else:
            print("I got it")
        print(" ")
        decision = input("Would you like to play again, " + player_name + "? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print(" ")
            print("I don't understand. Please enter 'y' or 'n'.")

def play(player_name):
          
    result = -1

    pick_low = pick_lowz(player_name)
      
    pick_high = pick_highz(player_name)

    tries = get_tries(pick_low,pick_high)

    turns = 1
    
    pick_number(player_name, pick_low, pick_high)

    current_low = pick_low

    current_high = pick_high
    
    while result != 0:
        guess = get_guess(current_low, current_high)

        state_tries(tries, turns)

        result = check_guess(tries, guess, player_name)

        if result == -1:
            if turns == tries:
                print(" ")
                print("I think you made a mistake somewhere")
                result = 0
            else:
                current_high = guess
                turns += 1

        elif result == 1:
            if turns == tries:
                print(" ")
                print("I think you made a mistake somewhere")
                result = 0
            else:
                current_low = guess
                turns += 1

    show_result()

# Game starts running here
show_start_screen()

player_name = get_name()

playing = True

while playing:
    play(player_name)
    playing = play_again(player_name, tries, turns)

show_credits()
