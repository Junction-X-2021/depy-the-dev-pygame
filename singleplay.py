import pygame.font
import random

from player import Developer

block_list = [(random.randint(0, 8), 0)]
block_img = pygame.image.load("assets/block.png")
block_img = pygame.transform.scale(block_img, (80, 60))
player: Developer


def single_player_game(screen: pygame.surface, font: pygame.font.Font, key_event,
                       current_stage, game_init, game_running):
    global block_list, block_img, player

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
        screen.blit(block_img, [block_x*80, block_y*30+100])
    # 플레이어 이동
    if key_event.type == pygame.KEYDOWN:
        if key_event.key == pygame.K_LEFT:
            player.move_to_left()
        elif key_event.key == pygame.K_RIGHT:
            player.move_to_right()
    player.draw(screen)
    print([player.x * 80 + 8, player.y * 30 + 60])
    pygame.display.update()
    return current_stage, game_init, game_running
