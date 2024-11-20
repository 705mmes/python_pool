#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student class"""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id)

    def    __post_init__(self):
        try:
            if "id" in self.__dict__:
                raise TypeError("Student.__init__() got an unexpected keyword argument 'id'")
            self.login = self.name[0] + self.surname[0:].lower()
        except TypeError as msg:
            print("TypeError:", msg)
            exit("TypeError stopped execution")