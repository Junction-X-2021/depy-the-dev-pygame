import pygame.font
import random

from player import Player

block_list = [(random.randint(0, 7), 0)]
block_list_all = []
block_img = pygame.image.load("assets/block.png")
block_img = pygame.transform.scale(block_img, (80, 60))
player: Player
ai: Player
start_tick: int
elapsed_time = 0


def single_player_game(screen: pygame.surface, font: pygame.font.Font,
                       current_stage, game_init, game_running, res_x, res_y):
    global block_list_all, block_list, block_img, player, ai, start_tick, elapsed_time

    def del_block(_block_list):
        _block_list = _block_list[1:]
        for idx in range(len(_block_list)):
            _block_list[idx] = _block_list[idx][0], _block_list[idx][1] - 1
        return _block_list

    # 블록 생성
    if not game_running:
        block_list = [(random.randint(0, 7), 0)]
        player = Player(block_list[0][0], block_list[0][1])
        ai = Player(block_list[0][0], block_list[0][1])
        start_tick = pygame.time.get_ticks()
        for block_y in range(1, 30 * current_stage):
            last_block_x = block_list[-1][0]
            if last_block_x == 0:
                block_x = last_block_x + 1
            elif last_block_x == 7:
                block_x = last_block_x - 1
            else:
                block_x = last_block_x + random.choice([-1, 1])
            block_list.append((block_x, block_y))
        block_list_all = block_list
        game_running = True

    if game_init:
        game_init = False

    # 블록 그리기
    hide_block_index = 15
    for block_x, block_y in block_list:
        screen.blit(block_img, [block_x * res_x * 0.125, block_y * res_y * 0.05 + res_y * 0.069])
    for key_event in pygame.event.get():
        # 플레이어 이동
        if key_event.type == pygame.KEYDOWN and len(block_list) > 1:
            if player.count < hide_block_index:
                block_index = player.count + 1
            else:
                block_index = hide_block_index
            if key_event.key == pygame.K_LEFT and block_list[block_index][0] == player.x - 1:
                player.move_to_left()
                # if 마지막 블럭 위치가 바닥 높이가 아니라면
                if player.count >= hide_block_index:
                    block_list = del_block(block_list)
                else:
                    player.y += 1
            elif key_event.key == pygame.K_RIGHT and block_list[block_index][0] == player.x + 1:
                player.move_to_right()
                # if 마지막 블럭 위치가 바닥 높이가 아니라면
                if player.count >= hide_block_index:
                    block_list = del_block(block_list)
                else:
                    player.y += 1
    player.draw(screen, res_x, res_y)
    if player.count == 30 * current_stage - 1:
        current_stage += 1
        game_running = False
    if elapsed_time != int((pygame.time.get_ticks() - start_tick) / 1000):
        ai.count += 1
        print(ai.count, player.count)
    elapsed_time = int((pygame.time.get_ticks() - start_tick) / 1000)
    timer = font.render(f"timer: {elapsed_time}", True, (0, 0, 0))
    screen.blit(timer, (10, 10))
    stage = font.render(f"stage: {current_stage}", True, (0, 0, 0))
    screen.blit(stage, (10, 50))
    if elapsed_time > 5:
        if player.count - ai.count < 15:
            ai_x = block_list_all[ai.count][0] * res_x*0.125 + res_x*0.0125
            ai_y = (player.y - player.count + ai.count) * res_y*0.05 + res_y*0.042
            screen.blit(ai.player_image, [ai_x, ai_y])
        if player.count == ai.count:
            pass

    pygame.display.update()
    return current_stage, game_init, game_running
