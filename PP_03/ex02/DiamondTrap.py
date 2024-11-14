#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name=first_name, is_alive=is_alive)

    def set_eyes(self, color):
        """sets eyes color"""
        self.eyes = color

    def set_hairs(self, color):
        """sets hairs color"""
        self.hairs = color

    def get_eyes(self):
        """gets eyes color"""
        return self.eyes

    def get_hairs(self):
        """gets hairs color"""
        return self.hairs
