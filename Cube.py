#this is meant to be just a general template for a state and the set of moves
#for the rubics cube. Changes may be made as neccessary

#colors
R = 'R'  # red
B = 'B'  # blue
G = 'G'  # green
Y = 'Y'  # yellow
O = 'O'  # orange
W = 'W'  # white


class State:
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
        return toReturn

    def __hash__(self):
        return (self.__str__()).__hash__()
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
    
    #below are the 12 possible moves coresponding to the moves in the image https://smhttp-ssl-62406.nexcesscdn.net/resources/images/solve-it/2x2-moves.jpg
    def rotate_right(self): #'R' in image
        #rotate the strip
        #save f
        temp1 = self.front[0][1]
        temp2 = self.front[1][1]
        #move u->f
        self.front[0][1] = self.under[0][1]
        self.front[1][1] = self.under[1][1]
        #move b->u
        self.under[0][1] = self.back[1][0]
        self.under[1][1] = self.back[0][0]
        #move t->b
        self.back[1][0] = self.top[0][1]
        self.back[0][0] = self.top[1][1]
        #move f->t
        self.top[0][1] = temp1
        self.top[1][1] = temp2
        
        #rotate the side
        temp1 = self.right[0][0]
        self.right[0][0] = self.right[1][0]
        self.right[1][0] = self.right[1][1]
        self.right[1][1] = self.right[0][1]
        self.right[0][1] = temp1
        
    def rotate_right_inverse(self): #'Ri' in image
        #rotate the strip
        #save f
        temp1 = self.front[0][1]
        temp2 = self.front[1][1]
        #move t->f
        self.front[0][1] = self.top[0][1]
        self.front[1][1] = self.top[1][1]
        #move b->t
        self.top[0][1] = self.back[1][0]
        self.top[1][1] = self.back[0][0]
        #move u->b
        self.back[1][0] = self.under[0][1]
        self.back[0][0] = self.under[1][1]
        #move f->u
        self.under[0][1] = temp1
        self.under[1][1] = temp2
        
        #rotate the side
        temp1 = self.right[0][0]
        self.right[0][0] = self.right[0][1]
        self.right[0][1] = self.right[1][1]
        self.right[1][1] = self.right[1][0]
        self.right[1][0] = temp1
        
    def rotate_left(self): #'L' in image
        #rotate the strip
        #save f
        temp1 = self.front[0][0]
        temp2 = self.front[1][0]
        #move t->f
        self.front[0][0] = self.top[0][0]
        self.front[1][0] = self.top[1][0]
        #move b->t
        self.top[0][0] = self.back[1][1]
        self.top[1][0] = self.back[0][1]
        #move u->b
        self.back[1][1] = self.under[0][0]
        self.back[0][1] = self.under[1][0]
        #move f->u
        self.under[0][0] = temp1
        self.under[1][0] = temp2
        
        #rotate the side
        temp1 = self.left[0][0]
        self.left[0][0] = self.left[1][0]
        self.left[1][0] = self.left[1][1]
        self.left[1][1] = self.left[0][1]
        self.left[0][1] = temp1
        
    def rotate_left_inverse(self): #'Li' in image
        #rotate the strip
        #save f
        temp1 = self.front[0][0]
        temp2 = self.front[1][0]
        #move u->f
        self.front[0][0] = self.under[0][0]
        self.front[1][0] = self.under[1][0]
        #move b->u
        self.under[0][0] = self.back[1][1]
        self.under[1][0] = self.back[0][1]
        #move t->b
        self.back[1][1] = self.top[0][0]
        self.back[0][1] = self.top[1][0]
        #move f->t
        self.top[0][0] = temp1
        self.top[1][0] = temp2
        
        #rotate the side
        temp1 = self.left[0][0]
        self.left[0][0] = self.left[0][1]
        self.left[0][1] = self.left[1][1]
        self.left[1][1] = self.left[1][0]
        self.left[1][0] = temp1
        
    def rotate_back(self): #'B' in image
        #rotate the strip
        #save t
        temp1 = self.top[0][0]
        temp2 = self.top[0][1]
        #move r->t
        self.top[0][0] = self.right[0][1]
        self.top[0][1] = self.right[1][1]
        #move u->r
        self.right[0][1] = self.under[1][1]
        self.right[1][1] = self.under[1][0]
        #move l->u
        self.under[1][1] = self.left[1][0]
        self.under[1][0] = self.left[0][0]
        #move t->l
        self.left[1][0] = temp1
        self.left[0][0] = temp2
        
        #rotate the side
        temp1 = self.back[0][0]
        self.back[0][0] = self.back[1][0]
        self.back[1][0] = self.back[1][1]
        self.back[1][1] = self.back[0][1]
        self.back[0][1] = temp1
        
    def rotate_back_inverse(self): #'Bi' in image
        #rotate the strip
        #save t
        temp1 = self.top[0][0]
        temp2 = self.top[0][1]
        #move l->t
        self.top[0][0] = self.left[1][0]
        self.top[0][1] = self.left[0][0]
        #move u->l
        self.left[1][0] = self.under[1][1]
        self.left[0][0] = self.under[1][0]
        #move r->u
        self.under[1][1] = self.right[0][1]
        self.under[1][0] = self.right[1][1]
        #move t->r
        self.right[0][1] = temp1
        self.right[1][1] = temp2
        
        #rotate the side
        temp1 = self.back[0][0]
        self.back[0][0] = self.back[0][1]
        self.back[0][1] = self.back[1][1]
        self.back[1][1] = self.back[1][0]
        self.back[1][0] = temp1
        
    def rotate_under(self): #'D' in image
        #rotate the strip
        #save f
        temp1 = self.front[1][0]
        temp2 = self.front[1][1]
        #move l->f
        self.front[1][0] = self.left[1][0]
        self.front[1][1] = self.left[1][1]
        #move b->l
        self.left[1][0] = self.back[1][0]
        self.left[1][1] = self.back[1][1]
        #move r->b
        self.back[1][0] = self.right[1][0]
        self.back[1][1] = self.right[1][1]
        #move f->r
        self.right[1][0] = temp1
        self.right[1][1] = temp2
        
        #rotate the side
        temp1 = self.under[0][0]
        self.under[0][0] = self.under[1][0]
        self.under[1][0] = self.under[1][1]
        self.under[1][1] = self.under[0][1]
        self.under[0][1] = temp1
        
    def rotate_under_inverse(self): #'Di' in image
        #rotate the strip
        #save f
        temp1 = self.front[1][0]
        temp2 = self.front[1][1]
        #move r->f
        self.front[1][0] = self.right[1][0]
        self.front[1][1] = self.right[1][1]
        #move b->r
        self.right[1][0] = self.back[1][0]
        self.right[1][1] = self.back[1][1]
        #move l->b
        self.back[1][0] = self.left[1][0]
        self.back[1][1] = self.left[1][1]
        #move f->l
        self.left[1][0] = temp1
        self.left[1][1] = temp2
        
        #rotate the side
        temp1 = self.under[0][0]
        self.under[0][0] = self.under[0][1]
        self.under[0][1] = self.under[1][1]
        self.under[1][1] = self.under[1][0]
        self.under[1][0] = temp1
    
    def rotate_front(self): #'F' in image
        #rotate the strip
        #save t
        temp1 = self.top[1][0]
        temp2 = self.top[1][1]
        #move l->t
        self.top[1][0] = self.left[1][1]
        self.top[1][1] = self.left[0][1]
        #move u->l
        self.left[1][1] = self.under[0][1]
        self.left[0][1] = self.under[0][0]
        #move r->u
        self.under[0][1] = self.right[0][0]
        self.under[0][0] = self.right[1][0]
        #move t->r
        self.right[0][0] = temp1
        self.right[1][0] = temp2
        
        #rotate the side
        temp1 = self.front[0][0]
        self.front[0][0] = self.front[1][0]
        self.front[1][0] = self.front[1][1]
        self.front[1][1] = self.front[0][1]
        self.front[0][1] = temp1
        
    def rotate_front_inverse(self): #'Fi' in image
        #rotate the strip
        #save t
        temp1 = self.top[1][0]
        temp2 = self.top[1][1]
        #move l->t
        self.top[1][0] = self.left[1][1]
        self.top[1][1] = self.left[0][1]
        #move u->l
        self.left[1][1] = self.under[0][1]
        self.left[0][1] = self.under[0][0]
        #move r->u
        self.under[0][1] = self.right[0][0]
        self.under[0][0] = self.right[1][0]
        #move t->r
        self.right[0][0] = temp1
        self.right[1][0] = temp2
        
        #rotate the side
        temp1 = self.front[0][0]
        self.front[0][0] = self.front[1][0]
        self.front[1][0] = self.front[1][1]
        self.front[1][1] = self.front[0][1]
        self.front[0][1] = temp1
        
    def rotate_top(self): #'U' in image
        #rotate the strip
        #save f
        temp1 = self.front[0][0]
        temp2 = self.front[0][1]
        #move r->f
        self.front[0][0] = self.right[0][0]
        self.front[0][1] = self.right[0][1]
        #move b->r
        self.right[0][0] = self.back[0][0]
        self.right[0][1] = self.back[0][1]
        #move l->b
        self.back[0][0] = self.left[0][0]
        self.back[0][1] = self.left[0][1]
        #move f->l
        self.left[0][0] = tmep1
        self.left[0][1] = temp2
        
        #rotate the side
        temp1 = self.top[0][0]
        self.top[0][0] = self.top[1][0]
        self.top[1][0] = self.top[1][1]
        self.top[1][1] = self.top[0][1]
        self.top[0][1] = temp1
        
    def rotate_top_inverse(self): #'Ui' in image
        #rotate the strip
        #save f
        temp1 = self.front[0][0]
        temp2 = self.front[0][1]
        #move l->f
        self.front[0][0] = self.left[0][0]
        self.front[0][1] = self.left[0][1]
        #move b->l
        self.left[0][0] = self.back[0][0]
        self.left[0][1] = self.back[0][1]
        #move r->b
        self.back[0][0] = self.right[0][0]
        self.back[0][1] = self.right[0][1]
        #move f->r
        self.right[0][0] = temp1
        self.right[0][1] = temp2
        
        #rotate the side
        temp1 = self.top[0][0]
        self.top[0][0] = self.top[0][1]
        self.top[0][1] = self.top[1][1]
        self.top[1][1] = self.top[1][0]
        self.top[1][0] = temp1