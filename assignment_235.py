

"""
class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj._protectedVar = 34
print(obj._protectedVar)
"""

# Created a class for a donor
# then an attribute for their donation
# is protected
class Donor:
    def __init__(self):
        self._donoVar = 0

# Creating a new object named Jim
# and assigning a value to the donation. 
Jim = Donor()
Jim._donoVar = 1000
print(Jim._donoVar)


"""
class Protected:
    def __init__(self):
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar =private

obj = Protected()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
"""
# creating a protected class of fundraiser
# then we assign a zone. 
class Fundraiser:
    def __init__(self):
        self.__zone = "Bay Area"

    def getZone(self):
        print(self.__zone)

    def setZone(self, private):
        self.__zone =private

Lisa = Fundraiser()
Lisa.getZone()
Lisa.setZone("Los Angeles")
Lisa.getZone()


