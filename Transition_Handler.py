from Cube import State
from Cube import OPERATORS

Q_VALUES = {}
CUBE = State()
FEATURES_VISITED = []
ACTIONS = list(OPERATORS)
ACTIONS.append("Exit")
PREVIOUS_STATE_FEATURES = None
LAST_ACTION = None

ALPHA = 0.5 # Learning Rate
EPSILON = 0.5 # Chance of Straying
GAMMA = 1.0 # discount (1.0 for no discount but we can change this later if we want)

POLICY = {}

def extract_policy():

