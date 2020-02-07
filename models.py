#! /usr/bin/env python3
# coding: utf-8

import json
import os
import pygame

from settings import size_square, size_window_x, size_window_y, image_mario, image_coins, image_start,\
    image_wall, image_peach, color_background


class Character:
    """Class that create a character"""

    def __init__(self):
        self.mario_image = pygame.image.load(image_mario).convert_alpha()
        self.position_mario = self.mario_image.get_rect()


    def move(self, direction):
        """This function manages the character moves """
        self._direction_x = 0
        self._direction_y = 0

        # In the limit of the map (size window)
        if direction == "up" and self.position_mario[1] > 0:
            self._direction_y -= size_square
            self.position_mario = self.position_mario.move(self._direction_x, self._direction_y)

        if direction == "right" and self.position_mario[0] < size_window_x-size_square:
            self._direction_x += size_square
            self.position_mario = self.position_mario.move(self._direction_x, self._direction_y)

        if direction == "down" and self.position_mario[1] < size_window_y-size_square:
            self._direction_y += size_square
            self.position_mario = self.position_mario.move(self._direction_x, self._direction_y)

        if direction == "left" and self.position_mario[0] > 0:
            self._direction_x -= size_square
            self.position_mario = self.position_mario.move(self._direction_x, self._direction_y)


class Level:
    """Class that create the level structure"""

    def __init__(self, file_level):
        self.list_squares = {}

        self._window = pygame.display.set_mode((size_window_x, size_window_x))
        self._coins = pygame.image.load(image_coins).convert()
        self._coins.set_colorkey((0, 0, 0))
        self._start = pygame.image.load(image_start).convert()
        self._wall = pygame.image.load(image_wall).convert()
        self._peach = pygame.image.load(image_peach)
        self._peach.set_colorkey((255, 255, 255))

        # Level structure according to the file txt
        self._structure_level = []
        with open(file_level, "r") as file:

            for line in file.readlines():
                line = line.replace("\n", "")
                self._structure_level.append(line)

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
                self.list_squares[self._square_coord] = element

                self._x += size_square

            self._x = 0
            self._y += size_square

    def display_coins(self, list_coins):
        """This function displays the coins, it's separated because we need to call it once."""

        for coin in list_coins:
            self._window.blit(self._coins, coin)


class Player:

    def __init__(self):
        self.file_name = "scores.json"
        self._scores = {}

    def get_score(self, player_name):
        """This function gets the scores and return an object {} with the score associated to the player."""

        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                self._scores = json.load(file)
                if player_name not in self._scores:
                    self._scores[player_name] = 0
        else:
            self._scores[player_name] = 0

        return self._scores

    def save_scores(self, players_scores):
        """This function save the player's score in a file."""

        with open(self.file_name, "w") as file:
            json.dump(players_scores, file)
