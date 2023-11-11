#!/usr/bin/python3
"""rectangle module"""

from models.base import Base


class Rectangle(Base):
    """represents a rectangle object class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle Object"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ses the val of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the val of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """this programme returns the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """displays a full rectangle"""
        for lines in range(self.y):
            print("")
        for i in range(self.height):
            for n in range(self.width + self.x):
                if n < self.x:
                    print(" ", end="")
                else:
                    print("#", end="")
            print("")

    def __str__(self):
        """string presentation of rectangle"""
        r = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        c = "{}/{} - {}/{}".format(
                self.x, self.y, self.width, self.height)
        return r + c

    def update(self, *args, **kwargs):
        """updates a method that assigns an
        argument to each attribute"""
        if args or len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(
                                self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            if kwargs or len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(
                                    self.width, self.height, self.x, self.y)
                        else:
                            self.id = value
                    if key == "width":
                        self.width = value
                    if key == "height":
                        self.height = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

    def to_dictionary(self):
        """returns a dictionary presentation
        of rectangle"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
