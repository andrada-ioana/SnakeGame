from src.domain.domain import SnakeBoard

class Repository:
    def __init__(self):
        self.file_path = r"D:\Andrada\Portofoliu programare\Python\Snake\src\repository\data.txt"
        n, apples = self.read_from_file()
        self.snake = []
        self.direction = "up"
        self.board = SnakeBoard(int(n), int(apples))

    def get_direction(self):
        return self.direction

    def set_direction(self, new_direction: str):
        self.direction = new_direction

    def get_snake(self):
        return self.snake

    def set_snake(self, new_snake: list):
        self.snake = new_snake

    def update_board(self, new_board):
        self.board.set_board(new_board)

    def get_n(self):
        return self.board.get_n()

    def get_nr_apple(self):
        return self.board.get_nr_apple()

    def get_board(self):
        return self.board.get_board()

    def get_board_object(self):
        return self.board

    def read_from_file(self):
        with open(self.file_path, "r") as file:
            text = file.readlines()[0]
            text = text.split(" ")
            return text[0], text[1]