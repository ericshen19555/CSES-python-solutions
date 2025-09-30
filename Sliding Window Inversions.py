def main():
    from sys import stdin
    e = stdin.readline

    def add(i, v):
        i += 1
        while i <= m:
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

    n, k = map(int, e().split())
    l = list(map(int, e().split()))
    mp = {v: i for i, v in enumerate(sorted(set(l)))}
    m = len(mp)
    bit = [0] * (m + 1)

    ans = []
    cur = 0
    for i in range(n):
        v = mp[l[i]]
        cur += query(v + 1, m)
        add(v, 1)
        if i >= k:
            p = mp[l[i - k]]
            add(p, -1)
            cur -= query(0, p)
        if i >= k - 1:
            ans.append(cur)
    print(*ans)
main()