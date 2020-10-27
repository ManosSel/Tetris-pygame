# This script has the Block and Tetriminos classes

# Block is a piece of the tetriminos
class Block(object):
    def __init__(self, board, board_x, board_y, color):
        ''' It takes board, board_x, board_y and color and put them in attributes '''
        self.board = board
        self.pos = [board_x, board_y]
        self.color = color

    def move_down(self):
        ''' Moves the block one place down '''
        if self.board[self.pos[0]][self.pos[1]] == self: # This prevents the overwriting of a block that had already gone down
            self.board[self.pos[0]][self.pos[1]] = None 
        self.pos = [self.pos[0] + 1, self.pos[1]] # attribute change
        self.board[self.pos[0]][self.pos[1]] = self # board change

    def move_right(self):
        ''' Moves the block one place right '''
        if self.board[self.pos[0]][self.pos[1]] == self: # This prevents the overwriting of a block that had already gone down
            self.board[self.pos[0]][self.pos[1]] = None
        self.pos = [self.pos[0], self.pos[1] + 1] # attribute change
        self.board[self.pos[0]][self.pos[1]] = self # board change

    def move_left(self):
        ''' Moves the block one place right '''
        if self.board[self.pos[0]][self.pos[1]] == self: # This prevents the overwriting of a block that had already gone down
            self.board[self.pos[0]][self.pos[1]] = None
        self.pos = [self.pos[0], self.pos[1] - 1] # attribute change
        self.board[self.pos[0]][self.pos[1]] = self # board change

    def __repr__(self):
        ''' Str representation for the terminal output '''
        return "="

import random

# The tetriminos object constructor with their behaviors '''
class Tetriminos(object):
    def __init__(self,board):
        ''' It takes as parameter the game board and chooses the type of the tetriminos '''
        self.board = board
        tetris_match = { # Helper dict for matching the type with the block constructor method
            "four_row" : self.four_row,
            "block" : self.block,
            "two_two_right" : self.two_two_rigth,
            "two_two_left" : self.two_two_left,
            "one_three_center" : self.one_three_center,
            "one_three_right" : self.one_three_right,
            "one_three_left" : self.one_three_left,
        }

        self.name = random.choice(["block","two_two_right","two_two_left","four_row","one_three_center","one_three_right","one_three_left"]) #,"block","two_two_rigth","two_two_left","four_row","one_three_center","one_three_rigth","one_three_left"
        tetris_match[self.name]() # Calls the matched method

