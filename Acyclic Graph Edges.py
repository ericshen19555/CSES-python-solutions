def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    for _ in range(m):
        a, b = map(int, e().split())
        if a > b: a, b = b, a
        print(a, b)
main()