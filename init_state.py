"""
Proposed state representation for the cube
"""

RE = 'RE'  # red
BL = 'BL'  # blue
G = 'G'  # green
Y = 'Y'  # yellow
O = 'O'  # orange
W = 'W'  # white

# this is a solvable initial state, to get there from
# the goal state, use U2, R2, F2
initial = {'F': [[O, O], [RE, RE]],  # front face
           'U': [[Y, W], [Y, W]],  # "up" (top) face
           'B': [[O, O], [RE, RE]],  # back face
           'L': [[BL, G], [G, BL]],  # left face
           'D': [[W, Y], [W, Y]],  # "down" (bottom) face
           'R': [[G, BL], [BL, G]]}  # right face

# to solve: F2, R2, U2 <- check this
# the action F2 means to rotate the F (front) face 180 degrees etc.