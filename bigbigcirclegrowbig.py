import pygame
import pgzrun
from random import randint

TITLE = "bigbigcirclegrowbig"
HEIGHT = 600
WIDTH = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()
pygame.display.update()

class Bigbigcirclegrowbig():
    def __init__(self, colour, position, radius, width):
        self.colour = colour
        self.position = position
        self.radius = radius 
        self.width = width
        self.circle_surface = screen
    def draw(self):
        pygame.draw.circle(self.circle_surface, self.colour, self.position, self.radius, self.width)
    def grow(self, r):
        self.radius = self.radius + r
        pygame.draw.circle(self.circle_surface, self.colour, self.position, self.radius, self.width)

#bigbigcirclegrowbig object 

twoh = Bigbigcirclegrowbig("aquamarine", (400,300), 30, 0 )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255, 255, 255))
            twoh.draw()
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255, 255, 255))
            twoh.grow(5)
            pygame.display.update()
