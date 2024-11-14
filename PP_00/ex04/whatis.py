#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


import sys


assert len(sys.argv) == 2, "Wrong number of arguments"
assert isinstance(int(sys.argv[1]), int), "argument is not an integer"
if int(sys.argv[1]) % 2 == 0:
	print("I'm Even.")
else:
	print("I'm Odd.")
	