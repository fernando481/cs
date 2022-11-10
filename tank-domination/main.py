import pygame

pygame.init()

# Game Setting.
monitor_display = (800,600)

game_display = pygame.display.set_mode(monitor_display)

pygame.display.set_caption("Tank domination")

system_Clock = pygame.time.Clock()

game_tank_svg = pygame.image.load("tank.svg")

game_tank_sprite = pygame.transform.scale(game_tank_svg, (75,75))

game_characteristics = {
    "sky":{
        "color": (135,206,235)
    },
    "grass":{
        "color":(0,255,0),
        "position": {
            "y":0.8 * monitor_display[1]
        }
    },"player": {
        "position":{
            "x": 0.2 * monitor_display[0]
        },
        "hp": 1
    },
    "cpu": {
        "position":{
            "x": 0.8 * monitor_display[0] - game_tank_sprite.get_width()
        },
        "hp": 1
    }
}
# Game Logic.
game_running_flag = True

while game_running_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running_flag = False

    if not game_running_flag:
        pygame.quit()

        break
        

    # movement 
    key_pressed = pygame.key.get_pressed()
    position_delta = 0 
        
    if key_pressed[pygame.K_LEFT]:
        position_deltal = -1 
    elif  key_pressed[pygame.K_RIGHT]:
        position_delta = 1 

    game_characteristics["player"]["position"]["x"] += position_delta



    # running game mechanics.

    game_display.fill(game_characteristics["sky"]["color"])

    # create grass.
    pygame.draw.rect(game_display,game_characteristics["grass"]["color"],pygame.Rect(0,game_characteristics["grass"]["position"]["y"],monitor_display[0],monitor_display[1]-game_characteristics["grass"]["position"]["y"]))

    # creat player and computer 
    game_tank_sprite_player = game_tank_sprite

    game_display.blit(game_tank_sprite_player, (game_characteristics["player"]["position"]["x"],game_characteristics["grass"]["position"]["y"]-game_tank_sprite_player.get_height()))

    game_tank_sprite_cpu = pygame.transform.flip(game_tank_sprite,True,False)

    game_display.blit(game_tank_sprite_cpu, (game_characteristics["cpu"]["position"]["x"],game_characteristics["grass"]["position"]["y"]-game_tank_sprite_cpu.get_height()))
    
    
    pygame.display.update()

    system_Clock.tick(30)