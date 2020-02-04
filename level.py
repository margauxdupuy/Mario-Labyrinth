#! /usr/bin/env python3
# coding: utf-8

import pygame
from labyrinth_data import *


class Level:
    """Class that create the level structure"""

    def __init__(self):
        # Initialization window
        pygame.init()
        self._window = pygame.display.set_mode((size_window_x, size_window_x))

        self._structure_level = []
        self._list_squares = {}

        self._coins = pygame.image.load(image_coins).convert()
        self._coins.set_colorkey((0, 0, 0))
        self._start = pygame.image.load(image_start).convert()
        self._wall = pygame.image.load(image_wall).convert()
        self._peach = pygame.image.load(image_peach)
        self._peach.set_colorkey((255, 255, 255))


    def get_structure(self, file_level):
        """This function gets the level structure according to the file txt"""
        with open(file_level, "r") as file:

            for line in file.readlines():
                line = line.replace("\n", "")
                self._structure_level.append(line)

        return  self._structure_level


    def display_structure(self):
        """This function displays the level structure according to the elements"""
        self._x = 0
        self._y = 0

        # Display the united background
        self._window.fill(color_background)
        pygame.display.update()

        for line in self._structure_level:

            for element in line:
                # start element
                if element == "s":
                    self._window.blit(self._start, (0, 0))
                # wall element
                if element == "1":
                    self._window.blit(self._wall, (self._x, self._y))
                # finish element
                if element == "p":
                    # We split the square sive in 1.5 because the img is not a square and we want to center it
                    self._window.blit(self._peach, (size_window_x-size_square/1.5, size_window_y-size_square))

                # Square's coordinates and nature
                self._square_coord = (self._x, self._y)
                self._list_squares[self._square_coord] = element

                self._x += size_square


            self._x = 0
            self._y += size_square


    def display_coins(self, list_coins):
        """This function displays the coins, it's separated because we need to call it once."""

        for coin in list_coins:
            self._window.blit(self._coins, coin)

