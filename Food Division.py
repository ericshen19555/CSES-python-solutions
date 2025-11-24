def main():
    from sys import stdin
    from itertools import accumulate
    e = stdin.readline

    n = int(e())
    a = list(map(int, e().split()))
    b = list(map(int, e().split()))
    d = [x - y for x, y in zip(a, b)]
    x = sorted(accumulate(d))[n >> 1]
    d[0] -= x
    d[-1] += x
    print(abs(x) + sum(map(abs, accumulate(d))))
main()
