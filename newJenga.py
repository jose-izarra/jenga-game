from generateTower import *

class JengaGame:
    def __init__(self, tower_height):
        self.tower = JengaTower(tower_height)
        
    def calculateProbability(self, block):
        # Placeholder for probability calculation
        return 0.5

    def checkStability(self):
        self.currentSum = 0
        
        return True

    def addPiece(self, piece):
        
        # Add a piece to the top of the tower
        # Has to check which spots are empty in the top layer before adding a new layer

        self.layers.append(JengaLayer())

    def removePiece(self, layer, piece):
        # Remove a piece from the tower
        # Placeholder for piece removal logic
        pass

    def backtracking(self):
        # Undo the last move
        # Placeholder for backtracking logic
        pass

# Game loop
def game_loop():
    game = JengaGame(3)
    game_over = False

    while not game_over:
        # Player makes a move
        move = input("Enter the layer and piece you want to remove (e.g., 2A): ")

        layer, piece = move[:-1], move[-1]

        game.removePiece(layer, piece)

        # Check tower stability
        if not game.checkStability():
            print("Tower falls. Game over!")
            game_over = True

        # Ask the user for the position to add the piece
        position = input("Enter the position to add the piece (A/B/C): ")

        # Add the piece to the tower at the specified position
        game.addPieceToTop(position)

        if not game.checkStability():
            print("Tower falls. Game over!")
            game_over = True

# Start the game
game_loop()

# # Example print:
# height = 10
# tower = JengaTower(height)

# for layer in tower.layers:
#     print(layer)