import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,screen,  x, y, width, height, health = 5, speed = 1):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.speed = speed
    def movement(self, keys):
        if keys[pygame.K_a]: 
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
    def drawPlayer(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
    def collision(self):
        if (self.x + self.width) >= 900:
            self.x -= self.speed
        if (self.x) <= 0:
            self.x += self.speed
        if (self.y + self.height) >= 900:
            self.y -= self.speed
        if (self.y) <= 0:
            self.y += self.speed
