# The game.py has the game class which has the game mainloop and the event handling

import tetriminos as tetr
import time
import keyboard

class Game(object):
    def __init__(self):
        ''' No parameters are taken. It creates the board and the first tetriminos '''
        self.run = True # This flag is used in the while loop
        self.delay = 0.5 # The game speed
        self.board = [[None for j in range(10)] for i in range(22)] 
        self.active_tetris = tetr.Tetriminos(self.board) 
        self.time_start = time.time() # This is used for the board update later
        self.press_cooldown = True # Cooldown after the button press

    def delete_row(self):
        ''' It deletes a row when it is full with blocks. It also drops down all the above blocks '''
        for index,row in enumerate(self.board): # I need the index for the second function of the method
            if None not in row: # This means that it is full
                self.board[index] = [None for i in range(10)] # delete

                for r in self.board[index::-1]: # From the index of the deleted row and above from bottom to up
                    for bl in r:
                        if bl != None: 
                            bl.move_down() # Move blocks down

    def lost(self):
        ''' If the blocks touch up then return True '''
        for bl in self.board[1]:
            if bl != None:
                return True
        return False

    def terminal_print(self):
        ''' It print out the board in a user friendly way '''
        for row in self.board:
            for pos in row:
                print("|",end = "")
                if pos != None:
                    print(pos,end = "")
                else:
                    print(0,end = "") 
            print("|")
        print("\n\n\n")

    def main_loop(self):
        ''' Event handling and update of the screen in the speed of the defined attribute '''
        if keyboard.is_pressed("left") and self.press_cooldown: # If left key is pressed, the active tetriminos is going left 
            if self.active_tetris.left_possible(): # But if it is possible
                for bl in self.active_tetris.blocks:
                    bl.move_left()
                    self.press_cooldown = False

        if keyboard.is_pressed("right") and self.press_cooldown: # If right key is pressed, the active tetriminos is going right 
            if self.active_tetris.right_possible(): # But if it is possible
                for bl in self.active_tetris.blocks:
                    bl.move_right()
                    self.press_cooldown = False

        if keyboard.is_pressed("z") and self.press_cooldown: # If z key is pressed, the active tetriminos is rotating left 
            if self.active_tetris.turn_possible("left"): # But if it is possible
                self.active_tetris.rotate("left")
                self.press_cooldown = False

        if keyboard.is_pressed("x") and self.press_cooldown: # If x key is pressed, the active tetriminos is rotating right 
            if self.active_tetris.turn_possible("right"): # But if it is possible
                self.active_tetris.rotate("right") 
                self.press_cooldown = False

        t = time.time()

        if t - self.time_start > self.delay: # Updates every self.delay seconds
            for bl in self.active_tetris.blocks: # Moves down
                bl.move_down()
            if self.active_tetris.stop(): # If the tetriminos hit a obstucle
                self.delete_row() # Checks for foul rows
                if self.lost(): # Checks if player lost
                    self.run = False # Finish the game
                    return
                self.active_tetris = tetr.Tetriminos(self.board) # Creates a new tetriminos

            self.terminal_print() 

            self.press_cooldown = True # Reset the cooldown

            self.time_start = time.time() # Resets the time

        

            
            

            