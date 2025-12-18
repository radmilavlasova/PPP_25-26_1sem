if __name__ == "__main__":
    pass 
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def vertices(self):
        pass
def distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)
class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.points = [(x1, y1), (x2, y2), (x3, y3)]

    def perimeter(self):
        p = 0
        for i in range(3):
            x1, y1 = self.points[i]
            x2, y2 = self.points[(i + 1) % 3]
            p += distance(x1, y1, x2, y2)
        return p

    def area(self):
        (x1, y1), (x2, y2), (x3, y3) = self.points
        return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2

    def vertices(self):
        return 3
class Rectangle(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.width = abs(x2 - x1)
        self.height = abs(y2 - y1)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def vertices(self):
        return 4
class Circle(Shape):
    def __init__(self, x, y, r):
        if r <= 0:
            raise ValueError("Radius must be positive")
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def vertices(self):
        return 0
class Polygon(Shape):
    def __init__(self, x, y, r, n):
        if n < 3:
            raise ValueError("Polygon must have at least 3 vertices")
        self.r = r
        self.n = n

    def area(self):
        return (self.n * self.r ** 2 * math.sin(2 * math.pi / self.n)) / 2

    def perimeter(self):
        side = 2 * self.r * math.sin(math.pi / self.n)
        return self.n * side

    def vertices(self):
        return self.n
def parse_shape(line: str):
    parts = line.split()
    shape_type = parts[0].lower()

    try:
        nums = list(map(float, parts[1:]))

        if shape_type == "triangle":
            return Triangle(*nums)
        elif shape_type == "rectangle":
            return Rectangle(*nums)
        elif shape_type == "circle":
            return Circle(*nums)
        elif shape_type == "polygon":
            x, y, r, n = nums
            return Polygon(x, y, r, int(n))
        else:
            raise ValueError("Unknown shape type")

    except Exception as e:
        raise ValueError(f"Invalid input: {e}")
def main():
    shapes = []

    print("Enter shapes (empty line to finish):")

    while True:
        line = input()
        if not line.strip():
            break
        try:
            shape = parse_shape(line)
            shapes.append(shape)
        except ValueError as e:
            print(f"Error: {e}")

    if not shapes:
        print("No shapes entered.")
        return

    command = input("Enter command (area / perimeter / vertices): ").strip().lower()

    if command == "area":
        total = sum(s.area() for s in shapes)
        print(f"Total area: {total:.2f}")

    elif command == "perimeter":
        total = sum(s.perimeter() for s in shapes)
        print(f"Total perimeter: {total:.2f}")

    elif command == "vertices":
        total = sum(s.vertices() for s in shapes)
        print(f"Total vertices: {total}")

    else:
        print("Unknown command")
if __name__ == "__main__":
    main()

