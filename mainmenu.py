import pygame.font

selected_index = 0


def draw_menu(screen: pygame.surface, font: pygame.font.Font, res_x, res_y):
    global selected_index

    text_surface = font.render("Single Play", False, (0, 0, 0))
    rect = text_surface.get_rect(center=(res_x*0.5, res_y*0.2))
    screen.blit(text_surface, rect)
    text_surface = font.render("Multi Play", False, (0, 0, 0))
    rect = text_surface.get_rect(center=(res_x*0.5, res_y*0.25))
    screen.blit(text_surface, rect)

    for key_event in pygame.event.get():
        if key_event and key_event.type == pygame.KEYDOWN:
            if key_event.key == pygame.K_UP:
                selected_index -= 1
            elif key_event.key == pygame.K_DOWN:
                selected_index += 1
            selected_index = selected_index % 2
            if key_event.key == pygame.K_RETURN:
                if selected_index == 0:
                    return "single", selected_index
                else:
                    return "multi", selected_index
        polygon_y = res_y*0.200 + selected_index * res_y*0.05
        pygame.draw.polygon(screen, (0, 0, 0), [[res_x*0.3125, polygon_y], [res_x*0.3125, polygon_y+res_y*0.0208], [res_x*0.359, polygon_y+res_y*0.01042]])
        pygame.display.update()
        return None, selected_index
    return None, selected_index
