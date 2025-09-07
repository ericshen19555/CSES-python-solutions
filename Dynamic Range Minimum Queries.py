def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    zkw = [0] * n
    zkw += map(int, e().split())
    for i in range(n-1, 0, -1):
        zkw[i] = min(zkw[i << 1], zkw[i << 1 | 1])

    ans = []
    for _ in range(q):
        o, a, b = map(int, e().split())
        if o == 1:
            i, v = a - 1, b
            i += n
            zkw[i] = v
            while i > 1:
                i >>= 1
                zkw[i] = min(zkw[i << 1], zkw[i << 1 | 1])
        else:
            s, t = a - 1, b
            s, t = s + n, t + n
            res = float("INF")
            while s < t:
                if s & 1:
                    res = min(res, zkw[s])
                    s += 1
                if t & 1:
                    t -= 1
                    res = min(res, zkw[t])
                s >>= 1
                t >>= 1
            ans.append(res)
    print("\n".join(map(str, ans)))
main()