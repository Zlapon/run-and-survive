import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, player,  width, height, speed =0.3): 
        self.screen = screen
        self.player = player
        self.width = width
        self.height = height
        self.x = random.randint(0, 900)
        self.y = random.randint(0, 900)
        self.speed = speed
    def movement(self):
        if self.x < self.player.x:
            self.x += self.speed
        if self.x > self.player.x:
            self.x -= self.speed
        if self.y < self.player.y:
            self.y += self.speed
        if self.y > self.player.y:
            self.y -= self.speed
    def drawEnemy(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.width, self.height))