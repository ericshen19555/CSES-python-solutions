import sys
from io import StringIO

testcase = """\
4 4
1 2
2 3
3 4
1 4
"""

sys.stdin = StringIO(testcase)

def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(n):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        G[b].append(a)

main()