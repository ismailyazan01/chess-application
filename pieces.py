class Piece:
    def __init__(self, color, value, symbol):
        self.color = color
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, value=1, symbol='P' if color == 'White' else 'p')


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color, value=3, symbol='N' if color == 'White' else 'n')


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color, value=3, symbol='B' if color == 'White' else 'b')


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color, value=5, symbol='R' if color == 'White' else 'r')


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color, value=9, symbol='Q' if color == 'White' else 'q')


class King(Piece):
    def __init__(self, color):
        super().__init__(color, value=300, symbol='K' if color == 'White' else 'k')
