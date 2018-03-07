
from Cube import State
from Cube import OPERATORS
from Transition_Handler import handle_transition
from Transition_Handler import extract_policy
#from Transition_Handler import HashableList

STATE = State()

USER_DRIVEN = False
RUNNING = True

#for user driven
def take_turn():
    
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
    reward = 0
    if next_operator == OPERATORS[len(OPERATORS)-1] and STATE.is_goal_state():
        reward = 100
    handle_transition(next_operator, STATE, reward)

    
while RUNNING:
    take_turn()

policy = extract_policy()

for op in policy:
    print(op+" : "+str(policy[op]))
