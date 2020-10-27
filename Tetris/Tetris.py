# The game runner
# It creates a game Class and runs its mainloop 

import game

tetris = game.Game()

while tetris.run:
    tetris.main_loop()