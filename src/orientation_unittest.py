import unittest
from math import pi
from orientation import Orientation

class TestOrientationMethods(unittest.TestCase):

    def test_orientation_from_standard_angle(self):
        orientation = Orientation.from_angle(pi/2.0, pi/4.0)
        self.assertEqual(orientation.angleDirection, pi/2.0)
        self.assertEqual(orientation.angleAperture, pi/4.0)

    def test_orientation_from_oversized_angle(self):
        orientation = Orientation.from_angle(4*pi, 2*pi + pi/4.0)
        self.assertEqual(orientation.angleDirection, 0.)
        self.assertEqual(orientation.angleAperture, pi/4.0)

    def test_orientation_from_negative_angle(self):
        orientation = Orientation.from_angle(-pi/2.0, pi/4.0)
        self.assertEqual(orientation.angleDirection, 3 * pi / 2)
        self.assertEqual(orientation.angleAperture, pi/4.0)

    def test_orientation_from_good_string_length_1(self):
        orientationN = Orientation.from_orientation('N')
        self.assertEqual(orientationN.angleDirection, pi / 2)
        self.assertEqual(orientationN.angleAperture, pi / 2)

        orientationS = Orientation.from_orientation('S')
        self.assertEqual(orientationS.angleDirection, 3 * pi / 2)
        self.assertEqual(orientationS.angleAperture, pi / 2)

        orientationW = Orientation.from_orientation('W')
        self.assertEqual(orientationW.angleDirection, pi)
        self.assertEqual(orientationW.angleAperture, pi / 2)

        orientationE = Orientation.from_orientation('E')
        self.assertEqual(orientationE.angleDirection, 0)
        self.assertEqual(orientationE.angleAperture, pi / 2)

    def test_orientation_from_good_string_length_2(self):
        orientationNE = Orientation.from_orientation('NE')
        self.assertEqual(orientationNE.angleDirection, pi / 4)
        self.assertEqual(orientationNE.angleAperture, pi / 4)

        orientationSE = Orientation.from_orientation('SE')
        self.assertEqual(orientationSE.angleDirection, 7 * pi / 4)
        self.assertEqual(orientationSE.angleAperture, pi / 4)

        orientationSW = Orientation.from_orientation('SW')
        self.assertEqual(orientationSW.angleDirection, 5 * pi / 4)
        self.assertEqual(orientationSW.angleAperture, pi / 4)

        orientationNW = Orientation.from_orientation('NW')
        self.assertEqual(orientationNW.angleDirection, 3 * pi / 4)
        self.assertEqual(orientationNW.angleAperture, pi / 4)

    def test_orientation_from_good_string_length_multiple(self):
        orientationNNE = Orientation.from_orientation('NNE')
        self.assertEqual(orientationNNE.angleDirection, 3 * pi / 8)
        self.assertEqual(orientationNNE.angleAperture, pi / 8)

        orientationENE = Orientation.from_orientation('ENE')
        self.assertEqual(orientationENE.angleDirection, pi / 8)
        self.assertEqual(orientationENE.angleAperture, pi / 8)

        orientationNENE = Orientation.from_orientation('NENE')
        self.assertEqual(orientationNENE.angleDirection, 3 * pi / 16)
        self.assertEqual(orientationNENE.angleAperture, pi / 16)

        orientationSSW = Orientation.from_orientation('SSW')
        self.assertEqual(orientationSSW.angleDirection, 11 * pi / 8)
        self.assertEqual(orientationSSW.angleAperture, pi / 8)

    def test_orientation_from_good_string_aperture(self):
        orientationN_wide = Orientation.from_orientation('<N')
        self.assertEqual(orientationN_wide.angleDirection, pi / 2)
        self.assertEqual(orientationN_wide.angleAperture, pi)

        orientationN_narrow = Orientation.from_orientation('>N')
        self.assertEqual(orientationN_narrow.angleDirection, pi / 2)
        self.assertEqual(orientationN_narrow.angleAperture, pi / 4)

    def test_orientation_from_bad_string(self):
        self.assertRaises(ValueError,Orientation.from_orientation, 'A')
        self.assertRaises(ValueError,Orientation.from_orientation, 'WN')
        self.assertRaises(ValueError,Orientation.from_orientation, 'SNE')
        self.assertRaises(ValueError,Orientation.from_orientation, 'NE<')
        self.assertRaises(ValueError,Orientation.from_orientation, 'E>')
        self.assertRaises(ValueError,Orientation.from_orientation, '<')
        self.assertRaises(ValueError,Orientation.from_orientation, 'ENE<NE')


if __name__ == '__main__':
    unittest.main()