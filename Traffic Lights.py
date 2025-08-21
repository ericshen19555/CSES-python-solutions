def main():
    from sys import stdin
    from bisect import bisect_left
    e = stdin.readline

    m, n = map(int, e().split())
    l = list(map(int, e().split()))
    p = sorted(l) + [m]
    pv = 0
    val = [0] * (n + 1)
    xorll = [0] * (n + 1)
    for i, v in enumerate(p):
        val[i] = v - pv
        pv = v
    cur = max(val)
    ans = []
    for v in reversed(l):
        ans.append(cur)
        i = bisect_left(p, v)
        i, j = xorll[i] ^ i, xorll[i + 1] ^ (i + 1)
        xorll[i] = xorll[j] = i ^ j
        val[i] = val[j] = val[i] + val[j]
        cur = max(cur, val[i])
    print(" ".join(map(str, reversed(ans))))
main()