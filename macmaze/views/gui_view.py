# -*- coding: utf-8 -*-
"""Manage the display of every elements of the game"""

import pygame
from pygame.locals import *

from config import constants



class GUIview:

    def __init__(self, board):
        self.board = board
    
    def draw_board(self, screen):

        for y, line in enumerate(self.board.grid):

            for tile in self.board.grid[y]:
                x = tile.x_square * constants.TILE_SIZE
                y = tile.y_square * constants.TILE_SIZE

                tile_image = constants.reach_image(constants.IMAGES_DICT[tile.visual])
                tile_surf = pygame.image.load(tile_image).convert()
                screen.blit(tile_surf, (x,y))

                if tile.toping:
                    toping_image = constants.reach_image(constants.IMAGES_DICT[tile.toping])
                    toping_surf = pygame.image.load(toping_image).convert()
                    screen.blit(toping_surf, (x, y))
