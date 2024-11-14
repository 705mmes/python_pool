#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter


def display(a, b):
    """display relation between the 2 given datasets"""
    plt.scatter(a['1900'], b['1900'], color='blue')

    plt.xscale('log')
    formatter = EngFormatter()
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.xticks([300, 1000, 10000])

    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.title("1900")
    plt.show()
