#!/usr/bin/python3
""" Base Geometry class inherited"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

""" Function that creates a rectangle and instantation of values"""

class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
