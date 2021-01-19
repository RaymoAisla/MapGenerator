class Point:
    def __init__(self):
        self.attributes = {}

    def addAttribute(self, attribute, attributeName):
        self.attributes[attributeName] = attribute

    def removeAttribute(self, attributeName):
        self.attributes.pop(attributeName)

    def getAttribute(self, attributeName):
        return self.attributes[attributeName]