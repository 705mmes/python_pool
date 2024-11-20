#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


def mean(args):
    res = 0
    for i in args:
        res += i
    res = res / len(args)
    print("mean:", res)


def median(args):
    sorted_list = sorted(args)
    index = int(len(sorted_list) / 2)
    print("median:", sorted_list[index])


def quartile(args):
    sorted_list = sorted(args)
    Q1 = int(len(sorted_list) / 4)
    Q3 = int(len(sorted_list) / 2) + int(len(sorted_list) / 4)
    print(f"quartile: [{sorted_list[Q1]}, {sorted_list[Q3]}]")


def variance(args):
    lst_mean = 0
    for i in args:
        lst_mean += i
    lst_mean = lst_mean / len(args)
    new_lst = []
    for i in args:
        new_lst.append((i - lst_mean) * (i - lst_mean))
    res = 0
    for i in new_lst:
        res += i
    res = res / len(args)
    return res


def standard_deviation(args):
    var = variance(args)
    res = var ** 0.5
    print("std:", res)


def ft_statistics(*args: any, **kwargs: any) -> None:
    if len(args) <= 0:
        return print("ERROR: args is empty")
    for i in kwargs:
        if kwargs[i] == "mean":
            mean(args)
        elif kwargs[i] == "median":
            median(args)
        elif kwargs[i] == "quartile":
            quartile(args)
        elif kwargs[i] == "std":
            standard_deviation(args)
        elif kwargs[i] == "var":
            var = variance(args)
            print("var:", var)
