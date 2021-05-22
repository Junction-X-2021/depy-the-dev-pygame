import socket

import pygame
import tkinter as tk

from common import server_address, server_port
from mainmenu import draw_menu
from singleplay import single_player_game, retry_menu

# 해상도 설정
root = tk.Tk()

RES_Y = root.winfo_screenheight()
RES_X = round(RES_Y * 0.7)


def init_game():
    pygame.init()
    pygame.display.set_caption("depy-the-dev")
    screen = pygame.display.set_mode((RES_X, RES_Y))

    server_socket = socket.socket()
    server_socket.connect((server_address, server_port))
    try:
        # 폰트 불러오기
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans MS', 30)
        current_mode = "menu"
        current_stage, game_init, game_running, game_stopped = 1, True, False, False
        while True:
            screen.fill((255, 255, 255))

            if current_mode == "menu":
                selected_menu, selected_index = draw_menu(screen, font, RES_X, RES_Y)
                if selected_menu:
                    current_mode = selected_menu
                    game_stopped = False
                    game_init = True
                    pygame.display.update()
            elif current_mode == "single":
                if game_stopped:
                    choice = retry_menu(screen, font, current_stage, RES_X, RES_Y)
                    if choice:
                        current_mode = choice
                        game_stopped = False
                        game_init = True
                else:
                    current_stage, game_init, game_running, game_stopped = single_player_game(server_socket, screen, font, current_stage, game_init, game_running, game_stopped, RES_X, RES_Y)
            elif current_mode == "multi":
                pass
            elif current_mode == "exit":
                break
    finally:
        server_socket.close()


if __name__ == '__main__':
    init_game()
