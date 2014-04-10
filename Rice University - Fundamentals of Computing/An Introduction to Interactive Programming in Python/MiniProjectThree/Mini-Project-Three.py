# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math


# initialize global variables used in your code
secret_number = 0
guess_left = 0
num_range = 100

# helper function to start and restart the game
def new_game():
    global secret_number, guess_left
    secret_number = random.randrange(0, num_range)
    guess_left = math.ceil(math.log(num_range, 2))
    print "Guessing range is 0 - " + str(num_range - 1) + " with " + str(int(guess_left)) + " guesses."
    
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts    
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global guess_left
    
    guess_left = guess_left - 1
    guess = int(guess)
    if(guess < secret_number):
        print "Your guess " + str(guess) + " is too low."
    elif(guess > secret_number):
        print "Your guess " + str(guess) + " is too high."
    else:
        print "Your guess " + str(guess) + " is correct!"
        new_game()
    if(int(guess_left) == 0):
        print "You ran out of guesses!"
        print
        new_game()
    else:
        print "You have " + str(int(guess_left)) + "guesses left."
        print
    
# create frame
frame = simplegui.create_frame("Guess the number", 300, 200)

# register event handlers for control elements
frame.add_button("[0-99]", range100, 100)
frame.add_button("[0-999]", range1000, 100)
frame.add_input("Your Guess", input_guess, 100)

# call new_game and start frame
new_game()
frame.start()



# always remember to check your completed program against the grading rubric
