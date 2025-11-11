def main():
    from sys import stdin
    from random import randrange
    e = stdin.readline
    VAL, LE, RI, SIZ, REV, MN = range(6)
    new_node = lambda v: [v, None, None, 1, 0, v]

    def size(o):
        return o[SIZ] if o else 0

    def pull(o):
        o[SIZ] = 1 + size(o[LE]) + size(o[RI])
        o[MN] = o[VAL]
        if o[LE] and o[LE][MN] < o[MN]:
            o[MN] = o[LE][MN]
        if o[RI] and o[RI][MN] < o[MN]:
            o[MN] = o[RI][MN]

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

    def query(o):
        if not o: return 0
        push(o)
        if o[VAL] == o[MN]:
            return size(o[LE])
        if o[LE] and o[LE][MN] == o[MN]:
            return query(o[LE])
        else:
            return size(o[LE]) + 1 + query(o[RI])

    n = int(e())

    rt = None
    for v in map(int, e().split()):
        rt = merge(rt, new_node(v))
    print(n)
    for s in range(n):
        a, b = split(rt, s)
        r = query(b) + 1
        b, c = split(b, r)
        print(s + 1, s + r)
        update(b)
        rt = merge(a, merge(b, c))
main()