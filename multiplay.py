from player import player

def multi_player_game(server_socket, screen, font,
                        current_stage,  game_running, game_stopped, RES_X, RES_Y):
    if not game_running:
            block_list = [] # 서버에서 맵데이터 받아오기

            user = player(block_list[0][0], block_list[0][1])
            enemy = player(block_list[0][0], block_list[0][1])
    return current_stage, game_running, game_stopped


