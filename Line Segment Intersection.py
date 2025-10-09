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


def banana(p1: Vector, p2: Vector, p3: Vector, p4: Vector) -> bool:
    def inter1d(a, b, c, d):
        if a > b: a, b = b, a
        if c > d: c, d = d, c
        return max(a, c) <= min(b, d)

    return (inter1d(p1.x, p2.x, p3.x, p4.x) and inter1d(p1.y, p2.y, p3.y, p4.y)
            and p1.cross(p2, p3) * p1.cross(p2, p4) <= 0
            and p3.cross(p4, p1) * p3.cross(p4, p2) <= 0)


def main():
    from sys import stdin
    e = stdin.readline

    ans = []
    for _ in range(int(e())):
        x1, y1, x2, y2, x3, y3, x4, y4 = map(int, e().split())
        p1, p2, p3, p4 = Vector(x1, y1), Vector(x2, y2), Vector(x3, y3), Vector(x4, y4)
        ans.append("YES" if banana(p1, p2, p3, p4) else "NO")
    print("\n".join(ans))
main()