def main():
    from sys import stdin
    e = stdin.readline

    def merge(pos):
        sm[pos] = sm[pos << 1] + sm[pos << 1 | 1]
        zkw[pos] = max(zkw[pos << 1], sm[pos << 1] + zkw[pos << 1 | 1])

    n, q = map(int, e().split())
    sm = [0] * n
    sm += map(int, e().split())
    zkw = sm.copy()
    for i in range(n-1, 0, -1):
        merge(i)

    ans = []
    for _ in range(q):
        o, a, b = map(int, e().split())
        if o == 1:
            i, v = a - 1 + n, b
            sm[i] = zkw[i] = v
            while i > 1:
                i >>= 1
                merge(i)
        else:
            s, t = a - 1 + n, b + n
            le, ri = 0, 0
            pre = 0
            while s < t:
                if s & 1:
                    le = max(le, pre + zkw[s])
                    pre += sm[s]
                    s += 1
                if t & 1:
                    t -= 1
                    ri = max(sm[t] + ri, zkw[t])
                s >>= 1
                t >>= 1
            ans.append(max(le, pre + ri))
    print(*ans)
main()
