from Cube import State
from Cube import COLORS
from Cube import OPERATORS
import random as rand

ACTIONS = None
Q_VALS = {}
CUBE

def setup():
    global Q_VALS, CUBE, LAST_ACTION, LAST_STATE, GAMMA, STEP, ACTIONS
    # global WEIGHTS
    ACTIONS = [op for op in OPERATORS]
    ACTIONS.append("Exit")
    SIDES = []
    Q_VALS = {}
    FEATURES = []
    WEIGHTS = []
    LAST_STATE = None
    LAST_ACTION = None
    GAMMA = 0.5
    STEP = 1  # not really sure what this is for or if its necessary
    #STEP is for keeping track of the number of moves you have made

    for color in COLORS:
        side = [[color, color], [color, color]]
        SIDES.append(side)

    # Rubiks cube state, initialized in goal state

    CUBE = State(SIDES[0], SIDES[1], SIDES[2], SIDES[3], SIDES[4], SIDES[5])

    for i in range(10): #mix up the cube
        action = rand.sample(ACTIONS[0:12], 1)[0]
        CUBE = action.apply(INIT)

    for op in OPERATORS:
        Q_VALS[(INIT, op)] = 0

    for i in range(len(FEATURES)):
        WEIGHTS[i] = 1


def controller(turn_lim):
    global CUBE, LAST_STATE, LAST_ACTION
    turns = 0
    LAST_STATE = CUBE
    action = rand.sample(ACTIONS[0:12], 1)[0]
    LAST_ACTION = action
    while not action == "Exit" or turns == turn_lim:
        turns += 1
        r = 0
        s_prime = LAST_ACTION.apply(LAST_STATE)
        print(str(s_prime))
        if s_prime.is_goal_state():
            r = 100
            action = "Exit"
        else:
            action = choose_next_action(s_prime)
            update_weights(s_prime, action, r)
            update_q_val(s_prime)
            LAST_STATE = s_prime
            LAST_ACTION = action


def update_weights(s_prime, new_action, r):
    global WEIGHTS
    # δ= r+γQw(s',a')-Qw(s,a)
    delta = r + GAMMA * Q_VALS[(s_prime, new_action)] - Q_VALS[(LAST_STATE, LAST_ACTION)]
    #wi ←wi + ηδFi(s,a)
    for i in range(len(WEIGHTS)):
        WEIGHTS[i] = WEIGHTS[i] + STEP * delta * s_prime.features[i]  #the features based on (LAST_STATE, LAST_ACTION)


def update_q_val(s_prime):
    global Q_VALS
    # Qw(s,a) = w0+w1 F1(s,a) + ...+ wn Fn(s,a)
    products = []
    for i in range(len(WEIGHTS)):
        products.append(WEIGHTS[i] * s_prime.features[i])
    total = 0
    for elem in products:
        total += elem

    Q_VALS[(LAST_STATE, LAST_ACTION)] = total


def choose_next_action(s_prime):
    global LAST_ACTION, LAST_STATE

    # choose an action 'new_action' based on new Q values
    max_qval = 0
    best_action = rand.sample(ACTIONS[0:12], 1)[0]
    for a in ACTIONS[0:12]:
        if Q_VALS[s_prime, a] > max_qval:  # need to handle if there is no q val yet
            max_qval = Q_VALS[s_prime, a]
            best_action = a
    return best_action
