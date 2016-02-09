import os
import time
from random import randint, getrandbits

VIEW_GRID_START = 0
VIEW_GRID_END = 11
NUM_GRID_START = 0
NUM_GRID_END = 11
NUM_OF_NUMS = 9

# 0 -> 10 : view grid
# 1 -> 9 : number grid

#    0 1 2 3 4 5 6 7 8 9 10
# 0  . . . . . . . . . . . 
# 1  . o o o o o o o o o .
# 2  . o o o o o o o o o .
# 3  . o o o o o o o o o .
# 4  . o o o o o o o o o .
# 5  . o o o o o o o o o .
# 6  . o o o o o o o o o .
# 7  . o o o o o o o o o .
# 8  . o o o o o o o o o .
# 9  . o o o o o o o o o .
# 10 . . . . . . . . . . . 

def display_grid(x, y):
    grid = [["." for i in range(VIEW_GRID_START, VIEW_GRID_END)] for j in range(VIEW_GRID_START, VIEW_GRID_END)]

    # Put the numbers into the view grid
    for next_num in range(len(x)):
        grid[y[next_num]][x[next_num]] = str(next_num+1)

    os.system('clear')

    for i in range(11):
            print(" ".join(grid[i]))    

score = 0
another_go = True

while (another_go):
    
    x = [randint(1,9) for i in range(NUM_OF_NUMS)]
    y = [randint(1,9) for i in range(NUM_OF_NUMS)]

    # Display each number number in its random x,y location
    display_grid(x, y)

    # Wait for a key
    input("")        

    # Choose which number to move left or right
    num_to_move = randint(0,NUM_OF_NUMS-1)

    if (getrandbits(1) == 1):
        x[num_to_move] = x[num_to_move] + 1
        print("moving %s right" % num_to_move)
    else:
        x[num_to_move] = x[num_to_move] - 1
        print("moving %s left" % num_to_move)

    display_grid(x, y)
    time.sleep(0.1)

    os.system('clear')
    print("WHICH NUMBER MOVED")
    user_guess = input("")

    if (user_guess == str(num_to_move+1)):
        print("WELL SPIED!")
        score += 1
        print("YOU NOW HAVE %s POINTS" % score)
        print("\nPRESS ENTER KEY")
        input("")  
    else:
        print("\nWRONG END OF GO")
        print("CORRECT ANSWER WAS %s" % str(num_to_move+1))
        print("YOU SCORED %s POINTS" % score)
        score = 0 # reset score for next go if there is one
        print("ANOTHER GO (Y/N)")
        another_go_input = input("")
        if (another_go_input.upper() != 'Y'):
            another_go = False