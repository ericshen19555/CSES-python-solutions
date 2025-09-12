def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    G = [[] for _ in range(n)]
    for i, p in enumerate(map(int, e().split()), 1):
        p -= 1
        G[p].append(i)
    for i, it in enumerate(G):
        G[i] = iter(it)

    qs = [[] for _ in range(n)]
    ans = [0] * q
    for qi in range(q):
        i, k = map(int, e().split())
        i -= 1
        if i == 0:
            ans[qi] = -1
        else:
            ans[qi] = k
            qs[i].append(qi)

    stk = [0]
    while stk:
        i = stk[-1]
        for j in G[i]:
            for ai in qs[j]:
                k = ans[ai]
                ans[ai] = -1 if k > len(stk) else stk[-k] + 1
            stk.append(j)
            break
        else:
            stk.pop()
    print("\n".join(map(str, ans)))
main()