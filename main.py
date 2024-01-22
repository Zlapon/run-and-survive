from scripts.player import Player
from scripts.enemies import Enemy
import pygame

class Game:
    def __init__(self, width, height, bg):
        pygame.init()
        self.width = width
        self.height = height
        self.bg = bg
        self.screen = pygame.display.set_mode((self.width, self.height))

        run = True

        self.player = Player(self.screen, self.width // 2, self.height // 2, 50, 50)
       
        while run:

            self.screen.fill(self.bg)

            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.player.drawPlayer()
            self.player.movement(keys)
            self.player.collision()

            pygame.display.flip()
game = Game(900, 900, (0, 0, 0))