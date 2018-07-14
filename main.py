import pygame

from gameover.gameover import GameOver
from player import create_player
from enemy import create_enemy
from gift import  create_gift, create_coin
import game_object
from game_object import game_objects, remove, render, update

from scenes.scene_manager import global_scene_manager
from scenes.gameplay_scene import GameplayScene

from input.input_manager import global_input_manager
from maps.map_generate_map import generate_map
from player.player import Player
from scenes.game_over_scene import GameOverScene
# from scenes.scene_manager import global_scene_manager


# BG = pygame.image.load("assets/images/36987938_870119473192633_6676325747356860416_n.png")

# 1. Init pygame
pygame.init()

# 2. Set screen
SIZE = (40*16, 30*16)
canvas = pygame.display.set_mode(SIZE)

pygame.display.set_caption('Hello baibe')
# 3. Clock
clock = pygame.time.Clock()

loop = True

gameplay_scene = GameplayScene()
global_scene_manager.change_scene(gameplay_scene)
# 4. music :
pygame.mixer.music.load('music/game_music.wav')
pygame.mixer.music.play(-1)





while loop:
    # 1. Event processing
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            global_input_manager.update(event)
    for game_object in game_objects :
        if type(game_object) == GameOver and game_object.is_active and global_input_manager.x_pressed:
            gameplay_scene = GameplayScene()
            global_scene_manager.change_scene(gameplay_scene)

    # if player.is_active:
    update()

    # 2. Draw
    # canvas.blit(BG,(0,0))
    canvas.fill((0, 0, 0))

    render(canvas)
    remove()
    # canvas.blit(image, (0, 0))
    # 3. Flip
    pygame.display.flip()
    clock.tick(60)
