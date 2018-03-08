from Cube import State
from Cube import OPERATORS
from random import uniform
from random import randint

# map for the Q values
# the keys are in the form (feature_list, operator)
# feature_list is the string representation of the list returned from Cube.features()
# operator is the operator object coresponding to that action
Q_VALUES = {}

# building a set for the entire state space would be very time comsuming so we
# just record the states that we have visited during our traversal.
FEATURES_VISITED = [] 

CUBE = State() # the rubik cube state
ACTIONS = OPERATORS # the set of all posible actions from any state

PREVIOUS_STATE_FEATURES = CUBE.features().__str__() # the string representation of the previous state's features
LAST_ACTION = None # the action taken from the previous state
INNITIAL_STATE_STRING = CUBE.features().__str__() # string representation of the solved cube

ALPHA = 0.5 # Learning Rate
EPSILON = 0.5 # Chance of Straying
GAMMA = 1.0 # discount (1.0 for no discount but we can change this later if we want) I'm not using it in this implementation

POLICY = {} # used to extract the optimal policy
Q_VALUES[(INNITIAL_STATE_STRING, ACTIONS[len(ACTIONS)-1])] = 100.0 # sets the goal state reward to 100

# For the sake of expiditing the learning a bit, I implemented a side function
# that will trace back over the path traversed from the start to goal and update
# the q values accordingly with alpha and gamma.
# The algorithm/implementation is fairly similar to feeding back on a neural net
USE_FEEDBACK = False # set to true if you want to use the feedback function
PATH = [] # path traversed from goal to start (in that order)


# has the same usage and features as the handle_transition function from asignment 5
def handle_transition(action, new_state, reward):
    
    global PREVIOUS_STATE_FEATURES, Q_VALUES, ALPHA, PATH
    
    #get the string representation of the previous state's features
    previous_state = PREVIOUS_STATE_FEATURES
    
    # add non-existent keys to the Q_VALUES set
    if not (previous_state, action) in Q_VALUES:
        Q_VALUES[(previous_state, action)] = 0.0
    
    # go ahead and calculate the remainder from alpha
    alpha_remainder = 1.0 - ALPHA
    
    # update the Q_Value
    Q_VALUES[(previous_state, action)] = (Q_VALUES[(previous_state, action)]*alpha_remainder) + (reward*ALPHA)
    
    # add the current state to the list of known states in the state space
    if not previous_state in FEATURES_VISITED:
        FEATURES_VISITED.append(previous_state)
    
    # for using the feedback function mentioned in the global variable section
    if USE_FEEDBACK:
        PATH.insert(0,(previous_state, action))
        if new_state.is_goal_state():
            update_values()
    
    # update globals
    PREVIOUS_STATE_FEATURES = new_state.features().__str__()
    LAST_ACTION = action

# this is the feedback function. I'm not going to include any commenting on it
# for the time being
def update_values():
    
    global PATH, Q_VALUES
    
    base_reward = 100.0
    current_reward = base_reward
    alpha_remainder = 1.0 - ALPHA
    
    # trace backwards over the path discounting the reward/value as you go
    for element in PATH:
        if not element in Q_VALUES:
            Q_VALUES[element] = 0.0
        current_reward = (Q_VALUES[element]*alpha_remainder) + (current_reward*ALPHA)
        Q_VALUES[element] = current_reward
    
# has the same usage and features as the chose_next_action function from asignment 5
def chose_next_action(current_state, reward):
    
    global Q_VALUES, OPERATORS, PREVIOUS_STATE_FEATURES
    global LAST_ACTION, ALPHA, EPSILON
    
    # first is to handle transition and update Q vals
    # it also handles updating the known state space
    handle_transition(LAST_ACTION, current_state, reward)
    
    # if the current state is a goal state, exit otherwhise don't consider the exit operator
    # note: the exit operator is always the last operator in the list
    if current_state.is_goal_state():
        handle_transition(OPERATORS[len(OPERATORS)-1], current_state, 100.0)
        return OPERATORS[len(OPERATORS)-1]
    
    # get the string representation of the feature list for the current state
    current_state_rep = current_state.features().__str__()
    
    # if we haven't been to this state before, initialize the Q values for all of
    # the actions posible from that state
    if not current_state_rep in FEATURES_VISITED:
        for action in OPERATORS:
            if not (current_state_rep, action) in Q_VALUES:
                Q_VALUES[(current_state_rep, action)] = 0.0
    
    # determine whether or not to explore
    chance = uniform(0.0, 1.0)
    
    if chance < EPSILON: # go exploring
        # pick a random action and take it
        index = randint(0, len(OPERATORS)-2)
        LAST_ACTION = OPERATORS[index]
        return LAST_ACTION
        
    else: # stick to the policy
        
        #get the best action from the current state
        
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
        
        # update globals
        LAST_ACTION = best_action
        
        
        return best_action

# has the same usage as the extract_policy function from asignment 5
# only returns the policy for states that have been visited
def extract_policy():
    
    global FEATURES_VISITED, ACTIONS, Q_VALUES, POLICY
    
    # get the optimal action from every state that has been visited
    for state in FEATURES_VISITED:
        
        best_action = ACTIONS[0]
        
        if not (state, best_action) in Q_VALUES:
            Q_VALUES[(state, best_action)] = 0.0
            
        best_action_value = Q_VALUES[(state, best_action)]
        
        for i in range(len(ACTIONS)-2):
            if not (state, ACTIONS[i]) in Q_VALUES:
                Q_VALUES[(state, ACTIONS[i])] = 0.0
                
            if Q_VALUES[(state, ACTIONS[i])] > best_action_value:
                best_action = ACTIONS[i]
                best_action_value = Q_VALUES[(state, best_action)]
                
        POLICY[state] = best_action
    
    # ensures that the policy will include the exit action only for goal states
    POLICY[INNITIAL_STATE_STRING] = ACTIONS[len(ACTIONS)-1]
    
    return POLICY

