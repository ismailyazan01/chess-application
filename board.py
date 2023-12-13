import pieces as pc


class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

        self.board[0] = [pc.Rook('White'), pc.Knight('White'), pc.Bishop('White'), pc.Queen('White'),
                         pc.King('White'), pc.Bishop('White'), pc.Knight('White'), pc.Rook('White')]
        self.board[1] = [pc.Pawn('White') for _ in range(8)]

        # Set up the black pieces
        self.board[6] = [pc.Pawn('Black') for _ in range(8)]
        self.board[7] = [pc.Rook('Black'), pc.Knight('Black'), pc.Bishop('Black'), pc.Queen('Black'),
                         pc.King('Black'), pc.Bishop('Black'), pc.Knight('Black'), pc.Rook('Black')]

    def __str__(self):
        board_str = ""
        for row in self.board:
            for piece in row:
                board_str += (str(piece) if piece else ".") + " "
            board_str += "\n"
        return board_str
