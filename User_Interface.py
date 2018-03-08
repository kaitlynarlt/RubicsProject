
from Cube import State
from Cube import Operator
from Cube import OPERATORS
from Transition_Handler import handle_transition
from Transition_Handler import extract_policy
from Transition_Handler import chose_next_action
from Transition_Handler import ALPHA
from Transition_Handler import EPSILON
from Transition_Handler import Q_VALUES
from random import randint
#from Transition_Handler import HashableList

STATE = State()

USER_DRIVEN = False
RUNNING = True

#for user driven
def take_turn_ui():
    
    global STATE, OPERATORS, RUNNING
    
    # show user the stuff
    print("Current State:")
    print(STATE)
    
    print("Available Actions (press coresponding key to invoke action):")
    for i in range(len(OPERATORS)-1):
        print("["+str(i)+"] : "+OPERATORS[i].name)
    print("Enter value not listed above to quit")
    # get user input
    
    next_move = int(input())
    if next_move >= len(OPERATORS) or next_move < 0:
        print(str(next_move))
        RUNNING = False
        return
    
    # translate user input
    next_operator = OPERATORS[next_move]
    next_operator.apply(STATE)
    
    # push update all the stuff
    handle_transition(next_operator, STATE, get_reward(STATE))

def take_turn_ai():
    
    global STATE, ALPHA
    
    if STATE.is_goal_state():
        print("The cube is at a goal state. How many actions would you like to take to mix up the cube:")

        ui = int(input())
        shuffle_cube(ui)
        
        print("Current Initial State:")
        print(STATE)
    
    print("")
    
    print("Set Alpha to:")
    ALPHA = float(input())
    
    print("Set Epsilon to:")
    EPSILON = float(input())
    print()
    print("How many turns would you like the ai to take?:")
    print("[0]: One turn")
    print("[1]: Ten turns")
    print("[2]: One hundred turns")
    print("[3]: Go until it finds the goal once")
    print("[4]: Go until it finds the goal three times")
    print("[5]: Go until it finds the goal five times")
    print("[6]: Go until it finds the goal ten times")
    print("[7]: Go until it finds the goal one hundred times")
    print("[8]: Go until it finds the goal one thousand times")
    print("Enter any other number to quit")
    
    next_move = int(input())
    num_of_actions_to_shuffle = 23
    
    if next_move >= 3:
        print("How many actions would you like to take to shuffle the cube each time?:")
        
        num_of_actions_to_shuffle = int(input())
    
    if next_move == 0:
        next_action = chose_next_action(STATE, get_reward(STATE))
        next_action.apply(STATE)
    elif next_move == 1:
        for i in range(10):
            next_action = chose_next_action(STATE, get_reward(STATE))
            next_action.apply(STATE)
            if STATE.is_goal_state():
                next_action = chose_next_action(STATE, get_reward(STATE))
                next_action.apply(STATE)
                break
    elif next_move == 2:
        for i in range(100):
            next_action = chose_next_action(STATE, get_reward(STATE))
            next_action.apply(STATE)
            if STATE.is_goal_state():
                next_action = chose_next_action(STATE, get_reward(STATE))
                next_action.apply(STATE)
                break
    elif next_move == 3:
        if STATE.is_goal_state():
            shuffle_cube(num_of_actions_to_shuffle)
        while not STATE.is_goal_state():
            next_action = chose_next_action(STATE, get_reward(STATE))
            next_action.apply(STATE)
        next_action = chose_next_action(STATE, get_reward(STATE))
        next_action.apply(STATE)
    elif next_move == 4:
        for i in range(3):
            if STATE.is_goal_state():
                shuffle_cube(num_of_actions_to_shuffle)
            while not STATE.is_goal_state():
                next_action = chose_next_action(STATE, get_reward(STATE))
                next_action.apply(STATE)
            next_action = chose_next_action(STATE, get_reward(STATE))
            next_action.apply(STATE)
    elif next_move == 5:
        for i in range(5):
            if STATE.is_goal_state():
                shuffle_cube(num_of_actions_to_shuffle)
            while not STATE.is_goal_state():
                next_action = chose_next_action(STATE, get_reward(STATE))
                next_action.apply(STATE)
            next_action = chose_next_action(STATE, get_reward(STATE))
            next_action.apply(STATE)
    elif next_move == 6:
        for i in range(10):
            if STATE.is_goal_state():
                shuffle_cube(num_of_actions_to_shuffle)
            while not STATE.is_goal_state():
                next_action = chose_next_action(STATE, get_reward(STATE))
                next_action.apply(STATE)
            next_action = chose_next_action(STATE, get_reward(STATE))
            next_action.apply(STATE)
    elif next_move == 7:
        for i in range(100):
            if STATE.is_goal_state():
                shuffle_cube(num_of_actions_to_shuffle)
            while not STATE.is_goal_state():
                next_action = chose_next_action(STATE, get_reward(STATE))
                next_action.apply(STATE)
            next_action = chose_next_action(STATE, get_reward(STATE))
            next_action.apply(STATE)
    elif next_move == 8:
        for i in range(1000):
            if STATE.is_goal_state():
                shuffle_cube(num_of_actions_to_shuffle)
            while not STATE.is_goal_state():
                next_action = chose_next_action(STATE, get_reward(STATE))
                next_action.apply(STATE)
            next_action = chose_next_action(STATE, get_reward(STATE))
            next_action.apply(STATE)
    
    print(STATE)
    
    print("NEW POLICY:")
    print_policy()
    
        
def get_reward(state):
    reward = 0
    if STATE.is_goal_state():
        reward = 100
    return reward

def shuffle_cube(num_of_actions):
    
    global STATE, OPERATORS
    if num_of_actions < 0:
        num_of_actions *= -1

    for i in range(num_of_actions):
        OPERATORS[randint(0, len(OPERATORS)-2)].apply(STATE)

def print_policy():
    
    global Q_VALUES
    
    policy = extract_policy()
    for op in policy:
        print(op + " : " + str(policy[op]) + " : " + str(Q_VALUES[(op,policy[op])]))

print("Welcome to the Rubiks Cube interface!")
print("How many actions would you like to take to mix up the cube:")

ui = int(input())
shuffle_cube(ui)

print("Starting state")
print(STATE)
print("Which version would you like to use?:")
print("[0]: User controled version")
print("[1]: Computer controled version")
print("Enter any other number to quit:")

ui = int(input())
if ui == 1:
    while RUNNING:
        take_turn_ai()
        
        print()
        print("- - - - - - - - - - - - - - - - - - -")
        print("    Would you like to continue?:")
        print("            [0]: Yes")
        print("            [1]: No")
        ui = int(input("               "))
            
        print("- - - - - - - - - - - - - - - - - - -")
        print()

        if ui != 0:
            RUNNING = False

elif ui == 0:
    while RUNNING:
        take_turn_ui()
        
        print()
        print("- - - - - - - - - - - - - - - - - - -")
        print("    Would you like to continue?:")
        print("            [0]: Yes")
        print("            [1]: No")
        
        ui = int(input("               "))
            
        print("- - - - - - - - - - - - - - - - - - -")
        print()

        if ui != 0:
            RUNNING = False

print("Final state:")
print(STATE)
print("Final policy:")
print_policy()
    
print()
print("Thank you for using the Rubiks Cube interface!")