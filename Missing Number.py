def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    s = sum(map(int, e().split()))
    print((n * (n + 1) >> 1) - s)
main()