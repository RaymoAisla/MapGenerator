import unittest
import random
from math import pi
from map import Map

class TestMapMethods(unittest.TestCase):

    def test_getExtremityFromDirection(self):
        map = Map(40, 1)

        coord1 = map.getExtremityFromDirection(0)
        self.assertEqual(coord1, [map.length - 1, (map.length - 1)/2])

        coord2 = map.getExtremityFromDirection(pi/4)
        self.assertEqual(coord2, [map.length - 1, 0])

        coord3 = map.getExtremityFromDirection(pi/2)
        self.assertEqual(coord3, [(map.length - 1)/2, 0])

        coord4 = map.getExtremityFromDirection(3*pi/4)
        self.assertEqual(coord4, [0, 0])

        coord5 = map.getExtremityFromDirection(3*pi)
        self.assertEqual(coord5, [0, (map.length - 1)/2])


if __name__ == '__main__':
    unittest.main()