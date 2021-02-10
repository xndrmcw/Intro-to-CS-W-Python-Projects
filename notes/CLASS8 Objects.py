class Coordinate (object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_distance_sq = (self.x - other.x) ** 2
        y_distance_sq = (self.y - other.y) ** 2
        return (x_distance_sq + y_distance_sq) ** 0.5

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"


point = Coordinate(3, 4)
origin = Coordinate(0, 0)

# BOTH ARE EQUIVALENT
print(point.distance(origin))
print(Coordinate.distance(point, origin))
print(point)

class Fraction(object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        top = self.num * other.denom + self.denom * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)


object1 = Fraction(12, 16)
object2 = Fraction(4, 16)
print(object1.__add__(object2))
