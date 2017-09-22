import random
import math

# config
low = 1
high = 100
limit = math.ceil(math.log(100, 2))

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


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()


