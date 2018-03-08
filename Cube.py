# this is meant to be just a general template for a state and the set of moves
# for the rubiks cube. Changes may be made as necessary

# colors
R = 'R'  # red
B = 'B'  # blue
G = 'G'  # green
Y = 'Y'  # yellow
O = 'O'  # orange
W = 'W'  # white

COLORS = [R, B, G, Y, O, W]
NOT_COLORS = [1, 2, 3, 4, 5, 6]


class State:
    def __init__(self):
        global R, B, G, Y, O, W
        self.front = [[R, R], [R, R]]
        self.back = [[B, B], [B, B]]
        self.left = [[G, G], [G, G]]
        self.right = [[Y, Y], [Y, Y]]
        self.top = [[O, O], [O, O]]
        self.under = [[W, W], [W, W]]

    def __str__(self):
        toReturn = ''
        toReturn += '      + - - +\n'
        toReturn += '      | ' + self.top[0][0] + ' ' + self.top[0][1] + ' |\n'
        toReturn += '      | ' + self.top[1][0] + ' ' + self.top[1][1] + ' |\n'
        toReturn += '+ - - + - - + - - + - - +\n'
        toReturn += '| ' + self.left[0][0] + ' ' + self.left[0][1] + ' | ' + self.front[0][0] + ' ' + self.front[0][
            1] + ' | ' + self.right[0][0] + ' ' + self.right[0][1] + ' | ' + self.back[0][0] + ' ' + self.back[0][
                        1] + ' |\n'
        toReturn += '| ' + self.left[1][0] + ' ' + self.left[1][1] + ' | ' + self.front[1][0] + ' ' + self.front[1][
            1] + ' | ' + self.right[1][0] + ' ' + self.right[1][1] + ' | ' + self.back[1][0] + ' ' + self.back[1][
                        1] + ' |\n'
        toReturn += '+ - - + - - + - - + - - +\n'
        toReturn += '      | ' + self.under[0][0] + ' ' + self.under[0][1] + ' |\n'
        toReturn += '      | ' + self.under[1][0] + ' ' + self.under[1][1] + ' |\n'
        toReturn += '      + - - +\n'
        return toReturn

    def __eq__(self, other):
        global COLORS
        # colors = list(COLORS)
        selfRep = []
        otherRep = []
        # front
        selfRep.append(self.front[0][0])
        otherRep.append(other.front[0][0])
        selfRep.append(self.front[0][1])
        otherRep.append(other.front[0][1])
        selfRep.append(self.front[1][0])
        otherRep.append(other.front[1][0])
        selfRep.append(self.front[1][1])
        otherRep.append(other.front[1][1])
        # left
        selfRep.append(self.left[0][0])
        otherRep.append(other.left[0][0])
        selfRep.append(self.left[0][1])
        otherRep.append(other.left[0][1])
        selfRep.append(self.left[1][0])
        otherRep.append(other.left[1][0])
        selfRep.append(self.left[1][1])
        otherRep.append(other.left[1][1])
        # back
        selfRep.append(self.back[0][0])
        otherRep.append(other.back[0][0])
        selfRep.append(self.back[0][1])
        otherRep.append(other.back[0][1])
        selfRep.append(self.back[1][0])
        otherRep.append(other.back[1][0])
        selfRep.append(self.back[1][1])
        otherRep.append(other.back[1][1])
        # right
        selfRep.append(self.right[0][0])
        otherRep.append(other.right[0][0])
        selfRep.append(self.right[0][1])
        otherRep.append(other.right[0][1])
        selfRep.append(self.right[1][0])
        otherRep.append(other.right[1][0])
        selfRep.append(self.right[1][1])
        otherRep.append(other.right[1][1])
        # top
        selfRep.append(self.top[0][0])
        otherRep.append(other.top[0][0])
        selfRep.append(self.top[0][1])
        otherRep.append(other.top[0][1])
        selfRep.append(self.top[1][0])
        otherRep.append(other.top[1][0])
        selfRep.append(self.top[1][1])
        otherRep.append(other.top[1][1])
        # under
        selfRep.append(self.under[0][0])
        otherRep.append(other.under[0][0])
        selfRep.append(self.under[0][1])
        otherRep.append(other.under[0][1])
        selfRep.append(self.under[1][0])
        otherRep.append(other.under[1][0])
        selfRep.append(self.under[1][1])
        otherRep.append(other.under[1][1])

        selfDict = {}
        otherDict = {}
        remainingColorsSelf = list(NOT_COLORS)
        remainingColorsOther = list(NOT_COLORS)
        for j in range(len(selfRep)):
            currentColorSelf = selfRep[j]
            currentColorOther = otherRep[j]

            if currentColorSelf in selfDict:
                selfRep[j] = selfDict[currentColorSelf]
            else:
                nextColorSelf = remainingColorsSelf.pop()
                selfDict[currentColorSelf] = nextColorSelf
                selfRep[j] = nextColorSelf

            if currentColorOther in otherDict:
                otherRep[j] = otherDict[currentColorOther]
            else:
                nextColorOther = remainingColorsOther.pop()
                otherDict[currentColorOther] = nextColorOther
                otherRep[j] = nextColorOther

        for k in range(len(selfRep)):
            if selfRep[k] != otherRep[k]:
                return False

        return True

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
    #           +  -   -  +
    #           | T00 T01 |
    #           | T10 T11 |
    # +  -   -  +  -   -  +  -   -  +  -   -  +
    # | L00 L01 | F00 F01 | R00 R01 | B00 B01 |
    # | L10 L11 | F10 F11 | R10 R11 | B10 B11 |
    # +  -   -  +  -   -  +  -   -  +  -   -  +
    #           | U00 U01 |
    #           | U10 U11 |
    #           +  -   -  +


    # below are the 12 possible moves coresponding to the moves in the image
    # https://smhttp-ssl-62406.nexcesscdn.net/resources/images/solve-it/2x2-moves.jpg
    # there are also 6 moves marked as 180 degree turns for their 90 degree counterparts
    

    def rotate_right_180(self):  # 'R' in image
        temp1 = self.front[0][1]
        temp2 = self.front[1][1]
        
        self.front[0][1] = self.back[1][0]
        self.front[1][1] = self.back[0][0]
        
        self.back[1][0] = temp1
        self.back[0][0] = temp2
        
        temp1 = self.top[0][1]
        temp2 = self.top[1][1]
        
        self.top[0][1] = self.under[0][1]
        self.top[1][1] = self.under[1][1]
        
        self.under[0][1] = temp1
        self.under[1][1] = temp2
        
        temp1 = self.right[0][0]
        self.right[0][0] = self.right[1][1]
        self.right[1][1] = temp1
        
        temp1 = self.right[0][1]
        self.right[0][1] = self.right[1][0]
        self.right[1][0] = temp1

    def rotate_left_180(self):
        
        temp1 = self.front[0][0]
        temp2 = self.front[1][0]
        
        self.front[0][0] = self.back[1][1]
        self.front[1][0] = self.back[0][1]
        
        self.back[1][1] = temp1
        self.back[0][1] = temp2
        
        temp1 = self.top[0][0]
        temp2 = self.top[1][0]
        
        self.top[0][0] = self.under[0][0]
        self.top[1][0] = self.under[1][0]
        
        self.under[0][0] = temp1
        self.under[1][0] = temp2
        
        temp1 = self.left[0][0]
        self.left[0][0] = self.left[1][1]
        self.left[1][1] = temp1
        
        temp1 = self.left[0][1]
        self.left[0][1] = self.left[1][0]
        self.left[1][0] = temp1

    def rotate_back_180(self):
        
        temp1 = self.top[0][0]
        temp2 = self.top[0][1]
        
        self.top[0][0] = self.under[1][1]
        self.top[0][1] = self.under[1][0]
        
        self.under[1][1] = temp1
        self.under[1][0] = temp2
        
        temp1 = self.left[0][0]
        temp2 = self.left[1][0]
        
        self.left[0][0] = self.right[1][1]
        self.left[1][0] = self.right[0][1]
        
        self.right[1][1] = temp1
        self.right[0][1] = temp2
        
        temp1 = self.back[0][0]
        self.back[0][0] = self.back[1][1]
        self.back[1][1] = temp1
        
        temp1 = self.back[0][1]
        self.back[0][1] = self.back[1][0]
        self.back[1][0] = temp1

    def rotate_under_180(self):
        
        temp1 = self.front[1][0]
        temp2 = self.front[1][1]
        
        self.front[1][0] = self.back[1][0]
        self.front[1][1] = self.back[1][1]
        
        self.back[1][0] = temp1
        self.back[1][1] = temp2
        
        temp1 = self.left[1][0]
        temp2 = self.left[1][1]
        
        self.left[1][0] = self.right[1][0]
        self.left[1][1] = self.right[1][1]
        
        self.right[1][0] = temp1
        self.right[1][1] = temp2
        
        temp1 = self.under[0][0]
        self.under[0][0] = self.under[1][1]
        self.under[1][1] = temp1
        
        temp1 = self.under[0][1]
        self.under[0][1] = self.under[1][0]
        self.under[1][0] = temp1

    def rotate_front_180(self):
        temp1 = self.top[1][0]
        temp2 = self.top[1][1]
        
        self.top[1][0] = self.under[0][1]
        self.top[1][1] = self.under[0][0]
        
        self.under[0][1] = temp1
        self.under[0][0] = temp2
        
        temp1 = self.left[0][1]
        temp2 = self.left[1][1]
        
        self.left[0][1] = self.right[1][0]
        self.left[1][1] = self.right[0][0]
        
        self.right[1][0] = temp1
        self.right[0][0] = temp2
        
        temp1 = self.front[0][0]
        self.front[0][0] = self.front[1][1]
        self.front[1][1] = temp1
        
        temp1 = self.front[0][1]
        self.front[0][1] = self.front[1][0]
        self.front[1][0] = temp1

    def rotate_top_180(self):
        
        temp1 = self.front[0][0]
        temp2 = self.front[0][1]
        
        self.front[0][0] = self.back[0][0]
        self.front[0][1] = self.back[0][1]
        
        self.back[0][0] = temp1
        self.back[0][1] = temp2
        
        temp1 = self.left[0][0]
        temp2 = self.left[0][1]
        
        self.left[0][0] = self.right[0][0]
        self.left[0][1] = self.right[0][1]
        
        self.right[0][0] = temp1
        self.right[0][1] = temp2
        
        temp1 = self.top[0][0]
        self.top[0][0] = self.top[1][1]
        self.top[1][1] = temp1
        
        temp1 = self.top[0][1]
        self.top[0][1] = self.top[1][0]
        self.top[1][0] = temp1



    def rotate_right(self):  # 'R' in image
        # rotate the strip
        # save f
        temp1 = self.front[0][1]
        temp2 = self.front[1][1]
        # move u->f
        self.front[0][1] = self.under[0][1]
        self.front[1][1] = self.under[1][1]
        # move b->u
        self.under[0][1] = self.back[1][0]
        self.under[1][1] = self.back[0][0]
        # move t->b
        self.back[1][0] = self.top[0][1]
        self.back[0][0] = self.top[1][1]
        # move f->t
        self.top[0][1] = temp1
        self.top[1][1] = temp2

        # rotate the side
        temp1 = self.right[0][0]
        self.right[0][0] = self.right[1][0]
        self.right[1][0] = self.right[1][1]
        self.right[1][1] = self.right[0][1]
        self.right[0][1] = temp1

    def rotate_left(self):  # 'L' in image
        # rotate the strip
        # save f
        temp1 = self.front[0][0]
        temp2 = self.front[1][0]
        # move t->f
        self.front[0][0] = self.top[0][0]
        self.front[1][0] = self.top[1][0]
        # move b->t
        self.top[0][0] = self.back[1][1]
        self.top[1][0] = self.back[0][1]
        # move u->b
        self.back[1][1] = self.under[0][0]
        self.back[0][1] = self.under[1][0]
        # move f->u
        self.under[0][0] = temp1
        self.under[1][0] = temp2

        # rotate the side
        temp1 = self.left[0][0]
        self.left[0][0] = self.left[1][0]
        self.left[1][0] = self.left[1][1]
        self.left[1][1] = self.left[0][1]
        self.left[0][1] = temp1

    def rotate_back(self):  # 'B' in image
        # rotate the strip
        # save t
        temp1 = self.top[0][0]
        temp2 = self.top[0][1]
        # move r->t
        self.top[0][0] = self.right[0][1]
        self.top[0][1] = self.right[1][1]
        # move u->r
        self.right[0][1] = self.under[1][1]
        self.right[1][1] = self.under[1][0]
        # move l->u
        self.under[1][1] = self.left[1][0]
        self.under[1][0] = self.left[0][0]
        # move t->l
        self.left[1][0] = temp1
        self.left[0][0] = temp2

        # rotate the side
        temp1 = self.back[0][0]
        self.back[0][0] = self.back[1][0]
        self.back[1][0] = self.back[1][1]
        self.back[1][1] = self.back[0][1]
        self.back[0][1] = temp1
        
    def rotate_under(self):  # 'D' in image
        # rotate the strip
        # save f
        temp1 = self.front[1][0]
        temp2 = self.front[1][1]
        # move l->f
        self.front[1][0] = self.left[1][0]
        self.front[1][1] = self.left[1][1]
        # move b->l
        self.left[1][0] = self.back[1][0]
        self.left[1][1] = self.back[1][1]
        # move r->b
        self.back[1][0] = self.right[1][0]
        self.back[1][1] = self.right[1][1]
        # move f->r
        self.right[1][0] = temp1
        self.right[1][1] = temp2

        # rotate the side
        temp1 = self.under[0][0]
        self.under[0][0] = self.under[1][0]
        self.under[1][0] = self.under[1][1]
        self.under[1][1] = self.under[0][1]
        self.under[0][1] = temp1
        
    def rotate_front(self):  # 'F' in image
        # rotate the strip
        # save t
        temp1 = self.top[1][0]
        temp2 = self.top[1][1]
        # move l->t
        self.top[1][0] = self.left[1][1]
        self.top[1][1] = self.left[0][1]
        # move u->l
        self.left[1][1] = self.under[0][1]
        self.left[0][1] = self.under[0][0]
        # move r->u
        self.under[0][1] = self.right[0][0]
        self.under[0][0] = self.right[1][0]
        # move t->r
        self.right[0][0] = temp1
        self.right[1][0] = temp2

        # rotate the side
        temp1 = self.front[0][0]
        self.front[0][0] = self.front[1][0]
        self.front[1][0] = self.front[1][1]
        self.front[1][1] = self.front[0][1]
        self.front[0][1] = temp1
        
    def rotate_top(self):  # 'U' in image
        # rotate the strip
        # save f
        temp1 = self.front[0][0]
        temp2 = self.front[0][1]
        # move r->f
        self.front[0][0] = self.right[0][0]
        self.front[0][1] = self.right[0][1]
        # move b->r
        self.right[0][0] = self.back[0][0]
        self.right[0][1] = self.back[0][1]
        # move l->b
        self.back[0][0] = self.left[0][0]
        self.back[0][1] = self.left[0][1]
        # move f->l
        self.left[0][0] = temp1
        self.left[0][1] = temp2

        # rotate the side
        temp1 = self.top[0][0]
        self.top[0][0] = self.top[1][0]
        self.top[1][0] = self.top[1][1]
        self.top[1][1] = self.top[0][1]
        self.top[0][1] = temp1
    
    

    def rotate_right_inverse(self):  # 'Ri' in image
        # rotate the strip
        # save f
        temp1 = self.front[0][1]
        temp2 = self.front[1][1]
        # move t->f
        self.front[0][1] = self.top[0][1]
        self.front[1][1] = self.top[1][1]
        # move b->t
        self.top[0][1] = self.back[1][0]
        self.top[1][1] = self.back[0][0]
        # move u->b
        self.back[1][0] = self.under[0][1]
        self.back[0][0] = self.under[1][1]
        # move f->u
        self.under[0][1] = temp1
        self.under[1][1] = temp2

        # rotate the side
        temp1 = self.right[0][0]
        self.right[0][0] = self.right[0][1]
        self.right[0][1] = self.right[1][1]
        self.right[1][1] = self.right[1][0]
        self.right[1][0] = temp1

    def rotate_left_inverse(self):  # 'Li' in image
        # rotate the strip
        # save f
        temp1 = self.front[0][0]
        temp2 = self.front[1][0]
        # move u->f
        self.front[0][0] = self.under[0][0]
        self.front[1][0] = self.under[1][0]
        # move b->u
        self.under[0][0] = self.back[1][1]
        self.under[1][0] = self.back[0][1]
        # move t->b
        self.back[1][1] = self.top[0][0]
        self.back[0][1] = self.top[1][0]
        # move f->t
        self.top[0][0] = temp1
        self.top[1][0] = temp2

        # rotate the side
        temp1 = self.left[0][0]
        self.left[0][0] = self.left[0][1]
        self.left[0][1] = self.left[1][1]
        self.left[1][1] = self.left[1][0]
        self.left[1][0] = temp1

    def rotate_back_inverse(self):  # 'Bi' in image
        # rotate the strip
        # save t
        temp1 = self.top[0][0]
        temp2 = self.top[0][1]
        # move l->t
        self.top[0][0] = self.left[1][0]
        self.top[0][1] = self.left[0][0]
        # move u->l
        self.left[1][0] = self.under[1][1]
        self.left[0][0] = self.under[1][0]
        # move r->u
        self.under[1][1] = self.right[0][1]
        self.under[1][0] = self.right[1][1]
        # move t->r
        self.right[0][1] = temp1
        self.right[1][1] = temp2

        # rotate the side
        temp1 = self.back[0][0]
        self.back[0][0] = self.back[0][1]
        self.back[0][1] = self.back[1][1]
        self.back[1][1] = self.back[1][0]
        self.back[1][0] = temp1

    def rotate_under_inverse(self):  # 'Di' in image
        # rotate the strip
        # save f
        temp1 = self.front[1][0]
        temp2 = self.front[1][1]
        # move r->f
        self.front[1][0] = self.right[1][0]
        self.front[1][1] = self.right[1][1]
        # move b->r
        self.right[1][0] = self.back[1][0]
        self.right[1][1] = self.back[1][1]
        # move l->b
        self.back[1][0] = self.left[1][0]
        self.back[1][1] = self.left[1][1]
        # move f->l
        self.left[1][0] = temp1
        self.left[1][1] = temp2

        # rotate the side
        temp1 = self.under[0][0]
        self.under[0][0] = self.under[0][1]
        self.under[0][1] = self.under[1][1]
        self.under[1][1] = self.under[1][0]
        self.under[1][0] = temp1

    def rotate_front_inverse(self):  # 'Fi' in image
        # rotate the strip
        # save t
        temp1 = self.top[1][0]
        temp2 = self.top[1][1]
        # move l->t
        self.top[1][0] = self.left[1][1]
        self.top[1][1] = self.left[0][1]
        # move u->l
        self.left[1][1] = self.under[0][1]
        self.left[0][1] = self.under[0][0]
        # move r->u
        self.under[0][1] = self.right[0][0]
        self.under[0][0] = self.right[1][0]
        # move t->r
        self.right[0][0] = temp1
        self.right[1][0] = temp2

        # rotate the side
        temp1 = self.front[0][0]
        self.front[0][0] = self.front[1][0]
        self.front[1][0] = self.front[1][1]
        self.front[1][1] = self.front[0][1]
        self.front[0][1] = temp1

    def rotate_top_inverse(self):  # 'Ui' in image
        # rotate the strip
        # save f
        temp1 = self.front[0][0]
        temp2 = self.front[0][1]
        # move l->f
        self.front[0][0] = self.left[0][0]
        self.front[0][1] = self.left[0][1]
        # move b->l
        self.left[0][0] = self.back[0][0]
        self.left[0][1] = self.back[0][1]
        # move r->b
        self.back[0][0] = self.right[0][0]
        self.back[0][1] = self.right[0][1]
        # move f->r
        self.right[0][0] = temp1
        self.right[0][1] = temp2

        # rotate the side
        temp1 = self.top[0][0]
        self.top[0][0] = self.top[0][1]
        self.top[0][1] = self.top[1][1]
        self.top[1][1] = self.top[1][0]
        self.top[1][0] = temp1


    # checks to see if the cube is solved
    # note: we check only by checking that every side is a single color
    # so the cube could be rotated from its orriginal state but still be 
    # considered a goal state
    def is_goal_state(self):
        global COLORS
        colors = list(COLORS)
        sides = [self.front, self.right, self.back, self.left, self.top, self.under]  # use is read only

        for side in sides:
            currentColor = side[0][0]
            if currentColor in colors:
                # haven't used this color yet
                colors.remove(currentColor)
            else:
                # have found this color twice
                return False
            if not (side[0][0] == side[0][1] and side[0][1] == side[1][1] and side[1][1] == side[1][0]):
                return False
        return True

    # gets the feature array for the current state
    # in the array 1 represents that the feature is present and 0 represents that
    # the feature is not present
    def features(self):
        
        result = self.get_num_of_solved_sides()
        result.extend(self.get_num_of_solved_adj())
        return result

    # gets the feature array corresponding to the edges
    # in the array 1 represents that the edge is solved and 0 represents the
    # edge not being solved
    def get_num_of_solved_adj(self):
        # checks all 12 edges
        result = []
        if self.front[0][0] == self.front[0][1] and self.top[1][0] == self.top[1][1]:
            result.append(1)
        else:
            result.append(0)

        if self.front[0][0] == self.front[1][0] and self.left[0][1] == self.left[1][1]:
            result.append(1)
        else:
            result.append(0)

        if self.front[1][0] == self.front[1][1] and self.under[0][0] == self.under[0][1]:
            result.append(1)
        else:
            result.append(0)

        if self.front[0][1] == self.front[1][1] and self.right[0][0] == self.right[1][0]:
            result.append(1)
        else:
            result.append(0)

        if self.right[0][0] == self.right[0][1] and self.top[1][1] == self.top[0][1]:
            result.append(1)
        else:
            result.append(0)

        if self.right[0][1] == self.right[1][1] and self.back[0][0] == self.back[1][0]:
            result.append(1)
        else:
            result.append(0)

        if self.right[1][0] == self.right[1][1] and self.under[0][1] == self.under[1][1]:
            result.append(1)
        else:
            result.append(0)

        if self.left[0][0] == self.left[0][1] and self.top[0][0] == self.top[1][0]:
            result.append(1)
        else:
            result.append(0)

        if self.left[0][0] == self.left[1][0] and self.back[0][1] == self.back[1][1]:
            result.append(1)
        else:
            result.append(0)

        if self.left[1][0] == self.left[1][1] and self.under[0][0] == self.under[1][0]:
            result.append(1)
        else:
            result.append(0)

        if self.under[1][0] == self.under[1][1] and self.back[1][0] == self.back[1][1]:
            result.append(1)
        else:
            result.append(0)

        if self.top[0][0] == self.top[0][1] and self.back[0][0] == self.back[0][1]:
            result.append(1)
        else:
            result.append(0)

        return result

    # gets the feature array coresponding to the sides
    # in the array 1 represents that the side is solved and 0 represents the side
    # not being solved
    # note: when we say that a side is solved we are only checking that the colors
    # for all the cubies on that side are the same and are not checking that the
    # surrounding edge is also solved
    def get_num_of_solved_sides(self):
        result = []
        
        for side in [self.front, self.back, self.left, self.right, self.top, self.under]:
            if side_is_solved(side):
                result.append(1)
            else:
                result.append(0)
        
        return result

