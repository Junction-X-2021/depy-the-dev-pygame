import pygame.font


def draw_menu(screen: pygame.surface, font: pygame.font.Font, key_event, selected_index):
    single_player_menu = font.render("Single Play", False, (0, 0, 0))
    multi_player_menu = font.render("Multi Play", False, (0, 0, 0))

    screen.blit(single_player_menu, (240, 300))
    screen.blit(multi_player_menu, (240, 360))
    if key_event is None:
        selected_index = 0
    elif key_event and key_event.type == pygame.KEYDOWN:
        if key_event.key == pygame.K_UP:
            selected_index = 0
        elif key_event.key == pygame.K_DOWN:
            selected_index = 1
        if key_event.key == pygame.K_RETURN:
            if selected_index == 0:
                return "single", selected_index
            else:
                return "multi", selected_index
    polygon_y = 300 + selected_index * 60
    pygame.draw.polygon(screen, (0, 0, 0), [[200, polygon_y], [200, polygon_y+30], [230, polygon_y+15]])
    pygame.display.update()
    return None, selected_index
