#! /usr/bin/env python3
# coding: utf-8

import pygame
from pygame.locals import KEYDOWN, QUIT, K_ESCAPE, K_1, K_2, K_KP1, K_KP2, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_RETURN
from time import sleep
from sys import argv

from settings import size_square, size_window_x, size_window_y, window_title, image_icon, image_home, image_final,\
    square_background, main_theme, level_complete, coin_sound, file_level1, file_level2
from models import Character, Level, Player


def play_sound(sound):
    return pygame.mixer.Sound(sound).play()


def display_image(image):
    image_loaded = pygame.image.load(image).convert()
    window.blit(image_loaded, (0, 0))
    pygame.display.flip()


if __name__ == '__main__':

    # Initialization
    pygame.init()
    window = pygame.display.set_mode((size_window_x, size_window_y))
    pygame.display.set_caption(window_title)

    icon = pygame.image.load(image_icon).convert()
    pygame.display.set_icon(icon)

    # Create a player
    player = Player()
    player_name = argv[1].capitalize()
    player_scores = player.get_score(player_name)
    continue_game = True

    while continue_game:
        continue_home = True
        play = True
        continue_final = False
        file_level = 0

        # Home screen
        display_image(image_home)
        print("Let's go {0}! Your actual score is {1}".format(player_name, player_scores[player_name]))

        # Display the home page until the player is ready
        while continue_home:
            # Limitation of loop speed
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():

                # Quit the game
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    play = False
                    continue_home = False
                    continue_game = False

                # Touch 1 for Level 1, Touch 2 for Level 2
                elif event.type == KEYDOWN:
                    if event.key == K_1 or event.key == K_KP1:
                        continue_home = False
                        file_level = file_level1

                    if event.key == K_2 or event.key == K_KP2:
                        continue_home = False
                        file_level = file_level2

        # Loading background if the player has made a choice
        # All of these need to be out of the play loop.
        if file_level != 0:

            # Generate the map structure according to the level
            game_map = Level(file_level)
            game_map.display_structure()

            # Add all the positions of coins in a list
            list_coins = [coordinates for coordinates in game_map.list_squares
                          if game_map.list_squares[coordinates] == "c"]

            # Generate mario character with its speed
            mario = Character()
            pygame.key.set_repeat(400, 30)

            # Main theme song
            music_game = play_sound(main_theme)

        # Display the labyrinth
        while play:

            position_character = (mario.position_mario[0], mario.position_mario[1])

            list_walls = [coordinates for coordinates in game_map.list_squares
                          if game_map.list_squares[coordinates] == "1"]

            for event in pygame.event.get():

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    play = False
                    continue_game = False

                if event.type == KEYDOWN:

                    # We check if the future position is in wall's location, if there is no wall, the player can move
                    if event.key == K_UP:
                        future_position = (mario.position_mario[0], mario.position_mario[1]-size_square)
                        if future_position not in list_walls:
                            mario.move("up")
                    if event.key == K_RIGHT:
                        future_position = (mario.position_mario[0]+size_square, mario.position_mario[1])
                        if future_position not in list_walls:
                            mario.move("right")
                    if event.key == K_DOWN:
                        future_position = (mario.position_mario[0], mario.position_mario[1]+size_square)
                        if future_position not in list_walls:
                            mario.move("down")
                    if event.key == K_LEFT:
                        future_position = (mario.position_mario[0]-size_square, mario.position_mario[1])
                        if future_position not in list_walls:
                            mario.move("left")

                # If Mario gets a coin
                if position_character in list_coins:
                    play_sound(coin_sound)
                    # Visually, we remove the coins and paste a background image
                    display_image(square_background)
                    # Remove this coin from the list of coins so that it is not display anymore
                    list_coins.remove(position_character)

                    if list_coins:
                        still_coins = False
                    player_scores[player_name] += 1

                # If Mario finds Peach
                if position_character == (size_window_x - size_square, size_window_y - size_square):

                    music_game.stop()

                    play_sound(level_complete)

                    sleep(2)
                    continue_final = True
                    play = False

                    # Score attribution according to level
                    if file_level == file_level1:
                        player_scores[player_name] += 2
                    if file_level == file_level2:
                        player_scores[player_name] += 4

            game_map.display_structure()
            game_map.display_coins(list_coins)

            window.blit(mario.mario_image, mario.position_mario)
            pygame.display.flip()

            # Final screen
            while continue_final:
                # Limitation of loop speed
                pygame.time.Clock().tick(30)

                display_image(image_final)

                for event in pygame.event.get():

                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        continue_final = False
                        continue_game = False

                    # The player can play again
                    if event.type == KEYDOWN and event.key == K_RETURN:
                        continue_final = False

    player.save_scores(player_scores)

    print("Your final score is {} points. See you !".format(player_scores[player_name]))
