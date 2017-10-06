#Chase Dunlap
#9/27/17
#A program where the player thinks of a number and the computer tries to predict it.

import math
import random


# helper functions
def show_start_screen():
    print(""" _____                               _   _                 _               
|  __ \                             | \ | |               | |              
| |  \/_   _  ___  ___ ___    __ _  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __|  / _` | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | (_| | | |\  | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__,_| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|   """)


def show_credits():
    print("""___  ___          _       ______         _____ _                     ______             _             
|  \/  |         | |      | ___ \       /  __ \ |                    |  _  \           | |            
| .  . | __ _  __| | ___  | |_/ /_   _  | /  \/ |__   __ _ ___  ___  | | | |_   _ _ __ | | __ _ _ __  
| |\/| |/ _` |/ _` |/ _ \ | ___ \ | | | | |   | '_ \ / _` / __|/ _ \ | | | | | | | '_ \| |/ _` | '_ \ 
| |  | | (_| | (_| |  __/ | |_/ / |_| | | \__/\ | | | (_| \__ \  __/ | |/ /| |_| | | | | | (_| | |_) |
\_|  |_/\__,_|\__,_|\___| \____/ \__, |  \____/_| |_|\__,_|___/\___| |___/  \__,_|_| |_|_|\__,_| .__/ 
                                  __/ |                                                        | |    
                                 |___/                                                         |_|""")
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a positive number you nimrod.")

def pick_number():
    print(" ")
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +". You have " + str(limit) + " tries.")

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print(" ")
        print("You guessed too low.")
    elif guess > rand:
        print(" ")
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
        print(" ")
        print("You win! now go get a life.")
        print(" ")
    else:
        print(" ")
        print("Wow you're really jsut a waste in space aren't you? The number was " + str(rand) + ".")
        print(" ")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("Wow you can't even type y or n.")
            print(" ")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)

def which_game():
    choice = input("Type 'ai' for Guess-a-number-AI or type 'gan' for Guess-a-Number.")
    choice = choice.lower()

    if choice == 'ai':
        return 1
    elif choice == 'gan':
        return -1
               
def a_get_name():
    print(" ")
    pn = input("What's your name?    ")
    print(" ")
    return pn

def a_pick_lowz(player_name):
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
            
def a_pick_highz(player_name):
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

def a_show_start_screen():
    print(""" ██████╗ ██╗   ██╗███████╗███████╗███████╗       █████╗       ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗      █████╗    ██╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝      ██╔══██╗      ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗    ██╔══██╗   ██║
██║  ███╗██║   ██║█████╗  ███████╗███████╗█████╗███████║█████╗██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝    ███████║   ██║
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║╚════╝██╔══██║╚════╝██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗    ██╔══██║   ██║
╚██████╔╝╚██████╔╝███████╗███████║███████║      ██║  ██║      ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    ██║  ██║██╗██║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝      ╚═╝  ╚═╝      ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝╚═╝""")

def a_show_credits():
    print(" ")
    print(""" ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗██████╗     ██████╗ ██╗   ██╗        ██████╗██╗  ██╗ █████╗ ███████╗███████╗
██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝██╗    ██╔════╝██║  ██║██╔══██╗██╔════╝██╔════╝
██║     ██████╔╝█████╗  ███████║   ██║   █████╗  ██║  ██║    ██████╔╝ ╚████╔╝ ╚═╝    ██║     ███████║███████║███████╗█████╗  
██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝  ██║  ██║    ██╔══██╗  ╚██╔╝  ██╗    ██║     ██╔══██║██╔══██║╚════██║██╔══╝  
╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗██████╔╝    ██████╔╝   ██║   ╚═╝    ╚██████╗██║  ██║██║  ██║███████║███████╗
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝     ╚═════╝    ╚═╝           ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝""")
    
def a_get_guess(current_low, current_high):
    g = (int(current_low) + int(current_high)) // 2
    return g

def a_get_tries(pick_low, pick_high):
    tries = math.ceil(math.log(((int(pick_high) - int(pick_low))-1),2))
    return tries

def a_pick_number(player_name, pick_low, pick_high):
    print(" ")
    print(player_name + ", think of a number between " + str(pick_low) + " to " + str(pick_high) + ".")
    print(" ")
    input("Press enter when your ready ")

def a_state_tries(tries, turns):
    print(" ")
    print("I have " + str(turns) + " out of " + str(tries) + " tries left.")

def a_check_guess(tries, guess, player_name):
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


def a_show_result():
    pass

def a_play_again(player_name):
    while True:
        print(" ")
        print("I win")
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

def a_play(player_name):
          
    result = -1

    pick_low = a_pick_lowz(player_name)
      
    pick_high = a_pick_highz(player_name)

    tries = a_get_tries(pick_low,pick_high)

    turns = 1
    
    a_pick_number(player_name, pick_low, pick_high)

    current_low = pick_low

    current_high = pick_high
    
    while result != 0:
        guess = a_get_guess(current_low, current_high)

        a_state_tries(tries, turns)

        result = a_check_guess(tries, guess, player_name)

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


    a_show_result()



choice = which_game()

#A.I Game starts running here

if choice == 1:
    a_show_start_screen()

    player_name = a_get_name()

    playing = True

    while playing:
        a_play(player_name)
        playing = a_play_again(player_name)

    a_show_credits()

#Guess-a-number starts here
    
elif choice == -1:
    
    low = 1
    high = 100
    limit = math.ceil(math.log(100, 2))
    
    show_start_screen()

    playing = True

    while playing:
        play()
        playing = play_again()

    show_credits()

