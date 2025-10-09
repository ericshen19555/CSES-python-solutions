class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other: "Vector") -> bool:
        return self.x == other.x and self.y == other.y

    def __pos__(self) -> "Vector":
        return self

    def __neg__(self) -> "Vector":
        return Vector(-self.x, -self.y)

    def __add__(self, other: "Vector") -> "Vector":
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

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"


def inter1d(a, b, c):
    if a > b: a, b = b, a
    return max(a, c) <= min(b, c)


def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    l = [Vector(*map(int, e().split())) for _ in range(n)]

    ans = []
    for _ in range(q):
        p = Vector(*map(int, e().split()))
        bound = inside = False
        for i in range(n):
            a, b = l[i - 1], l[i]
            if a.x > b.x: a, b = b, a
            crs = a.cross(b, p)
            if crs == 0 and inter1d(a.x, b.x, p.x) and inter1d(a.y, b.y, p.y):
                bound = True
                break
            if a.x <= p.x < b.x and crs > 0:
                inside = not inside
        ans.append("BOUNDARY" if bound else "INSIDE" if inside else "OUTSIDE")
    print("\n".join(ans))
main()