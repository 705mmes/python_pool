#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
from matplotlib.pyplot import legend


def convert_population(value):
    """converts value to numerical values"""
    if 'M' in value:
        return float(value.replace('M', '')) * 1e6
    elif 'B' in value:
        return float(value.replace('B', '')) * 1e9
    elif 'K' in value:
        return float(value.replace('K', '')) * 1e3
    else:
        return float(value)


def display(data):
    """display given dataset"""
    data.set_index("country", inplace=True)

    france_data = data.loc['France'][:-50].apply(convert_population)
    germany_data = data.loc['Germany'][:-50].apply(convert_population)
    france_data.plot()
    germany_data.plot()

    formatter = EngFormatter()
    plt.gca().yaxis.set_major_formatter(formatter)

    legend()

    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')
    plt.show()
