def main():
    from sys import stdin
    from random import randrange
    e = stdin.readline
    VAL, LE, RI, SIZ, REV = range(5)
    new_node = lambda v: [v, None, None, 1, 0]

    def size(o):
        return o[SIZ] if o else 0

    def pull(o):
        o[SIZ] = 1 + size(o[LE]) + size(o[RI])

    def update(o):
        if not o: return
        o[LE], o[RI] = o[RI], o[LE]
        o[REV] ^= 1

    def push(o):
        if not o[REV]: return
        o[REV] = 0
        update(o[LE])
        update(o[RI])

    def merge(a, b):
        if not a or not b:
            return a if a else b
        sa, sb = size(a), size(b)
        if randrange(0, sa + sb) < sa:
            push(o := a)
            a[RI] = merge(a[RI], b)
        else:
            push(o := b)
            b[LE] = merge(a, b[LE])
        pull(o)
        return o

    def split(o, k):
        if not o: return o, o
        push(o)
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
        push(o)
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
        update(b)
        rt = merge(a, merge(b, c))
    ans = []
    dfs(rt)
    print("".join(ans))
main()