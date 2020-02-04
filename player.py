#! /usr/bin/env python3
# coding: utf-8

import json
import os
import sys


class Player:

    def __init__(self):
        self.file_name = "scores.json"


    def get_score(self, player_name):
        """This function gets the scores and return an object {} with the score associated to the player."""

        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                self._scores = json.load(file)
                if not player_name in self._scores:
                    self._scores[player_name] = 0
        else:
            self._scores = {}
            self._scores[player_name] = 0

        return self._scores



    def save_scores(self, players_scores):
        """This function save the player's score in a file."""

        with open(self.file_name, "w") as file:
            json.dump(players_scores, file)



    def get_username(self):
        """This function gets the player's username and checks if it is composed at least 4 characters."""

        self._player_name = sys.argv[1].capitalize()

        if len(self._player_name) < 4:
            print("This name is invalid, please enter at least 4 characters")
            self.get_username()
        else:
            return self._player_name
