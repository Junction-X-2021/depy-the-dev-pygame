import pygame.font

selected_index = 0


def draw_menu(screen: pygame.surface, font: pygame.font.Font, key_event):
    global selected_index
    single_player_menu = font.render("Single Play", False, (255, 255, 255))
    multi_player_menu = font.render("Multi Play", False, (255, 255, 255))

    screen.blit(single_player_menu, (240, 300))
    screen.blit(multi_player_menu, (240, 360))
    if key_event[pygame.K_UP]:
        selected_index -= 1
    elif key_event[pygame.K_DOWN]:
        selected_index += 1
    selected_index = selected_index % 2
    if key_event[pygame.K_RETURN]:
        if selected_index == 0:
            return "multi"
        else:
            return "single"
    polygon_y = 300 + selected_index * 60
    pygame.draw.polygon(screen, (255, 255, 255), [[200, polygon_y], [200, polygon_y+30], [230, polygon_y+15]])
    pygame.display.update()
