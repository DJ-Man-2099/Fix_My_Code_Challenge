#!/usr/bin/python3
""" Square class """


class square():
    """ Square class """

    size = 0

    def __init__(self, *args, **kwargs):
        """ Constructor """
        if len(args) > 0:
            self.size = args[0]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.size * self.size

    def PermiterOfMySquare(self):
        """ Perimeter of the square"""
        return (self.size * 4)

    def __str__(self):
        """ String representation"""
        return "{}".format(self.size)


if __name__ == "__main__":
    s = square(size=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
