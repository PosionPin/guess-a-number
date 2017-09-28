#Chase Dunlap
#9/27/17
#A program where the player thinks of a number and the computer tries to predict it.


import random


# helper functions
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
    g = (current_low + current_high) // 2
    return g

def pick_number():
    print(" ")
    pick_low = input("What do you want the low to be?")

    while True:
        if low.isnumeric():
            print(" ")
            print("Thanks")
            print(" ")
            break
        else:
            print(" ")
            print("Please type a number")
            print(" ")
        
    pick_high = input ("What do you want the high to be")

    while True:
        if high.isnumeric():
            print(" ")
            print("Thanks")
            break
        else:
            print(" ")
            print("Please type a number")
        
    print(" ")
    print("Think of a number between " + str(pick_low) + " to " + str(pick_high) + ".")
    print(" ")
    input("Press enter when your ready ")


def check_guess(guess):
    print(" ")
    print("Is " + str(guess) + " your number?")
    print(" ")
    r = input("If it was correct put 'yes'. If it was to high put 'lower'. If it was too low put 'higher'.    ")
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

def play_again():
    while True:
        print(" ")
        print("I got it!")
        print(" ")
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print(" ")
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    result = -1

    pick_high_and_low()
    
    pick_number()
    
    while result != 0:
        guess = get_guess(current_low, current_high)

        result = check_guess(guess)

        if result == -1:
            current_high = guess

        elif result == 1:
            current_low = guess



    show_result()

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
