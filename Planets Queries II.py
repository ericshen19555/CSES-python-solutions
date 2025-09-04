def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    l = [int(v) - 1 for v in e().split()]

    tag = [0] * n
    counter = 0
    G = [[] for _ in range(n)]
    cycles = []
    in_cycle = [False] * n
    for s, v in enumerate(tag):
        if v: continue
        counter += 1
        i = s
        while not tag[i]:
            tag[i] = counter
            i = l[i]
        c = i
        if tag[c] == counter:
            size = 1
            pi, i = c, l[c]
            while i != c:
                size += 1
                G[i].append(pi)
                in_cycle[i] = True
                pi, i = i, l[i]
            G[i].append(pi)
            in_cycle[i] = True
            cycles.append((c, size))
        pi, i = s, l[s]
        while i != c:
            G[i].append(pi)
            pi, i = i, l[i]
        G[i].append(pi)

    qs = [[] for _ in range(n)]
    for qi in range(q):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        qs[a].append((b, qi))

    for i in range(n):
        G[i] = iter(G[i])
        qs[i] = iter(qs[i])

    dep = [-1] * n
    ans = [-1] * q
    for c, size in cycles:
        stk = [c]
        dep[c] = 0
        while stk:
            i = stk[-1]
            if in_cycle[i]:
                top = i
            for j in G[i]:
                dep[j] = len(stk)
                stk.append(j)
                break
            else:
                for j, qi in qs[i]:
                    if dep[j] == -1: continue
                    if in_cycle[j]:
                        ans[qi] = dep[i] - dep[top] + (dep[top] - dep[j]) % size
                    else:
                        ans[qi] = dep[i] - dep[j]
                stk.pop()
                if not in_cycle[i]:
                    dep[i] = -1
        dep[c] = -1
        i = l[c]
        while i != c:
            dep[i] = -1
            i = l[i]

    print("\n".join(map(str, ans)))
main()