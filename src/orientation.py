from enum import Enum
from math import pi

def getAngleFromOrientation(orientationString):
    angleDivision = 2
    angleMiddle = {'num':0, 'den':1}
    if len(orientationString) == 1:
        firstChar = orientationString[-1]
        if firstChar.upper() == 'E':
            angleMiddle['num'] = 0
            angleMiddle['den'] = 1
        elif firstChar.upper() == 'W':
            angleMiddle['num'] = 1
            angleMiddle['den'] = 1   
        elif firstChar.upper() == 'S':
            angleMiddle['num'] = 3
            angleMiddle['den'] = 2
        elif firstChar.upper() == 'N':
            angleMiddle['num'] = 1
            angleMiddle['den'] = 2
        else:
            raise ValueError('Bad input orientation')
    elif len(orientationString) >= 2 and orientationString[-2] != '>' and orientationString[-2] != '<':
        firstChar = orientationString[-1]
        secondChar = orientationString[-2]
        firstCharTurn = -1
        secondCharTurn = 1
        isMiddlePointComputationEnded = False 
        if firstChar.upper() == 'E' and secondChar.upper() == 'N':
            angleMiddle['num'] = 1
            angleMiddle['den'] = 4
            angleDivision = 4
            firstCharTurn = -1
            secondCharTurn = 1
        elif firstChar.upper() == 'E' and secondChar.upper() == 'S':
            angleMiddle['num'] = 7
            angleMiddle['den'] = 4
            angleDivision = 4
            firstCharTurn = 1
            secondCharTurn = -1
        elif firstChar.upper() == 'W' and secondChar.upper() == 'N':
            angleMiddle['num'] = 3
            angleMiddle['den'] = 4
            angleDivision = 4
            firstCharTurn = 1
            secondCharTurn = -1
        elif firstChar.upper() == 'W' and secondChar.upper() == 'S':
            angleMiddle['num'] = 5
            angleMiddle['den'] = 4
            angleDivision = 4
            firstCharTurn = -1
            secondCharTurn = 1
        else:
            raise ValueError('Bad input orientation')
        for currentChar in reversed(orientationString[:-2]):
            if isMiddlePointComputationEnded == False and currentChar == firstChar:
                angleDivision = angleDivision * 2
                angleMiddle['num'] = angleMiddle['num'] * 2 + firstCharTurn
                angleMiddle['den'] = angleMiddle['den'] * 2
            elif isMiddlePointComputationEnded == False and currentChar == secondChar:
                angleDivision = angleDivision * 2
                angleMiddle['num'] = angleMiddle['num'] * 2 + secondCharTurn
                angleMiddle['den'] = angleMiddle['den'] * 2
            elif currentChar == '>':
                angleDivision = angleDivision * 2
                isMiddlePointComputationEnded = True
            elif currentChar == '<':
                angleDivision = max(angleDivision / 2, 0.5)
                isMiddlePointComputationEnded = True
            else:
                raise ValueError('Bad input orientation')
    elif len(orientationString) >= 2 and (orientationString[-2] == '>' or orientationString[-2] == '<'):
        firstChar = orientationString[-1]
        if firstChar.upper() == 'E':
            angleMiddle['num'] = 0
            angleMiddle['den'] = 1
        elif firstChar.upper() == 'W':
            angleMiddle['num'] = 1
            angleMiddle['den'] = 1   
        elif firstChar.upper() == 'S':
            angleMiddle['num'] = 3
            angleMiddle['den'] = 2
        elif firstChar.upper() == 'N':
            angleMiddle['num'] = 1
            angleMiddle['den'] = 2
        else:
            raise ValueError('Bad input orientation')
        for currentChar in reversed(orientationString[:-1]):
            if currentChar == '>':
                angleDivision = angleDivision * 2
            elif currentChar == '<':
                angleDivision = max(angleDivision / 2, 0.5)
            else:
                raise ValueError('Bad input orientation')
    else:
        raise ValueError('Bad input orientation')
    return {'angleDirection':angleMiddle, 'angleAperture':angleDivision}


class Orientation:
    def __init__(self, angleDirection, angleAperture):
        self.angleDirection = angleDirection % (2 * pi)
        self.angleAperture = angleAperture % (2 * pi)

    @classmethod
    def from_angle(cls, direction, aperture):
        return cls(direction, aperture)

    @classmethod
    def from_orientation(cls, orientationString):
        angleProperties = getAngleFromOrientation(orientationString)
        return cls(pi*angleProperties['angleDirection']['num']/angleProperties['angleDirection']['den'], pi/angleProperties['angleAperture'])
                
