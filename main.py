import pygame
import tkinter as tk

from mainmenu import draw_menu
from singleplay import single_player_game

# 해상도 설정
root = tk.Tk()

RES_Y = root.winfo_screenheight()
RES_X = round(RES_Y * 0.44)


def init_game():
    pygame.init()
    pygame.display.set_caption("depy-the-dev")
    screen = pygame.display.set_mode((RES_X, RES_Y))

    # 폰트 불러오기
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    current_mode = "menu"
    current_stage, game_init, game_running = 1, True, False

    while True:
        screen.fill((255, 255, 255))

        if current_mode == "menu":
            selected_menu, selected_index = draw_menu(screen, font, RES_X, RES_Y)
            if selected_menu:
                current_mode = selected_menu
                pygame.display.update()
        elif current_mode == "single":
            current_stage, game_init, game_running = single_player_game(screen, font, current_stage,
                                                                        game_init, game_running, RES_X, RES_Y)
        elif current_mode == "multi":
            pass


if __name__ == '__main__':
    init_game()
