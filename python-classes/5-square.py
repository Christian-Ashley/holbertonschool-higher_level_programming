#!/usr/bin/python3
"""this class kills facists:"""


Sure, I'd be happy to add some documentation! Here's the updated implementation with documentation included:

class Square:
    """
    Represents a square with a size attribute and methods to calculate its area and print it.
    """
    def __init__(self, size=0):
        """
        Initializes an instance of the Square class with the given size attribute.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size
    
    @property
    def size(self):
        """
        The size attribute of the square.

        Returns:
            int: The size attribute.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Sets the size attribute of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
    
    def my_print(self):
        """
        Prints the square using the '#' character for each side. If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print()
