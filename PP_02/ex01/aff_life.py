#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


import matplotlib.pyplot as plt


def display(data):
    """display given dataset"""
    data.set_index("country", inplace=True)
    # print(data.loc['France'])
    data.loc['France'].plot()
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.show()
