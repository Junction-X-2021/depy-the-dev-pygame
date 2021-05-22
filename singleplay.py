import pygame.font
import random

from player import Developer

block_list = [(random.randint(0, 8), 0)]
block_img = pygame.image.load("assets/block.png")
block_img = pygame.transform.scale(block_img, (80, 60))
player: Developer


def single_player_game(screen: pygame.surface, font: pygame.font.Font, key_event,
                       current_stage, game_init, game_running, res_x, res_y):
    global block_list, block_img, player

    def del_block(_block_list):
        _block_list = _block_list[1:]
        for idx in range(len(_block_list)):
            _block_list[idx] = _block_list[idx][0], _block_list[idx][1]-1
        return _block_list

    # 블록 생성
    if not game_running:
        block_list = [(random.randint(0, 8), 0)]
        player = Developer(block_list[0][0], block_list[0][1])
        for block_y in range(1, 30*current_stage):
            last_block_x = block_list[-1][0]
            if last_block_x == 0:
                block_x = last_block_x + 1
            elif last_block_x == 7:
                block_x = last_block_x - 1
            else:
                block_x = last_block_x + random.choice([-1, 1])
            block_list.append((block_x, block_y))
        game_running = True

    if game_init:
        game_init = False

    # 블록 그리기
    for block_x, block_y in block_list:
        screen.blit(block_img, [block_x*res_x*0.125, block_y*res_y*0.05+res_y*0.069])
    # 플레이어 이동
    if key_event.type == pygame.KEYDOWN and len(block_list) > 1:
        if key_event.key == pygame.K_LEFT and block_list[1][0] == player.x - 1:
            player.move_to_left()
            #if 마지막 블럭 위치가 바닥 높이가 아니라면
            block_list = del_block(block_list)
        elif key_event.key == pygame.K_RIGHT and block_list[1][0] == player.x + 1:
            player.move_to_right()
            #if 마지막 블럭 위치가 바닥 높이가 아니라면
            block_list = del_block(block_list)
    player.draw(screen, res_x, res_y)
    if player.y == 30*current_stage - 1:
        current_stage += 1
        game_running = False

    pygame.display.update()
    return current_stage, game_init, game_running
