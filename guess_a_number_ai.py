#Chase Dunlap
#9/27/17
#A program where the player thinks of a number and the computer tries to predict it.


import random

# config
low = 1
high = 100


# helper functions
def show_start_screen():
    print("**************************")
    print("*  Guess a Number A.I.!  *")
    print("**************************")

def show_credits():
    print(" ")
    print("This awesome game was created by Chase Dunalp.")
    
def get_guess(current_low, current_high):
    g = (current_low + current_high) // 2
    return g

def pick_number():
        print(" ")
        print("Think of a number between " + str(low) + " to " + str(high) + ".")
        print(" ")
        input("Press enter when your ready ")


def check_guess(guess):
    print(" ")
    print("Is " + str(guess) + " your number?")
    print(" ")
    r = input("If it was correct put 'yes'. If it was to high put 'lower'. If it was too low put 'higher'.")

    if r == 'yes':
        return 0
    elif r == 'lower':
        return -1
    elif r == 'higher':
        return 1
    else:
        print(" ")
        print("Please type 'yes' if it was correct, 'lower' if it was too high, or 'higher' if it was too low")


def show_result():
    pass

def play_again():
    while True:
        print(" ")
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print(" ")
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    result = -1
    
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
