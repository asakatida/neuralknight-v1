from .board import KING, QUEEN


def test_board_creation_valid(start_board):
    assert start_board


def test_pieces_on_board(start_board):
    assert KING in start_board
    assert QUEEN in start_board
    assert KING | 1 in start_board
    assert QUEEN | 1 in start_board


def test_first_move_available(start_board):
    assert next(start_board.lookahead_boards(1))
