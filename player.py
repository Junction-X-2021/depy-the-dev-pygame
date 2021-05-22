import random

import pygame.image


class Developer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.player_image = pygame.image.load(f"assets/Idle{random.randint(1, 2)}.png")
        self.player_image = pygame.transform.scale(self.player_image, (64, 64))

    def move_to_right(self):
        self.player_image = pygame.image.load(f"assets/Walk{random.randint(1, 5)}.png")
        self.player_image = pygame.transform.scale(self.player_image, (64, 64))
        self.x += 1
        self.y += 1

    def move_to_left(self):
        self.player_image = pygame.image.load(f"assets/Walk{random.randint(1, 5)}.png")
        self.player_image = pygame.transform.flip(self.player_image, True, False)
        self.player_image = pygame.transform.scale(self.player_image, (64, 64))
        self.x -= 1
        self.y += 1

    def draw(self, screen):
        screen.blit(self.player_image, [self.x * 80 + 8, self.y * 30 + 60])


class CEO:
    pass