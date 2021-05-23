import pickle
import socket

import pygame
import tkinter as tk

from common import server_address, server_port
from mainmenu import draw_menu
from singleplay import single_player_game, retry_menu
from multiplayer import multi_player_init, multi_player_game, room_name


# 해상도 설정
root = tk.Tk()

RES_Y = root.winfo_screenheight()
RES_X = round(RES_Y * 0.7)
playing_time = 0


def init_game():
    global playing_time

    pygame.init()
    pygame.display.set_caption("depy-the-dev")
    screen = pygame.display.set_mode((RES_X, RES_Y))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, server_port))
    start_tick = pygame.time.get_ticks()
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
                    current_mode = retry_menu(screen, font, current_stage, RES_X, RES_Y)
                else:
                    current_stage, game_init, game_running, game_stopped = single_player_game(client_socket, screen, font, current_stage, game_init, game_running, game_stopped, RES_X, RES_Y)
            elif current_mode == "multi":
                if game_init:
                    game_init = multi_player_init(client_socket, screen, font, RES_X, RES_Y)
                else:
                    # current_stage, game_init, game_running, game_stopped = single_player_game(client_socket, screen, font, current_stage, game_init, game_running, game_stopped, RES_X, RES_Y)
                    pass
            elif current_mode == "exit":
                break
            if playing_time != int((pygame.time.get_ticks() - start_tick) / 1000):
                playing_time = int((pygame.time.get_ticks() - start_tick) / 1000)
                client_socket.send(pickle.dumps({"chat": []}))
    finally:
        client_socket.close()


if __name__ == '__main__':
    init_game()