# To do:
# Avg and worst runtime complexity of each function, in a READ.ME file and comments
# Complexity in code comments and in the READ.ME file analysis. 

# To add in the code:
# - Add a function to check if the tower is stable
# - Add a function
# - Add a timer for each player which will later impact there scores. Add if timer runs out, plaer loses and is skipped.
# The timer starts for the next player the moment the previous player makes a move. Timer starts with 50 seconds, which score = 10 * seconds left

# - The array of scores will be sorted in descending order, so the player with the highest score will be at the top of the leaderboard. 
# Use QuickSort to sort the array of scores. Analyze time complexity.

# - Integrate graphics for the leaderboard and the tower in the game logic

# Data structures:
# - 3D matrix for the tower
# - Hashmap for the leaderboard, key = player name, value = score
# - Linked list for the moves, to be able to backtrack

# Algorithms:
# - Backtracking: you will be able to go back after each move if you don't feel you removed the right piece
# - QuickSort: to sort the leaderboard in descending order



from generateTower import *

class JengaGame:
    def __init__(self, tower_height):
        self.tower = JengaTower(tower_height)
        # EVERY LAYER VALUE STARTS AT 0

        # when initializing game, populate layers with 1s to indicate presence of pieces
        for layer in self.tower.layers:
            for piece in layer.pieces:
                piece.val = 1

    def calculateProbability(self, block):
        # Placeholder for probability calculation
        return 0.5

    def checkStability(self):

        x_balance = 0
        y_balance = 0

        for layer in self.tower.layers[:-1]:        
            
        # Condition 1: Right and middle pieces missing or left and middle pieces missing
            if (layer.pieces[0].val == 1 and layer.pieces[1].val == 0 and layer.pieces[2].val == 0) or \
               (layer.pieces[0].val == 0 and layer.pieces[1].val == 0 and layer.pieces[2].val == 1):
                print("\nNOOO!!! You removed the wrong piece (╥﹏╥)")
                return False

        # Condition 2: No pieces left in the layer
            if layer.pieces[0].val == 0 and layer.pieces[1].val == 0 and layer.pieces[2].val == 0:
                print("\nNOOO!!! No more pieces left in that layer (╥﹏╥)")
                return False
            

        # Condition 3: Balance of tower
        for layer in self.tower.layers: 

            if layer.orientation == "horizontal":
                if layer.pieces[0].val == 0 and layer.pieces[1].val == 0: # Counter balance of the added piece to the right
                    x_balance += 0.5
                elif layer.pieces[1].val == 0 and layer.pieces[2].val == 0: # Counter balance of the added piece to the left
                    x_balance -= 0.5
                elif layer.pieces[0].val == 0 and layer.pieces[2].val == 0: # if both left and right pieces are missing, balance stays the same
                    x_balance += 0
                elif layer.pieces[1].val == 0: # if middle piece is missing, balance stays the same
                    x_balance += 0
                elif layer.pieces[2].val == 0: # if right piece is missing, balance shifts to the right
                    x_balance += 1
                elif layer.pieces[0].val == 0: # if left piece is missing, balance shifts to the left
                    x_balance -= 1

            if layer.orientation == "vertical":
                if layer.pieces[0].val == 0 and layer.pieces[1].val == 0: # Counter balance of the added piece to the right
                    y_balance += 0.5
                elif layer.pieces[1].val == 0 and layer.pieces[2].val == 0: # Counter balance of the added piece to the left
                    y_balance -= 0.5
                elif layer.pieces[0].val == 0 and layer.pieces[2].val == 0: # if both left and right pieces are missing, balance stays the same
                    y_balance += 0
                elif layer.pieces[1].val == 0: # if middle piece is missing, balance stays the same
                    y_balance += 0
                elif layer.pieces[2].val == 0:
                    y_balance += 1
                elif layer.pieces[0].val == 0:
                    y_balance -= 1

        # Distance between two points formula to get the total balance
        balance = (x_balance**2 + y_balance**2)**0.5
        print(f"\nBalance: {balance}")

        if balance == 0:
            print("\nTower is stable ヽ(´▽`)/")
            return True
            
        elif 0 <= balance <= 1:
            print("\nTower moved a bit...")
            return True
        
        elif 1 <= balance <= 2:
            print("\nTower is leaning towards one side (O_O)!")
            return True
        
        elif 2 <= balance <= 3:
            print("\nTower is unstable, be careful (╥﹏╥)!!!")
            return True
        
        elif 3 <= balance <= 4:
            print("\nIT'S ABOUT TO FALL, CAREFULLL !!!")
            return True
        
        else:
            print("\n (╯°□°）╯︵ ┻━┻")
            return False
        

    def addPiece(self, position):
        
        # Add a piece to the top of the tower
        # Has to check which spots are empty in the top layer before adding a new layer
        # Get the last layer
        last_layer = self.tower.layers[-1]

        # Check if the last layer is full
        if all(piece.val == 1 for piece in last_layer.pieces):
            # If the last layer is full, create a new layer with zeros
            new_layer = JengaLayer(orientation="horizontal" if len(self.tower.layers) % 2 == 0 else "vertical")

            # Add the new layer to the tower
            self.tower.layers.append(new_layer)
            last_layer = new_layer

        position = position.upper()
        if position == 'A':
            position_index = 0
        elif position == 'B':
            position_index = 1
        elif position == 'C':
            position_index = 2

        # Check if the specified place has already a piece (val is 1)
        if last_layer.pieces[position_index].val == 1:
            print("\nInvalid move! There's a piece already in that position. Choose a different place.")
            self.addPiece(input("\nEnter the position to add the piece you just removed (A/B/C): "))
            return
        
        # Set the value of the position to 1
        last_layer.pieces[position_index].val = 1


    def removePiece(self, move):

        layer, piece = move[:-1], move[-1]

        piece = piece.upper()
        if piece == 'A':
            piece_index = 0
        elif piece == 'B':
            piece_index = 1
        elif piece == 'C':
            piece_index = 2

        
        layer_index = int(layer) - 1

        # Check if the specified layer is the last one or the second-to-last one
        if layer_index == len(self.tower.layers) - 1 or layer_index == len(self.tower.layers) - 2:
            print("\nInvalid move! Cannot remove pieces from the last or second-to-last layer.")
            self.removePiece(input("\nEnter the layer and piece you want to remove (e.g., 2A): "))
            return

        # Check if the specified piece is already removed (val is 0)
        if self.tower.layers[layer_index].pieces[piece_index].val == 0:
            print("\nInvalid move! The chosen piece has already been removed. Choose a different piece.")
            self.removePiece(input("\nEnter the layer and piece you want to remove (e.g., 2A): "))
            return
        
        # Set the value of the specified piece to 0
        self.tower.layers[layer_index].pieces[piece_index].val = 0

    def backtracking(self):
        # Undo the last move
        # Returns game_over = True, just in case player wants to backtrack after game over
        # uses a stack or linked list to keep track of moves
        # maybe, can add a limit to undo moves in game loop
        pass

    def leaderboard(self, player_name, score):
        # Sort the scores in descending order
        # Print the leaderboard
        pass



# Game loop
def game_loop():
    game = JengaGame(18)
    game_over = False

    # Printing of layers is reversed so first layer is at the bottom
    for layer in reversed(game.tower.layers):
        print(layer)

    while not game_over:

        # Player makes a move removing piece
        move = input("\nEnter the layer and piece you want to remove (e.g., 2A): ")

        game.removePiece(move)

        # Print tower
        for layer in reversed(game.tower.layers):
            print(layer)


        # Check tower stability
        if not game.checkStability():
            print("\nTower falls. Game over!")
            game_over = True
            break


        # Ask the user for the position to add the piece
        position = input("\nEnter the position to add the piece you just removed (A/B/C): ")

        # Add the piece to the tower at the specified position
        game.addPiece(position)

        # Print tower
        for layer in reversed(game.tower.layers):
            print(layer)

        if not game.checkStability():
            print("\nTower falls. Game over!")
            game_over = True
    
    # Print Player leaderboard (maybe)

# Start the game
game_loop()