from gift.gift import Gift
import pygame
import game_object

def create_gift():

    gift = Gift(600, 200)
    game_object.add(gift)
    
