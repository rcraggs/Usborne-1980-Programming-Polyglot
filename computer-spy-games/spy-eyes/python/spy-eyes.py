import os
import time
from random import randint, getrandbits

def display_grid(x, y):
    grid = [["." for i in range(len(x)+1)] for j in range(len(y)+1)]

    for next_num_to_display in range(HOW_MANY_NUMBERS_TO_DISPLAY-1):
        # The arrays are zero indexed so add one to make the number shown 1-9
        print(x[next_num_to_display])
        grid[y[next_num_to_display]][x[next_num_to_display]] = str(next_num_to_display+1)

    os.system('clear')

    for i in range(9):
            print(" ".join(grid[i]))    

score = 0

HOW_MANY_NUMBERS_TO_DISPLAY = 9
SIZE_OF_GRID = 9

# x and y are arrays from 0..8 containing random numbers from 1..9.
# this gives us 9 random x,y locations
x = [randint(1,SIZE_OF_GRID) for i in range(0,HOW_MANY_NUMBERS_TO_DISPLAY-1)]
y = [randint(1,SIZE_OF_GRID) for i in range(0,HOW_MANY_NUMBERS_TO_DISPLAY-1)]

# Display each number number in its random x,y location
display_grid(x, y)

# Wait for a key
input("")        

# Move a random number left or right
num_to_move = randint(0,HOW_MANY_NUMBERS_TO_DISPLAY-1)

if (getrandbits(1) == 1):
    x[num_to_move] = x[num_to_move] + 1
    print("moving %s right" % num_to_move)
else:
    x[num_to_move] = x[num_to_move] - 1
    print("moving %s left" % num_to_move)

display_grid(x, y)
time.sleep(0.5)

os.system('clear')
print("WHICH NUMBER MOVED")
user_guess = input("")

if (user_guess == (num_to_move+1)):
    print("WELL SPIED!")
    score += 1
    print("YOU NOW HAVE %S POINTS" % score)
    print("\nPRESS A KEY")
