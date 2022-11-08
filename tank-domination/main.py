import pygame

pygame.init()

# Game Setting.
monitor_display = (800,600)

game_display = pygame.display.set_mode(monitor_display)

pygame.display.set_caption("Tank domination")

system_Clock = pygame.time.Clock()

game_characteristics = {
    "sky":{
        "color": (135,206,235)
    }
}
# Game Ligic.
game_running_flag = True

while game_running_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running_flag = False

    if not game_running_flag:
        pygame.quit()

        break

    # running game mechanics.

    game_display.fill(game_characteristics["sky"]["color"])
    pygame.display.update()

    system_Clock.tick(30)