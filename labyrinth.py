#! /usr/bin/env python3
# coding: utf-8



from pygame.locals import *
import time

from character import *
from level import *
from player import *



# Initialization
pygame.init()
window = pygame.display.set_mode((size_window_x, size_window_x))
pygame.display.set_caption(window_title)

icon = pygame.image.load(image_icon)
pygame.display.set_icon(icon)

player = Player()
player_name = player.get_username()
player_scores = player.get_score(player_name)

continue_game = True


while continue_game:
    continue_home = True
    play = True
    continue_final = False
    file_level = 0

    # Home screen
    home = pygame.image.load(image_home).convert()
    window.blit(home, (0,0))
    pygame.display.flip()

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
        game_map = Level()
        structure_map = game_map.get_structure(file_level)
        game_map.display_structure()

        # Add all the positions of coins in a list
        list_coins = [coordinates for coordinates in game_map._list_squares if game_map._list_squares[coordinates] == "c"]

        # Generate mario character with its speed
        mario = Character()
        pygame.key.set_repeat(400, 30)

        # Main theme song
        music_game = pygame.mixer.Sound(main_theme)
        music_game.play()


    # Display the labyrinth
    while play:

        position_character = (mario._position_mario[0], mario._position_mario[1])

        list_walls = [coordinates for coordinates in game_map._list_squares if game_map._list_squares[coordinates] == "1"]

        for event in pygame.event.get():

            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                play = False
                continue_game = False

            if event.type == KEYDOWN:

                # We check if the future position is in wall's location, if there is no wall, the player can move
                if event.key == K_UP :
                    future_position = (mario._position_mario[0], mario._position_mario[1]-size_square)
                    if not future_position in list_walls:
                        mario.move("up")
                if event.key == K_RIGHT:
                    future_position = (mario._position_mario[0]+size_square, mario._position_mario[1])
                    if not future_position in list_walls:
                        mario.move("right")
                if event.key == K_DOWN:
                    future_position = (mario._position_mario[0], mario._position_mario[1]+size_square)
                    if not future_position in list_walls:
                        mario.move("down")
                if event.key == K_LEFT:
                    future_position = (mario._position_mario[0]-size_square, mario._position_mario[1])
                    if not future_position in list_walls:
                        mario.move("left")


            # If Mario gets a coin
            if position_character in list_coins:

                music_coin = pygame.mixer.Sound(coin_sound)
                music_coin.play()

                # Visually, we remove the coins and paste a background image
                square = pygame.image.load(square_background).convert()
                window.blit(square, (0,0))
                pygame.display.flip()

                # Remove this coin from the list of coins so that it is not display anymore
                list_coins.remove(position_character)

                if list_coins != []:
                    still_coins = False

                player_scores[player_name] += 1



            # If Mario finds Peach
            if (position_character == (size_window_x - size_square, size_window_y - size_square)):

                music_game.stop()

                music_win = pygame.mixer.Sound(level_complete)
                music_win.play()

                time.sleep(2)
                continue_final = True
                play = False


        game_map.display_structure()
        game_map.display_coins(list_coins)

        window.blit(mario._mario_image, mario._position_mario)
        pygame.display.flip()


        # Final screen
        while continue_final:

            # Limitation of loop speed
            pygame.time.Clock().tick(30)

            final = pygame.image.load(image_final).convert()
            window.blit(final, (0, 0))
            pygame.display.flip()


            for event in pygame.event.get():

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    continue_final = False
                    continue_game = False

                # The player can play again
                if event.type == KEYDOWN and event.key == K_RETURN:
                    continue_final = False


    # Score attribution according to level
    if file_level == file_level1:
        player_scores[player_name] += 2
    if file_level == file_level2:
        player_scores[player_name] += 4


player.save_scores(player_scores)

print("Your final score is {} points. See you !".format(player_scores[player_name]))
