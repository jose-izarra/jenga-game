import random 
import numpy as np

TOTAL_PIECES = 54
TOWER_HEIGHT = 18
TOWER_WIDTH = 3
MAX_HEIGHT = 48


class Jenga:
    def __init__(self):
        # Create a 3D matrix representing height, game pieces, and individual components of our pieces
        self.game_matrix = np.zeros((MAX_HEIGHT,3,3))
        
        
        # tracks how many successfull moves you have made 
        self.move_counter = 0
        # variable to keep track of how many extra levels we have added - every 3 pieces stacked is +1
        self.extra_levels = 0
        
        self.init_weights()  
        
    def nheight(self):
        return len(self.game_matrix)
    
    def npieces(self):
        return len(self.game_matrix[0])

    def npiece_components(self):
        return len(self.game_matrix[0][0])
    
    def print_matrix(self):
        print(self.game_matrix)
    
    def init_weights(self):
        # add all the initial weights + to the matrix | this part should have the random values
        ...
    
    def remove_piece(self, piece):
        
        ...
        
    def stack_piece(self, piece, new_pos: [0,1,2]):
        # stacks up the piece that was taken out + gives the piece new children depending on its position
        
        self.move_counter += 1
        if self.move_counter%3 == 0 and self.move_counter != 0:
            self.extra_levels += 1
        ...
        
    def check_state(self):
        # checks the state of the tower and returns true or false depending on if it has fallen or not
        ...
    
    def update_weights(self, piece, pos):
        # runs the algorithm to update the weight distribution of the jenga pieces
        ...
        
    def show_tower_window(self): # show the tower to the screen
        ...
    
    def update_tower_window(self): # update the tower once a move is made
        ...
        
    