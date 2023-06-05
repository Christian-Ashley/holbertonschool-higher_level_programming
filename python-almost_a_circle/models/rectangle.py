#!/usr/bin/python3
"""Definition of Rectangle"""
from . base import Base


class Rectangle(Base):
    """define a rectangle object

    Args:
        Base (class): Base Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """rectangle constructor

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int, optional): x offset of rectangle. Defaults to 0.
            y (int, optional): y offset of rectangle. Defaults to 0.
            id (int, optional): identifier. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def display(self):
        """Print the Rectangle instance with the character #"""
        for i in range(self.height):
            print("#" * self.width)
