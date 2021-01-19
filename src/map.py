from point import Point
from math import pi, cos, sin, tan

def cotan(x):
    if x % pi != 0:
        return cos(x)/sin(x)
    else:
        raise ValueError('cotan is not defined for this value')

class Map:
    def __init__(self, midlength, res = 1):
        self.length = 2 * midlength + 1
        self.resolution = res
        self.map = [Point() for i in range(self.length * self.length)]

    def getPoint(self, x, y):
        return self.map[x + y * self.length]

    def getExtremityFromDirection(self, orientation):
        if (orientation >= 0 and orientation < pi / 4) or (orientation >= 7 * pi / 4 and orientation < 2 * pi):
            return [self.length - 1, round((self.length - 1) / 2 * (1 - tan(orientation)))]
        elif (orientation >= pi / 4 and orientation < 3 * pi / 4):
            return [round((self.length - 1) / 2 * (1 + cotan(orientation))), 0]
        elif (orientation >= 3 * pi / 4 and orientation < 5 * pi / 4):
            return [0, round((self.length - 1) / 2 * (1 + tan(orientation)))]
        elif (orientation >= 5 * pi / 4 and orientation < 7 * pi / 4):
            return [round((self.length - 1) / 2 * (1 - cotan(orientation))), self.length - 1]
        else:
            return self.getExtremityFromDirection(orientation % (2 * pi))
