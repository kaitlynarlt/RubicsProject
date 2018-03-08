from Cube import State
from Cube import OPERATORS
from random import uniform
from random import randint

Q_VALUES = {}
CUBE = State()
FEATURES_VISITED = []
ACTIONS = OPERATORS
PREVIOUS_STATE_FEATURES = CUBE.features().__str__()
LAST_ACTION = None
INNITIAL_STATE_STRING = CUBE.features().__str__()
ALPHA = 0.5 # Learning Rate
EPSILON = 0.5 # Chance of Straying
GAMMA = 1.0 # discount (1.0 for no discount but we can change this later if we want) I'm not using it in this implementation

POLICY = {}

PATH = []

def handle_transition(action, new_state, reward):
    
    global PREVIOUS_STATE_FEATURES, Q_VALUES, ALPHA, PATH
    
    previous_state = PREVIOUS_STATE_FEATURES
    
    PATH.insert(0,(previous_state, action))
    if not (previous_state, action) in Q_VALUES:
        Q_VALUES[(previous_state, action)] = 0.0
    alpha_remainder = 1.0 - ALPHA
    
    Q_VALUES[(previous_state, action)] = (Q_VALUES[(previous_state, action)]*alpha_remainder) + (reward*ALPHA)
    if not previous_state in FEATURES_VISITED:
        FEATURES_VISITED.append(previous_state)
    
    if new_state.is_goal_state():
        update_values()
    
    PREVIOUS_STATE_FEATURES = new_state.features().__str__()
    LAST_ACTION = action

def update_values():
    
    global PATH, Q_VALUES
    
    base_reward = 100.0
    current_reward = base_reward
    alpha_remainder = 1.0 - ALPHA
    
    for element in PATH:
        if not element in Q_VALUES:
            Q_VALUES[element] = 0.0
        current_reward = (Q_VALUES[element]*alpha_remainder) + (current_reward*ALPHA)
        Q_VALUES[element] = current_reward
    
def chose_next_action(current_state, reward):
    
    global Q_VALUES, OPERATORS, PREVIOUS_STATE_FEATURES
    global LAST_ACTION, ALPHA, EPSILON
    
    # first is to handle transition and update Q vals
    # it also handles updating the known state space
    handle_transition(LAST_ACTION, current_state, reward)
    
    if current_state.is_goal_state():
        handle_transition(OPERATORS[len(OPERATORS)-1], current_state, 100.0)
        return OPERATORS[len(OPERATORS)-1]
    
    current_state_rep = current_state.features().__str__()
    
    if not current_state_rep in FEATURES_VISITED:
        for action in OPERATORS:
            if not (current_state_rep, action) in Q_VALUES:
                Q_VALUES[(current_state_rep, action)] = 0.0
    
    # determine whether or not to explore
    
    chance = uniform(0.0, 1.0)
    
    if chance < EPSILON:
        index = randint(0, len(OPERATORS)-1)
        LAST_ACTION = OPERATORS[index]
        return LAST_ACTION
    else:
        
        best_action = OPERATORS[0]
        
        if not (current_state_rep, best_action) in Q_VALUES:
            Q_VALUES[(current_state_rep, best_action)] = 0.0
            
        best_action_value = Q_VALUES[(current_state_rep, best_action)]
        
        for index in range(len(OPERATORS)-2):
            if not (current_state_rep, OPERATORS[index]) in Q_VALUES:
                Q_VALUES[(current_state_rep, OPERATORS[index])] = 0.0
                
            if Q_VALUES[(current_state_rep, OPERATORS[index])] > best_action_value:
                best_action = OPERATORS[index]
                best_action_value = Q_VALUES[(current_state_rep, best_action)]
        LAST_ACTION = best_action
        return best_action

def extract_policy():
    
    global FEATURES_VISITED, ACTIONS, Q_VALUES, POLICY
    
    for state in FEATURES_VISITED:
        
        best_action = ACTIONS[0]
        
        if not (state, best_action) in Q_VALUES:
            Q_VALUES[(state, best_action)] = 0.0
            
        best_action_value = Q_VALUES[(state, best_action)]
        
        for action in ACTIONS:
            if not (state, action) in Q_VALUES:
                Q_VALUES[(state, action)] = 0.0
                
            if Q_VALUES[(state, action)] > best_action_value:
                best_action = action
                best_action_value = Q_VALUES[(state, best_action)]
                
        POLICY[state] = best_action
    Q_VALUES[(INNITIAL_STATE_STRING, ACTIONS[len(ACTIONS)-1])] = 100.0
    POLICY[INNITIAL_STATE_STRING] = ACTIONS[len(ACTIONS)-1]
    
    return POLICY

