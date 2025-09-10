def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    l = list(map(int, e().split()))
    qs = [[] for _ in range(n)]
    for i in range(q):
        s, t = map(int, e().split())
        qs[t-1].append((s-1, i))

    last = dict.fromkeys(l, -1)
    bit = [0] * (n + 1)
    ans = [0] * q
    cur = 0
    for i in range(n):
        v = l[i]
        if ~(pi := last[v]):
            cur -= 1
            x = pi + 1
            while x <= n:
                bit[x] -= 1
                x += x & -x
        cur += 1
        last[v] = i
        x = i + 1
        while x <= n:
            bit[x] += 1
            x += x & -x
        for s, ai in qs[i]:
            res = cur
            while s:
                res -= bit[s]
                s &= s-1
            ans[ai] = res
    print("\n".join(map(str, ans)))
main()