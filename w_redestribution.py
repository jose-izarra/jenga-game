# Description: This file contains the function that will go through every piece and update the "weights" accordingly
#             every time a piece is moved (on or out of the tower). The weights are used to determine the probability
#             of the tower falling over. If the sum of the weights goes over the threshold value, the tower falls over.

# Notes:
# - Remember we can't remove the pieces from the two top most levels of the tower according to Jenga Bible, so we can't
# remove those pieces.
#
# - The pieces' weight will simulate the effect of gravity on the tower. The more weight a piece has, the more likely
# it is to fall over.

# Levels to keep track of number of pieces:
# Number of full levels: 3/3 pieces
# Number of half levels: 2/3 pieces
# Top level amount of pieces: ?/3 pieces

import numpy as np

def w_redistribution(matrix, coefficient -> (value that indicates if tower falls)):

    