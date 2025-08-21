def main():
    from sys import stdin
    from bisect import bisect_left
    e = stdin.readline

    def check(x):
        cur = 0
        r = k
        for v in l:
            cur += v
            if cur > x:
                cur = v
                r -= 1
                if not r:
                    return False
        return True

    n, k = map(int, e().split())
    l = list(map(int, e().split()))
    print(bisect_left(
        range(sum(l)),
        True,
        lo=max(l),
        key=check
    ))
main()