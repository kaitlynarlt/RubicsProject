#this is meant to be just a general template for a state and the set of moves
#for the rubics cube. Changes may be made as neccessary

#colors
R = 'R'  # red
B = 'B'  # blue
G = 'G'  # green
Y = 'Y'  # yellow
O = 'O'  # orange
W = 'W'  # white


Class State:
    def __init__(self, front, back, left, right, top, under):
        self.front = front
        self.back = back
        self.left = left
        self.right = right
        self.top = top
        self.under = under
    
    def __str__(self):
        toReturn = ''
        toReturn += '      + - - +\n' 
        toReturn += '      | ' + self.top[0][0] + ' ' + slef.top[0][1] + ' |\n'
        toReturn += '      | ' + self.top[1][0] + ' ' + self.top[1][1] + ' |\n'
        toReturn += '+ - - + - - + - - + - - +\n'
        toReturn += '| ' + self.left[0][0] + ' ' + self.left[0][1] + ' | ' + self.front[0][0] + ' ' + self.front[0][1] + ' | ' + self.right[0][0] + ' ' + self.right[0][1] + ' | ' + self.back[0][0] + ' ' + self.back[0][1] + ' |\n'
        toReturn += '| ' + self.left[1][0] + ' ' + self.left[1][1] + ' | ' + self.front[1][0] + ' ' + self.front[1][1] + ' | ' + self.right[1][0] + ' ' + self.right[1][1] + ' | ' + self.back[1][0] + ' ' + self.back[1][1] + ' |\n'
        toReturn += '+ - - + - - + - - + - - +\n'
        toReturn += '      | ' + self.under[0][0] + ' ' + slef.under[0][1] + ' |\n'
        toReturn += '      | ' + self.under[1][0] + ' ' + self.under[1][1] + ' |\n'
        toReturn += '      + - - +\n' 



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
#          + - - +
#
# slightly deformed but with indicies for the faces
#          +  -   -  +
#          | T00 T01 |
#          | T10 T11 |
#+  -   -  +  -   -  +  -   -  +  -   -  +
#| L00 L01 | F00 F01 | R00 R01 | B00 B01 |
#| L10 L11 | F10 F11 | R10 R11 | B10 B11 |
#+  -   -  +  -   -  +  -   -  +  -   -  +
#          | U00 U01 |
#          | U10 U11 |
#          +  -   -  +