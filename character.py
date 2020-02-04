#! /usr/bin/env python3
# coding: utf-8

import pygame
from labyrinth_data import *


class Character:
    """Class that create a character"""

    def __init__(self):
        self._mario_image = pygame.image.load(image_mario).convert_alpha()
        self._position_mario = self._mario_image.get_rect()



    def move(self, direction):
        """This function manages the character moves """
        self._direction_x = 0
        self._direction_y = 0


        # In the limite of the map (size window)
        if(direction == "up" and self._position_mario[1] > 0):
            self._direction_y -= size_square
            self._position_mario = self._position_mario.move(self._direction_x, self._direction_y)

        if (direction == "right" and self._position_mario[0] < size_window_x-size_square):
            self._direction_x += size_square
            self._position_mario = self._position_mario.move(self._direction_x, self._direction_y)

        if (direction == "down" and self._position_mario[1] < size_window_y-size_square):
            self._direction_y += size_square
            self._position_mario = self._position_mario.move(self._direction_x, self._direction_y)

        if (direction == "left" and self._position_mario[0] > 0):
            self._direction_x -= size_square
            self._position_mario = self._position_mario.move(self._direction_x, self._direction_y)