# These methods handle the construction of the blocks of its tetriminos
# It also puts a center and the distance from the center in every direction 
# which will help later for the rotation of the tetriminos

    def four_row(self):
        ''' I tetriminos type constructor '''
        bl1 = self.board[0][4] = Block(self.board,0,4,"chiel")
        bl2 = self.board[1][4] = Block(self.board,1,4,"chiel")
        bl3 = self.board[2][4] = Block(self.board,2,4,"chiel")
        bl4 = self.board[3][4] = Block(self.board,3,4,"chiel")
        self.blocks = (bl2, bl1, bl3, bl4)
        self.center = bl2
        self.up = ((-1,0),(1,0),(-2,0))
        self.right = ((0,-2),(0,-1),(0,1))
        self.down = ((-2,0),(-1,0),(1,0))
        self.left = ((0,-1),(0,1),(0,2))
        self.direction = self.up

    def block(self):
        ''' O tetriminos type constructor '''
        bl1 = self.board[0][3] = Block(self.board,0,3,"yellow")
        bl2 = self.board[0][4] = Block(self.board,0,4,"yellow")
        bl3 = self.board[1][3] = Block(self.board,1,3,"yellow")
        bl4 = self.board[1][4] = Block(self.board,1,4,"yellow")
        self.blocks = (bl4, bl3, bl2, bl1)

    def two_two_rigth(self):
        ''' S tetriminos type constructor '''
        bl1 = self.board[0][3] = Block(self.board,0,3,"green")
        bl2 = self.board[1][3] = Block(self.board,1,3,"green")
        bl3 = self.board[1][4] = Block(self.board,1,4,"green")
        bl4 = self.board[2][4] = Block(self.board,2,4,"green")
        self.blocks = (bl2, bl1, bl3, bl4)
        self.center = bl2
        self.up = ((-1,-1),(0,-1),(1,0))
        self.right = ((0,-1),(-1,0),(-1,1))
        self.down = ((-1,0),(0,1),(1,1))
        self.left = ((0,1),(1,-1),(1,0))
        self.direction = self.up

    def two_two_left(self):
        ''' Z tetriminos type constructor '''
        bl1 = self.board[0][4] = Block(self.board,0,4,"red")
        bl2 = self.board[1][3] = Block(self.board,1,3,"red")
        bl3 = self.board[1][4] = Block(self.board,1,4,"red")
        bl4 = self.board[2][3] = Block(self.board,2,3,"red")
        self.blocks = (bl2, bl1, bl3, bl4)
        self.center = bl2
        self.up = ((-1,1),(0,1),(1,0))
        self.right = ((0,-1),(1,0),(1,1))
        self.down = ((-1,0),(0,-1),(1,-1))
        self.left = ((-1,-1),(-1,0),(0,1))
        self.direction = self.up

    def one_three_center(self):
        ''' T tetriminos type constructor '''
        bl1 = self.board[0][3] = Block(self.board,0,3,"purple")
        bl2 = self.board[0][4] = Block(self.board,0,4,"purple")
        bl3 = self.board[0][5] = Block(self.board,0,5,"purple")
        bl4 = self.board[1][4] = Block(self.board,1,4,"purple")
        self.blocks = (bl4, bl1, bl2, bl3)
        self.center = bl4
        self.up = ((-1,-1),(-1,0),(-1,1))
        self.right = ((-1,1),(0,1),(1,1))
        self.down = ((1,-1),(1,0),(1,1))
        self.left = ((1,-1),(0,-1),(-1,-1))
        self.direction = self.up

    def one_three_right(self):
        ''' J tetriminos type constructor '''
        bl1 = self.board[0][3] = Block(self.board,0,3,"orange")
        bl2 = self.board[1][3] = Block(self.board,1,3,"orange")
        bl3 = self.board[2][3] = Block(self.board,2,3,"orange")
        bl4 = self.board[0][4] = Block(self.board,0,4,"orange")
        self.blocks = (bl2, bl1, bl3, bl4)
        self.center = bl2
        self.up = ((-1,0),(-1,1),(1,0))
        self.right = ((0,-1),(0,1),(1,1))
        self.down = ((1,-1),(-1,0),(1,0))
        self.left = ((-1,-1),(0,-1),(0,1))
        self.direction = self.up

    def one_three_left(self):
        ''' L tetriminos type constructor '''
        bl1 = self.board[0][4] = Block(self.board,0,4,"blue")
        bl2 = self.board[1][4] = Block(self.board,1,4,"blue")
        bl3 = self.board[2][4] = Block(self.board,2,4,"blue")
        bl4 = self.board[0][3] = Block(self.board,0,3,"blue")
        self.blocks = (bl2, bl1, bl3, bl4)
        self.center = bl2
        self.up = ((-1,-1),(-1,0),(1,0))
        self.right = ((0,-1),(0,1),(-1,1))
        self.down = ((-1,0),(1,0),(1,1))
        self.left = ((0,-1),(1,-1),(0,1))
        self.direction = self.up

    def rotate(self,dir):
        ''' This method makes the tetriminos rotate.
            It achieve that by moving the blocks around the central block which remain the same.
            It uses the up , down , right and left attributes to find the new positions 
        '''
        dirs = [self.up,self.right,self.down,self.left] # This mechanism finds the new direction 
        if dir == "right": # If it is right takes the next dir from the dirs list
            try:
                self.direction = dirs[dirs.index(self.direction) + 1]
            except IndexError: 
                self.direction = dirs[0]

        else: # If it is left takes the previous dir from the dirs list
            try:
                self.direction = dirs[dirs.index(self.direction) - 1]
            except IndexError:
                self.direction = dirs[3]

        dir_pos = iter(self.direction) # I use this within the for loop with the next function
        for bl in self.blocks[1:]: # 1: are the blocks without the central 
            new_pos = next(dir_pos)
            if bl.board[bl.pos[0]][bl.pos[1]] == bl: # This prevents the overwriting of a block that had already rotate
                bl.board[bl.pos[0]][bl.pos[1]] = None
            bl.pos = [self.center.pos[0] + new_pos[0],self.center.pos[1] + new_pos[1]] # attribute change
            bl.board[bl.pos[0]][bl.pos[1]] = bl # board change

    def stop(self):
        ''' Return true if the tetriminos touches down or a other not active block else False '''
        for bl in self.blocks:
            try:
                if self.board[bl.pos[0] + 1][bl.pos[1]] != None:
                    if self.board[bl.pos[0] + 1][bl.pos[1]] not in self.blocks:
                        return True
            except IndexError: 
                return True

        return False

    def right_possible(self):
        ''' It checkes whether it it is possible to go right and returns '''
        for bl in self.blocks:
            if bl.pos[1] + 1 > 9: # Checks if goes out of the right limit
                return False
            if self.board[bl.pos[0]][bl.pos[1] + 1] != None: # Checks if touches a non active block
                if self.board[bl.pos[0]][bl.pos[1] + 1] not in self.blocks:
                    return False

        return True

    def left_possible(self):
        ''' It checkes whether it it is possible to go left and returns '''
        for bl in self.blocks:
            if bl.pos[1] - 1 < 0: # Checks if goes out of the left limit
                return False
            if self.board[bl.pos[0]][bl.pos[1] - 1] != None: # Checks if touches a non active block
                if self.board[bl.pos[0]][bl.pos[1] - 1] not in self.blocks:
                    return False

        return True

    def turn_possible(self,dir):
        ''' It checkes whether it it is possible to rotate to a direction and returns '''
        if self.name == "block": # Block can't rotate 
            return False

        dirs = [self.up,self.right,self.down,self.left] # First find the new direction in the same way as in rotate method
        if dir == "right":
            try:
                new_dir = dirs[dirs.index(self.direction) + 1]
            except IndexError:
                new_dir = dirs[0]
        else:
            try:
                new_dir = dirs[dirs.index(self.direction) - 1]
            except IndexError:
                new_dir = dirs[3]

        dir_pos = iter(new_dir) # I use this within the for loop with the next function
        for bl in self.blocks[1:]:  # 1: are the blocks without the central 
            new_pos = next(dir_pos)
            if bl.pos[1] + new_pos[1] < 0 or bl.pos[1] + new_pos[1] > 9: # Checks if goes out of the limits 
                return False
            if self.board[bl.pos[0] + new_pos[0]][bl.pos[1] + new_pos[1]] != None: # Checks if touches a non active block
                if self.board[bl.pos[0] + new_pos[0]][bl.pos[1] + new_pos[1]] not in self.blocks:
                    return False

        return True

    


        
