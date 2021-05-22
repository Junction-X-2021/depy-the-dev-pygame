import pygame.font

selected_index = 0


def draw_menu(screen: pygame.surface, font: pygame.font.Font, res_x, res_y):
    global selected_index

    single_player_menu = font.render("Single Play", False, (0, 0, 0))
    multi_player_menu = font.render("Multi Play", False, (0, 0, 0))

    screen.blit(single_player_menu, (res_x*0.375, res_y*0.208))
    screen.blit(multi_player_menu, (res_x*0.375, res_y*0.25))

    for key_event in pygame.event.get():
        if key_event and key_event.type == pygame.KEYDOWN:
            if key_event.key == pygame.K_UP:
                selected_index = 0
            elif key_event.key == pygame.K_DOWN:
                selected_index = 1
            if key_event.key == pygame.K_RETURN:
                if selected_index == 0:
                    return "single", selected_index
                else:
                    return "multi", selected_index
        polygon_y = res_y*0.208 + selected_index * res_y*0.042
        pygame.draw.polygon(screen, (0, 0, 0), [[res_x*0.3125, polygon_y], [res_x*0.3125, polygon_y+res_y*0.0208], [res_x*0.359, polygon_y+res_y*0.01042]])
        pygame.display.update()
        return None, selected_index
    return None, selected_index
