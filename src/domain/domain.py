from texttable import Texttable

class SnakeBoard:
    def __init__(self, n: int, nr_apple: int):
        self.__n = n
        self.__nr_apple = nr_apple
        self.__board = [[" " for i in range(n)] for j in range(n)]

    def get_n(self):
        return self.__n

    def get_nr_apple(self):
        return self.__nr_apple

    def get_board(self):
        return self.__board

    def set_board(self, new_board):
        self.__board = new_board

    def __str__(self):
        snake_board = Texttable()
        snake_board.set_cols_align(["c"] * (self.__n))
        for i in range(self.__n):
            snake_board.add_row(self.__board[i])
        return snake_board.draw()
