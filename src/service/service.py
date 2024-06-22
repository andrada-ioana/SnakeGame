from src.repository.repository import Repository
from random import randint


class Service:

    def __init__(self):
        self.__repository = Repository()

    def get_direction(self):
        return self.__repository.get_direction()

    def get_board_object(self):
        return self.__repository.get_board_object()

    def valid_command(self, command: str):
        if command == "up" or command == "down" or command == "left" or command == "right" or command == "move":
            return True
        try:
            command = command.split(" ")
            if len(command) != 2:
                return False
            if command[0] != "move":
                return False
            steps = int(command[1])
            return True
        except:
            return False

    def move_snake(self, command):
        game_board = self.__repository.get_board()
        n = self.__repository.get_n()
        snake = self.__repository.get_snake()
        if command == "up":
            head = snake[0]
            if head[0] - 1 < 0 or game_board[head[0] - 1][head[1]] == "+":
                return False
            apple = 0
            if game_board[head[0] - 1][head[1]] == "a":
                apple = 1
            game_board[head[0] - 1][head[1]] = "*"
            new_snake = [[head[0] - 1, head[1]]]
            for coord in snake:
                new_snake.append(coord)
            if apple == 0:
                new_snake.pop()
            else:
                self.place_one_apple()
            self.__repository.set_snake(new_snake)
            self.remove_snake_from_board()
            self.place_snake()
            self.__repository.update_board(game_board)
            self.__repository.set_direction("up")
        elif command == "down":
            head = snake[0]
            if head[0] + 1 == n or game_board[head[0] + 1][head[1]] == "+":
                return False
            apple = 0
            if game_board[head[0] + 1][head[1]] == "a":
                apple = 1
            game_board[head[0] + 1][head[1]] = "*"
            new_snake = [[head[0] + 1, head[1]]]
            for coord in snake:
                new_snake.append(coord)
            if apple == 0:
                new_snake.pop()
            else:
                self.place_one_apple()
            self.__repository.set_snake(new_snake)
            self.remove_snake_from_board()
            self.place_snake()
            self.__repository.update_board(game_board)
            self.__repository.set_direction("down")
        elif command == "right":
            head = snake[0]
            if head[1] + 1 == n or game_board[head[0]][head[1] + 1] == "+":
                return False
            apple = 0
            if game_board[head[0]][head[1] + 1] == "a":
                apple = 1
            game_board[head[0]][head[1] + 1] = "*"
            new_snake = [[head[0], head[1] + 1]]
            for coord in snake:
                new_snake.append(coord)
            if apple == 0:
                new_snake.pop()
            else:
                self.place_one_apple()
            self.__repository.set_snake(new_snake)
            self.remove_snake_from_board()
            self.place_snake()
            self.__repository.update_board(game_board)
            self.__repository.set_direction("right")
        if command == "left":
            head = snake[0]
            if head[1] - 1 < 0 or game_board[head[0]][head[1] - 1] == "+":
                return False
            apple = 0
            if game_board[head[0]][head[1] - 1] == "a":
                apple = 1
            game_board[head[0]][head[1] - 1] = "*"
            new_snake = [[head[0], head[1] - 1]]
            for coord in snake:
                new_snake.append(coord)
            if apple == 0:
                new_snake.pop()
            else:
                self.place_one_apple()
            self.__repository.set_snake(new_snake)
            self.remove_snake_from_board()
            self.place_snake()
            self.__repository.update_board(game_board)
            self.__repository.set_direction("left")
        return True

    def remove_snake_from_board(self):
        game_board = self.__repository.get_board()
        n = self.__repository.get_n()
        for i in range(n):
            for j in range(n):
                if game_board[i][j] == "*" or game_board[i][j] == "+":
                    game_board[i][j] = " "

    def get_board(self):
        return self.__repository.get_board()

    def create_snake(self):
        n = self.__repository.get_n()
        game_board = self.__repository.get_board()
        snake = []
        for i in range(3):
            snake.append([n // 2 + i - 1, n // 2])
        self.__repository.set_snake(snake)

    def place_snake(self):
        game_board = self.__repository.get_board()
        n = self.__repository.get_n()
        snake = self.__repository.get_snake()
        for coord in snake:
            game_board[coord[0]][coord[1]] = "+"
        game_board[snake[0][0]][snake[0][1]] = "*"
        self.__repository.update_board(game_board)

    @staticmethod
    def random_pos(n: int):
        x = randint(0, n - 1)
        return x

    def place_one_apple(self):
        game_board = self.__repository.get_board()
        n = self.__repository.get_n()
        while True:
            x = self.random_pos(n - 1)
            y = self.random_pos(n - 1)
            if game_board[x][y] == " ":
                if x > 0 and x < n - 1 and game_board[x - 1][y] != "a" and game_board[x + 1][y] != "a":
                    if y > 0 and y < n - 1 and game_board[x][y - 1] != "a" and game_board[x][y + 1] != "a":
                        game_board[x][y] = "a"
                        break
        self.__repository.update_board(game_board)

    def place_apples(self):
        game_board = self.__repository.get_board()
        nr_apples = self.__repository.get_nr_apple()
        n = self.__repository.get_n()
        cont = 1
        while cont <= nr_apples:
            x = self.random_pos(n)
            y = self.random_pos(n)
            if game_board[x][y] == " ":
                if x > 0 and x < n - 1 and game_board[x - 1][y] != "a" and game_board[x + 1][y] != "a":
                    if y > 0 and y < n - 1 and game_board[x][y - 1] != "a" and game_board[x][y + 1] != "a":
                        game_board[x][y] = "a"
                        cont += 1
        self.__repository.update_board(game_board)
