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
# - Stack list for the moves, to be able to backtrack

# Algorithms:
# - Backtracking: you will be able to go back after each move if you don't feel you removed the right piece
# - QuickSort: to sort the leaderboard in descending order


import os
import csv
from datetime import datetime
from generateTower import *

class JengaGame:
    def __init__(self, tower_height):
        self.tower = JengaTower(tower_height)
        # EVERY LAYER VALUE STARTS AT 0

        # when initializing game, populate layers with 1s to indicate presence of pieces
        for layer in self.tower.layers:
            for piece in layer.pieces:
                piece.val = 1
        
        # moves stack for backtracking
        self.moves = []   
        # order -> [ [removed_layer_piece_index_1, removed_piece_index_1, added_piece_layer_index_1, added_piece_index_1], [... _2] ]
        
        self.num_moves = 0
        

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
        self.addMove(-1, position_index, True)
        self.num_moves += 1


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
        self.addMove(layer_index, piece_index, False)
        
    def addMove(self, layer_index, piece_index, add):
        
        # append the new move to stack
        
        # first you add the removed piece, and then the added piece
        if not add:
            self.moves.append([layer_index, piece_index])
            
        else:
            self.moves[-1].append(layer_index)
            self.moves[-1].append(piece_index)

    def backtrack(self):
        if not self.num_moves:
            print("BRUH. You're at the starting point, you can't go back")
            return
        
        # Undo the last move
        # Returns game_over = True, just in case player wants to backtrack after game over
        # uses a stack or linked list to keep track of moves
        # maybe, can add a limit to undo moves in game loop
        print("\nBacktracking\n")
        remove_layer, remove_piece, add_layer, add_piece = self.moves.pop()
        
        print(remove_layer, remove_piece, add_layer, add_piece)
        
        
        # reverse engineer the process
        self.tower.layers[remove_layer].pieces[remove_piece].val = 1
        self.tower.layers[add_layer].pieces[add_piece].val = 0
        
        last_layer = self.tower.layers[-1]
        
        
        if all(piece.val == 0 for piece in last_layer.pieces):
            self.tower.layers.remove(last_layer)
        self.num_moves -= 1
           
    def print_tower(self):
        for layer in reversed(self.tower.layers):
            print(layer)
            
    def game_over(self):
        print("\n---------- GAME OVER ----------\n")
        
        name = input("Input your name to be added to the Leaderboard! -> ")
        date = datetime.now().strftime("%Y-%m-%d")
        return name, date
    


def sorting_key(row):
    return int(row[1])

def quicksort(data_arr):
    if len(data_arr) <= 1:
        return data_arr

    pivot = data_arr[len(data_arr) // 2]
    left = [x for x in data_arr if sorting_key(x) > sorting_key(pivot)]
    middle = [x for x in data_arr if sorting_key(x) == sorting_key(pivot)]
    right = [x for x in data_arr if sorting_key(x) < sorting_key(pivot)]
    return quicksort(left) + middle + quicksort(right)

def print_leaderboard(file_name):
    with open(file_name, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Skip the header row
        data = list(csv_reader)
        
    sorted_data = quicksort(data)
    print("\nLadies and Gentleman... The Leaderboard")
    print("Name     Number of Moves     Date")
    for row in sorted_data:
        print(f"{row[0]}    {row[1]}            {row[2]}")

print_leaderboard('scores.txt')
# Game loop
def game_loop():
    game = JengaGame(18)
    game_over = False

    # Printing of layers is reversed so first layer is at the bottom
    for layer in reversed(game.tower.layers):
        print(layer)

    while not game_over:
        print(f"\nNumber of moves: {game.num_moves}")
        print(f"Moves list: {game.moves}")
        
        # Instruct the player of backtracking option after first move
        if game.num_moves > 0: print("\nEnter -1 if you want to undo your move")
        
        # Player makes a move removing piece
        move = input("Enter the layer and piece you want to remove (e.g., 2A): ")

        if move == "-1":
            game.backtrack()
            game.print_tower()
            continue
        
                    
        game.removePiece(move)
        
        # Print tower
        game.print_tower()

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
        game.print_tower()

        if not game.checkStability():
            print("\nTower falls. Game over!")
            game_over = True
    
    
    name, date = game.game_over()

    data = [name, game.num_moves, date]
    
    file_name = "scores.txt"
    
    # Write to file where scores will be stored
    if not os.path.isfile(file_name):
        with open(file_name, "w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Name", "Number of Moves", "Date"])
            csv_writer.writerow(data)
    else:
        with open(file_name, "a", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data)

    # Print Player leaderboard
    print_leaderboard(file_name)
    

# Start the game
game_loop()