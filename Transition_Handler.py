from Cube import State
from Cube import OPERATORS

Q_VALUES = {}
CUBE = State()
FEATURES_VISITED = []
ACTIONS = list(OPERATORS)
ACTIONS.append("Exit")
PREVIOUS_STATE_FEATURES = CUBE.features().__str__()
LAST_ACTION = None
INNITIAL_STATE_STRING = CUBE.features().__str__()
ALPHA = 0.5 # Learning Rate
EPSILON = 0.5 # Chance of Straying
GAMMA = 1.0 # discount (1.0 for no discount but we can change this later if we want)

POLICY = {}

def handle_transition(action, new_state, reward):
    
    global PREVIOUS_STATE_FEATURES, Q_VALUES, ALPHA
    
    previous_state = PREVIOUS_STATE_FEATURES
    
    if not (previous_state, action) in Q_VALUES:
        Q_VALUES[(previous_state, action)] = 0.0
    
    alpha_remainder = 1.0 - ALPHA
    
    Q_VALUES[(previous_state, action)] = (Q_VALUES[(previous_state, action)]*alpha_remainder) + (reward*ALPHA)
    FEATURES_VISITED.append(previous_state)
    
    PREVIOUS_STATE_FEATURES = new_state.features().__str__()
    LAST_ACTION = action

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
    
    POLICY[INNITIAL_STATE_STRING] = "Exit"
    
    return POLICY

