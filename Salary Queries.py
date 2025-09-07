def main():
    from sys import stdin
    e = stdin.readline

    def add(i, v):
        while i < m:
            bit[i] += v
            i += i & -i

    def query(s, t):
        res = 0
        while t > s:
            res += bit[t]
            t &= t-1
        while s > t:
            res -= bit[s]
            s &= s-1
        return res

    n, q = map(int, e().split())
    l = list(map(int, e().split()))
    sl = l.copy()
    qs = [e() for _ in range(q)]
    for o in qs:
        if o.startswith("!"):
            sl.append(int(o.rsplit(maxsplit=1)[1]))
        else:
            s, t = map(int, o.split()[1:])
            sl.append(s - 1)
            sl.append(t)
    mp = {v: i for i, v in enumerate(sorted(set(sl)), 1)}
    m = len(mp) + 1
    bit = [0] * m
    for i in range(n):
        l[i] = mp[l[i]]
        add(l[i], 1)
    ans = []
    for o in qs:
        if o.startswith("!"):
            i, v = map(int, o.split()[1:])
            i -= 1
            add(l[i], -1)
            l[i] = mp[v]
            add(l[i], 1)
        else:
            s, t = map(int, o.split()[1:])
            ans.append(query(mp[s - 1], mp[t]))
    print("\n".join(map(str, ans)))
main()
