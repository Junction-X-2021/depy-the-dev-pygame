import random

import pygame.image


class Player:
    def __init__(self, x, y, player_type):
        self.x = x
        self.y = y
        self.count = 0
        self.credit = 0
        self.player_type = player_type
        if player_type == "player":
            self.player_image = pygame.image.load(f"assets/Idle{random.randint(1, 2)}.png")
        elif player_type == "ceo":
            self.player_image = pygame.image.load(f"assets/cIdle{random.randint(1, 2)}.png")
        else:
            self.player_image = pygame.image.load(f"assets/eIdle{random.randint(1, 2)}.png")

        self.player_image = pygame.transform.scale(self.player_image, (64, 64))

    def move_to_right(self):
        global player_type

        if self.player_type == "player":
            self.player_image = pygame.image.load(f"assets/Walk{random.randint(1, 5)}.png")
        elif self.player_type == "ceo":
            self.player_image = pygame.image.load(f"assets/cWalk{random.randint(1, 5)}.png")
        else:
            self.player_image = pygame.image.load(f"assets/eWalk{random.randint(1, 5)}.png")
        self.player_image = pygame.transform.scale(self.player_image, (64, 64))
        self.x += 1
        self.count += 1

    def move_to_left(self):
        if self.player_type == "player":
            self.player_image = pygame.image.load(f"assets/Walk{random.randint(1, 5)}.png")
        elif self.player_type == "ceo":
            self.player_image = pygame.image.load(f"assets/cWalk{random.randint(1, 5)}.png")
        else:
            self.player_image = pygame.image.load(f"assets/eWalk{random.randint(1, 5)}.png")
        self.player_image = pygame.transform.flip(self.player_image, True, False)
        self.player_image = pygame.transform.scale(self.player_image, (64, 64))
        self.x -= 1
        self.count += 1

    def draw(self, screen, res_x, res_y):
        screen.blit(self.player_image, [self.x * res_x*0.125 + res_x*0.0125, self.y * res_y*0.05 + res_y*0.042])


