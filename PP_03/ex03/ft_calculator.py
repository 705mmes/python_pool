#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


class calculator:
    """Your docstring for Class"""
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object) -> None:
        """Your docstring for Method add"""
        print("object:", object)
        for i in range(len(self.vector)):
            self.vector[i] += object
        print(self.vector)

    def __mul__(self, object) -> None:
        """Your docstring for Method mul"""
        for i in range(len(self.vector)):
            self.vector[i] *= object
        print(self.vector)

    def __sub__(self, object) -> None:
        """Your docstring for Method sub"""
        for i in range(len(self.vector)):
            self.vector[i] -= object
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Your docstring for Method div"""
        if object == 0:
            print("object is 0")
            return None
        for i in range(len(self.vector)):
            self.vector[i] /= object
        print(self.vector)
