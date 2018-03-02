from Cube import State
from Cube import COLORS


SIDES = []

for color in COLORS:
    side = [[color, color], [color, color]]
    SIDES.append(side)

# Rubics cube state, initialized in goal state
CUBE = State(SIDES[0],SIDES[1],SIDES[2],SIDES[3],SIDES[4],SIDES[5])

# list of all posible moves
OPERATORS = []

#adding the 12 posible moves to the set of operators
OPERATORS.append(lambda: CUBE.rotate_right())
OPERATORS.append(lambda: CUBE.rotate_right_inverse())
OPERATORS.append(lambda: CUBE.rotate_left())
OPERATORS.append(lambda: CUBE.rotate_left_inverse())
OPERATORS.append(lambda: CUBE.rotate_back())
OPERATORS.append(lambda: CUBE.rotate_back_inverse())
OPERATORS.append(lambda: CUBE.rotate_under())
OPERATORS.append(lambda: CUBE.rotate_under_inverse())
OPERATORS.append(lambda: CUBE.rotate_front())
OPERATORS.append(lambda: CUBE.rotate_front_inverse())
OPERATORS.append(lambda: CUBE.rotate_top())
OPERATORS.append(lambda: CUBE.rotate_top_inverse())


# USAGES

# print the current state:
# print(CUBE)

# use a particular operator:
# OPERATORS[i]()

# check if the current state is a goal state
# CUBE.is_goal_state()