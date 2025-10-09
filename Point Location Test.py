class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: "Vector"):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector") -> int:
        return self.x * other.x + self.y * other.y

    def __xor__(self, other: "Vector") -> int:
        return self.x * other.y - self.y * other.x

    def cross(self, a: "Vector", b: "Vector") -> int:
        o = self
        return (a - o) ^ (b - o)


def main():
    from sys import stdin
    e = stdin.readline

    ans = []
    for _ in range(int(e())):
        x1, y1, x2, y2, x3, y3 = map(int, e().split())
        p1, p2, p3 = Vector(x1, y1), Vector(x2, y2), Vector(x3, y3)
        x = p1.cross(p2, p3)
        ans.append("TOUCH" if x == 0 else "LEFT" if x > 0 else "RIGHT")
    print("\n".join(ans))
main()