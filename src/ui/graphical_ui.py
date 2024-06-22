import pygame

class GUI:
    def start(self):
        pygame.init()
        width = 1000
        height = 700
        DARK_GREEN = (0, 100, 0)
        GRASS_GREEN = (0, 200, 0)

        RED = (255, 0, 0)
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake")
        screen.fill(GRASS_GREEN)
        pygame.draw.rect(screen, DARK_GREEN, (0, 0, 1000, 700), 20)
        pygame.display.update()
        #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return


gui = GUI()
gui.start()