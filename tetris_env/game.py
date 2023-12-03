from tetris_env.board import Board

class Game:
    def __init__(self, board: Board):
        self.board = board
        self.level = 0
        self.score = 0

    def update(self):
        if self.board.piece is None:
            self.board.get_piece()