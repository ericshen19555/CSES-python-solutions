def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    G = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        G[b].append(a)
    pa = [-1] * n
    q = [0]
    for i in q:
        p = pa[i]
        for j in G[i]:
            if j == p: continue
            pa[j] = i
            q.append(j)
    ans = 0
    used = [False] * n
    for i in reversed(q):
        if not i: continue
        if used[i]: continue
        p = pa[i]
        if used[p]: continue
        ans += 1
        used[p] = True
    print(ans)
main()