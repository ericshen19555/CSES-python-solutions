def main():
    from sys import stdin
    from bisect import bisect_left
    e = stdin.readline

    def check(x):
        return sum(x // v for v in l) >= k

    n, k = map(int, e().split())
    l = list(map(int, e().split()))
    print(bisect_left(
        range(max(l) * ((k - 1) // n + 1)),
        True,
        key=check
    ))
main()