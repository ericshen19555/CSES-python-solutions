def main():
    from sys import stdin
    e = stdin.readline
    VAL, LE, RI = range(3)
    new_node = lambda: [0, None, None]

    def pull(node):
        node[VAL] = node[LE][VAL] + node[RI][VAL]

    def build(node, s, t):
        if s + 1 == t:
            node[VAL] = l[s]
        else:
            mid = s + t >> 1
            node[LE] = build(new_node(), s, mid)
            node[RI] = build(new_node(), mid, t)
            pull(node)
        return node

    def modify(node, s, t, idx, val):
        node = node.copy()
        if s + 1 == t:
            node[VAL] = val
        else:
            mid = s + t >> 1
            if idx < mid:
                node[LE] = modify(node[LE], s, mid, idx, val)
            else:
                node[RI] = modify(node[RI], mid, t, idx, val)
            pull(node)
        return node

    def query(node, s, t, qs, qt):
        if qt <= s or  t <= qs:
            return 0
        if qs <= s and t <= qt:
            return node[VAL]
        mid = s + t >> 1
        res = 0
        res += query(node[LE], s, mid, qs, qt)
        res += query(node[RI], mid, t, qs, qt)
        return res

    n, q = map(int, e().split())
    l = list(map(int, e().split()))
    roots = [new_node()]
    build(roots[0], 0, n)

    ans = []
    for _ in range(q):
        o, *oo = map(int, e().split())
        if o == 1:
            ver, idx, val = oo
            ver, idx = ver-1, idx-1
            roots[ver] = modify(roots[ver], 0, n, idx, val)
        elif o == 2:
            ver, s, t = oo
            ver, s = ver-1, s-1
            ans.append(query(roots[ver], 0, n, s, t))
        else:
            ver = oo[0] - 1
            roots.append(roots[ver])
    print("\n".join(map(str, ans)))
main()