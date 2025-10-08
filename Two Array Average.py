def main():
    from sys import stdin
    from itertools import accumulate
    e = stdin.readline
    m = 10**6

    def check(x):
        mx, i = max((v, i) for i, v in enumerate(accumulate(v - x for v in a), 1))
        for j, p in enumerate(accumulate(v - x for v in b), 1):
            if mx >= -p:
                return i, j

    n = int(e())
    a = [int(v) * m for v in e().split()]
    b = [int(v) * m for v in e().split()]

    s, t = 1, max(max(a), max(b))
    ans = (1, 1)
    while s < t:
        mid = s + t >> 1
        if ret := check(mid):
            s = mid + 1
            ans = ret
        else:
            t = mid
    print(*ans)
main()