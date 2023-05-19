#!/usr/bin/python3
"""a class for squares with stuff!!:"""


class Square:
    """this class makes sure that size is an integer and tells 
    you if you fucked that up and how:"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
