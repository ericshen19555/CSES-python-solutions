from sys import stdin
from math import gcd

def main():
    e = stdin.readline

    def solve():
        m, n = map(int, e().split())
        m, n = m - 1, n - 1
        g = gcd(m, n)
        print(m * n // g << 1, m * n // g - (m // g - 1) * (n // g - 1) // 2 + 1)

    for _ in range(int(e())):
        solve()
main()
