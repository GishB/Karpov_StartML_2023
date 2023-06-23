class Vector():
    def __init__(self, coords: list = None):
        self.coords = coords

    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError(f"left and right lengths differ: {len(self.coords)} != {len(other.coords)}")
        else:
            return Vector([x + y for x, y in zip(self.coords, other.coords)])

    def __mul__(self, other):
        if isinstance(other, int):
            gate = Vector([x * other for x in self.coords])
        else:
            if len(self.coords) != len(other.coords):
                raise ValueError(f"left and right lengths differ: {len(self.coords)} != {len(other.coords)}")
            else:
                gate = sum([x * y for x, y in zip(self.coords, other.coords)])
        return gate

    def  __eq__(self, other):
        return self.coords == other.coords

    def __abs__(self):
        return sum([i**2 for i in self.coords])**0.5

    def __str__(self):
        return '{}'.format(self.coords)


print(abs(Vector([-12,5])))