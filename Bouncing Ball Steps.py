from sys import stdin
from math import lcm

def main():
    e = stdin.readline

    def solve():
        m, n, k = map(int, e().split())
        m, n = m - 1, n - 1
        mq, mr = divmod(k, m)
        nq, nr = divmod(k, n)
        print((m - mr if mq & 1 else mr) + 1, (n - nr if nq & 1 else nr) + 1, mq + nq - k // lcm(m, n))

    for _ in range(int(e())):
        solve()
main()
