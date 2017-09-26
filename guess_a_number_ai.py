import random

# config
low = 1
high = 1000


# helper functions
def show_start_screen():
    print("**************************")
    print("*  Guess a Number A.I.!  *")
    print("**************************")

def show_credits():
    print("This awesome game was created by Chase Dunalp.")
    
def get_guess(current_low, current_high):
    g = (current_low + current_high) // 2
    return g

def pick_number():
    while True:
        print("Think of a number between " + str(low) + " to " + str(high) + ".")
        print(" ")
        ready = input("Type 'y' when your ready ")

        if ready == 'y':
            return False
        else:
            print(" ")
            print("I don't understand. Please enter 'y' when your ready")
            print(" ")

def check_guess(guess):
    print(" ")
    print("Is " + str(guess) + " your number?")
    print(" ")
    r = input("If it was correct put 0. If it was to high put 1. If it was too low put -1")
    #Returns -1 if the guess was too low
             #0 if the guess was correct
             #1 if the guess was too high

def show_result():
    pass

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
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
            # adjust current high
            pass
        elif result == 1:
            # adjust current low
            pass

    show_result()

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
