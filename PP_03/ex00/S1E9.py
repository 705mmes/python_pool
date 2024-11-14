#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Your docstring for Method"""
        if self.is_alive is True:
            self.is_alive = False


class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name=first_name, is_alive=is_alive)
