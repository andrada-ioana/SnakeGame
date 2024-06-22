from src.service.service import Service

class UI:
    def print_board(self, service):
        print(service.get_board_object())

    def read_command(self, service):
        command = input("Enter command: ")
        if service.valid_command(command):
            return command
        else:
            raise Exception("Not valid")


    def start(self):
        service = Service()
        service.create_snake()
        service.place_snake()
        service.place_apples()
        while True:
            self.print_board(service)
            try:
                command = self.read_command(service)
                snake_direction = service.get_direction()
                if command == "right" or command == "left" or command == "up" or command == "down":
                    if snake_direction == "right" and command == "left" or snake_direction == "left" and \
                            command == "right" or snake_direction == "up" and command == "down" or \
                            snake_direction == "down" and command == "up":
                        raise Exception("Invalid command")
                    if snake_direction == command:
                        raise Exception("Invalid command")
                    end_game = service.move_snake(command)
                    if end_game == False:
                        print("Game over")
                        break
                elif command == "move":
                    end_game = service.move_snake(snake_direction)
                    if end_game == False:
                        print("Game over")
                        break
                else:
                    command = command.split(" ")
                    cont = command[1]
                    end_game = True
                    for i in range(int(cont)):
                        end_game = service.move_snake(snake_direction)
                        if end_game == False:
                            print("Game over")
                            break
                    if end_game == False:
                        break
            except Exception as e:
                print(e)



ui = UI()
ui.start()