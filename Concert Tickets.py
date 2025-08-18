def main():
    from sys import stdin
    from bisect import bisect_right
    e = stdin.readline

    n, m = map(int, e().split())
    s = int(n ** 0.5)
    l = sorted(map(int, e().split()))
    sl = []
    for i in range(0, n, s):
        sl.append(l[i:i+s])
    if i + s < n:
        sl.append(l[i+s:])
    mn = [b[0] for b in sl]
    ans = []
    for v in map(int, e().split()):
        i = bisect_right(mn, v) - 1
        if i == -1:
            ans.append(-1)
            continue
        b = sl[i]
        j = bisect_right(b, v) - 1
        if j == -1:
            ans.append(-1)
            continue
        ans.append(b[j])
        del b[j]
        if not b:
            del sl[i]
            del mn[i]
        elif j == 0:
            mn[i] = b[0]
    print("\n".join(map(str, ans)))
main()