import sys
import pygame

from mainmenu import draw_menu


def init_game():
    pygame.init()
    pygame.display.set_caption("depy-the-dev")
    screen = pygame.display.set_mode((640, 480))

    # 폰트 불러오기
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    clock = pygame.time.Clock()

    current_mode = "menu"

    while True:
        screen.fill((0, 0, 0))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            key_event = pygame.key.get_pressed()
            if current_mode == "menu":
                draw_menu(screen, font, key_event)


if __name__ == '__main__':
    init_game()


