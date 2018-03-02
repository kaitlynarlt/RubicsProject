#this is meant to be just a general template for a state and the set of moves
#for the rubics cube. Changes may be made as neccessary


Class State:
    def __init__(self, front, back, left, right, top, bottom):
        self.front = front
        self.back = back
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
    
    def __str__(self):
        toReturn = ''
        toReturn
        
       
# example string representation
#          + - - +
#          | T T |
#          | T T |
#    + - - + - - + - - + - - +
#    | L L | F F | R R | B B |
#    | L L | F F | R R | B B |
#    + - - + - - + - - + - - +
#          | U U |
#          | U U |
#          + - - |