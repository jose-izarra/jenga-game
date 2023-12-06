class JengaPiece:
    def __init__(self): # Time complexity = O(1)
        
        self.val = 0 # 0 = empty, 1 = not empty

    def __repr__(self): 
        return f"[{self.val}]"


class JengaLayer:
    def __init__(self, orientation): # Time complexity = O(1)
        self.pieces = [JengaPiece() for _ in range(3)] # 3 pieces per layer
        self.orientation = orientation # horizontal or vertical

    def __repr__(self):
        return repr(self.pieces)


class JengaTower:
    def __init__(self, height): # height = number of layers; Time complexity = O(n)
        self.layers = [JengaLayer("horizontal" if i % 2 == 0 else "vertical") for i in range(height)] # alternating orientation

    def __repr__(self):
        return repr(self.layers)
