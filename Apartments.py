def main():
    from sys import stdin
    inf = float("INF")
    e = stdin.readline

    n, m, k = map(int, e().split())
    a = sorted(map(int, e().split()))
    b = sorted(map(int, e().split()))
    it = iter(b)
    j = next(it)
    ans = 0
    for i in a:
        while j < i - k:
            j = next(it, inf)
        if j is inf: break
        if j <= i + k:
            ans += 1
            j = next(it, inf)
            if j is inf: break
    print(ans)
main()