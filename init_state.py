"""
Proposed state representation for the cube
"""

RE = 'RE'  # red
BL = 'BL'  # blue
G = 'G'  # green
Y = 'Y'  # yellow
O = 'O'  # orange
W = 'W'  # white

# this is a solvable initial state
initial = {'F': [[RE, RE], [O, O]],  # front face
           'U': [[W, Y], [W, Y]],  # "up" (top) face
           'B': [[RE, RE], [O, O]],  # back face
           'L': [[BL, G], [G, BL]],  # left face
           'D': [[Y, W], [Y, W]],  # "down" (bottom) face
           'R': [[G, BL], [BL, G]]}  # right face

# to solve: F2, R2, U2 <- check this
# the action F2 means to rotate the F (front) face 180 degrees etc.