#!/usr/bin/python3
"""Module"""


class square():
    """ Class Square """
    width = 0

    def __init__(self, *args, **kwargs):
        """ Initialize """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Calculating Permiter """
        return self.width * 4

    def __str__(self):
        """ String format """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    """ Another doc :') """
    s = square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
