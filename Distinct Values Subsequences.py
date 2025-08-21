def main():
    from sys import stdin
    from functools import reduce
    e = stdin.readline
    mod = 10**9 + 7
    mul = lambda a, b: a * b % mod

    e()
    c = {}
    for v in map(int, e().split()):
        c[v] = c.get(v, 1) + 1
    print((reduce(mul, c.values()) - 1) % mod)
main()