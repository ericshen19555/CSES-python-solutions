def main():
    from sys import stdin
    e = stdin.readline
    r = 1 << 20
    m = r << 1
    shift = r + m

    n = int(e())
    q = []
    for _ in range(n):
        a, b, c, d = map(int, e().split())
        q.append((a << 1 | 0, shift + b, shift + d))
        q.append((c << 1 | 1, shift + b, shift + d))
    q.sort()

    def merge(i, r):
        if tag[i]: zkw[i] = r
        elif r > 1: zkw[i] = zkw[i << 1] + zkw[i << 1 | 1]
        else: zkw[i] = 0

    def add(s, t, v):
        r = 1
        while s < t:
            if s & 1:
                tag[s] += v
                merge(s, r)
                s += 1
            if t & 1:
                t -= 1
                tag[t] += v
                merge(t, r)
            s >>= 1; t >>= 1
            v <<= 1; r <<= 1

    def pull(i):
        r = 1
        while i > 1:
            i >>= 1; r <<= 1
            merge(i, r)

    ans = px = 0
    tag = [0] * (m << 1)
    zkw = [0] * (m << 1)
    for x, s, t in q:
        x, v = x >> 1, -1 if x & 1 else 1
        ans += zkw[1] * (x - px)
        add(s, t, v)
        pull(s), pull(t - 1)
        px = x
    print(ans)
main()
