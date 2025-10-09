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

    n = int(e())
    ans = 0
    first = pre = Vector(*map(int, e().split()))
    for _ in range(n - 1):
        cur = Vector(*map(int, e().split()))
        ans += pre ^ cur
        pre = cur
    ans += cur ^ first
    print(abs(ans))
main()