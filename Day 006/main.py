print('==========================================')
print('| Day 006 - Project: Reeborgs Maze       |')
print('==========================================')


# Solution to Maze at https://reeborg.ca/

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if at_goal():
        done()
    elif right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
