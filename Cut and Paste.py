def main():
    from sys import stdin
    from random import randrange
    e = stdin.readline
    VAL, LE, RI, SIZ = range(4)
    new_node = lambda v: [v, None, None, 1]

    def size(o):
        return o[SIZ] if o else 0

    def pull(o):
        o[SIZ] = 1 + size(o[LE]) + size(o[RI])

    def merge(a, b):
        if not a or not b:
            return a if a else b
        sa, sb = size(a), size(b)
        if randrange(0, sa + sb) < sa:
            a[RI] = merge(a[RI], b)
            o = a
        else:
            b[LE] = merge(a, b[LE])
            o = b
        pull(o)
        return o

    def split(o, k):
        if not o: return o, o
        if (ls := size(o[LE])) < k:
            a = o
            o[RI], b = split(o[RI], k - ls - 1)
        else:
            b = o
            a, o[LE] = split(o[LE], k)
        pull(o)
        return a, b

    def dfs(o):
        if not o: return
        dfs(o[LE])
        ans.append(o[VAL])
        dfs(o[RI])

    n, q = map(int, e().split())
    s = e()

    rt = None
    for i in range(n):
        rt = merge(rt, new_node(s[i]))
    for _ in range(q):
        s, t = map(int, e().split())
        s -= 1
        a, b = split(rt, s)
        b, c = split(b, t - s)
        rt = merge(a, merge(c, b))
    ans = []
    dfs(rt)
    print("".join(ans))
main()