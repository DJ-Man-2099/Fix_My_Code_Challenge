#!/usr/bin/python3
""" Square class """


class Square():
    """ Square class """

    __width = 0

    def __init__(self, *args, **kwargs):
        """ Constructor """
        if len(args) > 0:
            self.width = args[0]
        else:
            for key, value in kwargs.items():
                if key == "width":
                    self.width = value

    @property
    def width(self):
        """ Width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Perimeter of the square"""
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """ String representation"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
