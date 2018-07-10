import pygame

import game_object

from input.input_manager import InputManager

BG = (0, 0, 0)

# 1. Init pygame
pygame.init()

# 2. Set screen
SIZE = (800, 600)
canvas = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Jet zero')

# 3. Clock
clock = pygame.time.Clock()

loop = True

input_manager = InputManager()

while loop:
    # 1. Event processing
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            input_manager.update(event)

    game_object.update()

    # 2. Draw
    canvas.fill(BG)

    game_object.render(canvas)

    # 3. Flip
    pygame.display.flip()
    clock.tick(60)
