def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    s, t = [1 << 62] * n, [1 << 62] * n
    for i in range(n):
        s[i], t[i] = map(int, e().split())
    s.sort(), t.sort()
    s, t = iter(s), iter(t)
    i, j = next(s), next(t)
    ans = cur = 0
    while i is not None and j is not None:
        if i < j:
            i = next(s, None)
            cur += 1
            if cur > ans: ans = cur
        else:
            j = next(t, None)
            cur -= 1
    print(ans)
main()