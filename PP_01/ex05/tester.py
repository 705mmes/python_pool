#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


from load_image import ft_load
from pimp_image import ft_green, ft_red, ft_blue, ft_grey, ft_invert


array = ft_load("landscape.jpg")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_invert.__doc__)
