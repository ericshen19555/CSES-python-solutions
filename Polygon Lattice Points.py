def main():
    from sys import stdin
    from math import gcd
    e = stdin.readline

    # Pick: A = inside + edge/2 - 1

    n = int(e())
    area = edge = 0
    ox, oy = px, py = tuple(map(int, e().split()))
    for _ in range(n - 1):
        x, y = map(int, e().split())
        area += px * y - py * x
        edge += gcd(x - px, y - py)
        px, py = x, y
    area += x * oy - y * ox
    edge += gcd(x - ox, y - oy)
    area = abs(area)
    print(area + 2 - edge >> 1, edge)
main()