import numpy as np


class City:
    def __init__(self, posNum, x, y):
        self.posNum = posNum
        self.x = x
        self.y = y

# this is used absolutely nowhere
    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance

    def __repr__(self):
        return "City" + str(self.posNum) + "_(" + str(self.x) + "," + str(self.y) + ")"
