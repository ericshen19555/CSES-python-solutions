def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    le, ri = [0] * n, [0] * n
    for i in range(n):
        le[i], ri[i] = map(int, e().split())
    l = sorted(range(n), key=lambda i: (le[i], -ri[i]))
    lo = float("INF")
    ans = [0] * n
    for i in reversed(l):
        b = ri[i]
        ans[i] = 1 if lo <= b else 0
        if b < lo: lo = b
    print(*ans)
    hi = 0
    for i in l:
        b = ri[i]
        ans[i] = 1 if b <= hi else 0
        if b > hi: hi = b
    print(*ans)
main()