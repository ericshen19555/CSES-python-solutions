def main():
    from sys import stdin
    e = stdin.readline

    def merge(i, h=0):
        if tag[i] < 0:
            zkw[i] = -tag[i] << h
        else:
            zkw[i] = zkw[i << 1] + zkw[i << 1 | 1] + (tag[i] << h)

    def update(i, v, h):
        if v > 0:
            zkw[i] += v << h
            if h:
                tag[i] += v if tag[i] >= 0 else -v
        elif v < 0:
            zkw[i] = -v << h
            if h:
                tag[i] = v

    def push(i):
        for h in range(lg, 0, -1):
            j = i >> h
            if not tag[j]: continue
            update(j << 1 | 0, tag[j], h - 1)
            update(j << 1 | 1, tag[j], h - 1)
            tag[j] = 0

    def pull(i):
        h = 0
        while i > 1:
            i >>= 1
            h += 1
            merge(i, h)

    def modify(s, t, v):
        s, t = s + n, t + n
        push(s), push(t - 1)
        ss, tt = s, t
        h = 0
        while s < t:
            if s & 1:
                update(s, v, h)
                s += 1
            if t & 1:
                t -= 1
                update(t, v, h)
            s >>= 1
            t >>= 1
            h += 1
        pull(ss), pull(tt - 1)

    def query(s, t):
        s, t = s + n, t + n
        push(s), push(t - 1)
        res = 0
        while s < t:
            if s & 1:
                res += zkw[s]
                s += 1
            if t & 1:
                t -= 1
                res += zkw[t]
            s >>= 1
            t >>= 1
        return res

    n, q = map(int, e().split())
    lg = n.bit_length()
    zkw = [0] * n
    tag = [0] * n
    zkw += map(int, e().split())
    for i in range(n-1, 0, -1):
        merge(i)

    ans = []
    for _ in range(q):
        o, s, t, *v = map(int, e().split())
        s -= 1
        if o == 1:
            modify(s, t, v[0])
        elif o == 2:
            modify(s, t, -v[0])
        else:
            ans.append(query(s, t))
    print("\n".join(map(str, ans)))
main()