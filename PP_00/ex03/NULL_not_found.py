#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-?


def NULL_not_found(object: any) -> int:
	if object == None:
		print("Nothing:", object, type(object))
	elif object != object:
		print("Cheese:", object, type(object))
	elif type(object) == bool:
		print("Fake:", object, type(object))
	elif type(object) == int:
		print("Zero:", object, type(object))
	elif object == '':
		print("Empty:", object, type(object))
	else:
		print("Type not Found")
		return (1)
	return (0)
