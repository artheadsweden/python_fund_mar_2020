class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f"Point({self._x}, {self._y})"

    def __str__(self):
        return f"Point object with x = {self._x} and y = {self._y}"

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y)


def main():
    p1 = Point(10, 45)
    p2 = Point(10, 46)

    print(repr(p1))
    result = str(p2)
    print(result)
    if p1 == p2:
        print("They are the same")
    else:
        print("They are not the same")

    p3 = p1 + p2
    print(p3)


if __name__ == '__main__':
    main()