# a generic checker to see if a side is solved
# does not check that the edges around that side are solved
def side_is_solved(side):  # where side is the array representing that side
    return side[0][0] == side[0][1] and side[0][0] == side[1][0] and side[0][0] == side[1][1]


# Operator class modeled off of the operator class from Towers of Hanoi
# every action is posible from every state so there is no need for a precondition
# check
class Operator:
    def __init__(self, name, state_transf):
        self.name = name
        self.state_transf = state_transf

    def __str__(self):
        return self.name

    def apply(self, s):
        return self.state_transf(s)


# posible actions from within the state space.
# this doesn't include the 180 degree rotations as they are more easily represented
# a the same action done twice from a particular state
OPERATORS = [
    Operator("rotate front", lambda s: s.rotate_front()),
    Operator("rotate under", lambda s: s.rotate_under()),
    Operator("rotate back", lambda s: s.rotate_back()),
    Operator("rotate left", lambda s: s.rotate_left()),
    Operator("rotate right", lambda s: s.rotate_right()),
    Operator("rotate top", lambda s: s.rotate_top()),
    Operator("rotate front inverse", lambda s: s.rotate_front_inverse()),
    Operator("rotate under inverse", lambda s: s.rotate_under_inverse()),
    Operator("rotate back inverse", lambda s: s.rotate_back_inverse()),
    Operator("rotate left inverse", lambda s: s.rotate_left_inverse()),
    Operator("rotate right inverse", lambda s: s.rotate_right_inverse()),
    Operator("rotate top inverse", lambda s: s.rotate_top_inverse()),
    Operator("Exit", lambda s: "Is the cube solved: "+str(s.is_goal_state()))]

# operators2 is used mainly for display purposes. has very limited state space 
# which alows for much faster runtime on certain functions
OPERATORS2 = [ 
    Operator("rotate front 180", lambda s: s.rotate_front_180()),
    Operator("rotate under 180", lambda s: s.rotate_under_180()),
    Operator("rotate back 180", lambda s: s.rotate_back_180()),
    Operator("rotate left 180", lambda s: s.rotate_left_180()),
    Operator("rotate right 180", lambda s: s.rotate_right_180()),
    Operator("rotate top 180", lambda s: s.rotate_top_180()),
    Operator("Exit", lambda s: "Is the cube solved: "+str(s.is_goal_state()))]
