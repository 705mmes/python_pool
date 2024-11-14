#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Representing the Baratheon family."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """docstring for __str__"""
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self):
        """docstring for __repr__"""
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'


class Lannister(Character):
    """Representing the Lannister family."""
    @staticmethod
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def create_lannister(first_name, is_alive):
        """returns a lannister obj"""
        return Lannister(first_name, is_alive)

    def __str__(self):
        """docstring for __str__"""
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self):
        """docstring for __repr__"""
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'
