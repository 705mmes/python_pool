#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


class calculator:
    """Your docstring for Calculator class"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Your docstring for Method dotproduct"""
        res = 0
        for x, y in zip(V1, V2):
            res += (x * y)
        print("Dot product is", res)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Your docstring for Method add"""
        res = [x + y for x, y in zip(V1, V2)]
        print("Add Vector is", res)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Your docstring for Method sous"""
        res = [x - y for x, y in zip(V1, V2)]
        print("Sous Vector is", res)
