def main():
    from sys import stdin
    from operator import itemgetter
    e = stdin.readline

    n = int(e())
    l = [(*map(int, e().split()), i) for i in range(n)]
    l.sort(key=lambda x: (x[0], -x[1]))
    mp = {v: i for i, v in enumerate(sorted(set(map(itemgetter(1), l))))}
    m = len(mp)
    bit = [0] * (n + 1)
    ans = [0] * n
    for a, b, i in reversed(l):
        b = mp[b] + 1
        res = 0
        x = b
        while x:
            res += bit[x]
            x &= x - 1
        ans[i] = res
        x = b
        while x <= n:
            bit[x] += 1
            x += x & -x
    print(*ans)
    bit = [0] * (n + 1)
    l.sort(key=lambda x: (x[0], -x[1]))
    for a, b, i in l:
        b = m - mp[b]
        res = 0
        x = b
        while x:
            res += bit[x]
            x &= x - 1
        ans[i] = res
        x = b
        while x <= n:
            bit[x] += 1
            x += x & -x
    print(*ans)
main()