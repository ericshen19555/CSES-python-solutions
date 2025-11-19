# credit: dreamoon

def main():
    from sys import stdin
    inf = 10**10
    e = stdin.readline

    n = int(e())
    l = sorted(map(int, e().split()))
    for i in range(n - 1):
        l[i] = l[i + 1] - l[i]
    l[-1] = inf

    ds = []
    stk = [inf]
    pp, p = inf + 1, inf + 2
    for v in l:
        while pp >= p <= v:
            ds.append(p)
            v += pp - p
            p = stk.pop()
            pp = stk.pop()
        stk.append(pp)
        pp, p = p, v
    ds.sort()

    cur = 0
    ans = []
    for d in ds:
        cur += d
        ans.append(cur)
    print(*ans)
main()