class JengaPiece:
    def __init__(self):
        # Each block has three components: left, middle, right
        self.val = 0

        # self.left = 0
        # self.middle = 0
        # self.right = 0

    def __repr__(self):
        return f"[{self.val}]"

        # return f"[{self.left}, {self.middle}, {self.right}]"


class JengaLayer:
    def __init__(self, orientation):
        self.pieces = [JengaPiece() for _ in range(3)]
        self.orientation = orientation

    def __repr__(self):
        return repr(self.pieces)


class JengaTower:
    def __init__(self, height):
        self.layers = [JengaLayer("horizontal" if i % 2 == 0 else "vertical") for i in range(height)]

    def __repr__(self):
        return repr(self.layers)

    # Not working!!
    def render(self):
        x = 0
        y = 0
        for layer in self.layers:
            for piece in layer.pieces:
                print(f"\033[{y};{x}H", end="")
                print(piece, end="")
                x += len(str(piece)) + 1
            x = 0
            y += 1
        print()


# height = 3
# tower = JengaTower(height)

# # Modify the middle value of all pieces in the chosen layer
# for layer in tower.layers:
#     for piece in layer.pieces:
#         piece.val = 1

# # Print each layer on a new line
# for layer in tower.layers:
#     print(layer)