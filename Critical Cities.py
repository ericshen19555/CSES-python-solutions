# credit: sk_coder007 https://cses.fi/problemset/hack/1703/entry/11872565/

def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        G[a].append(b)

    dep = [0] * n

    vis = [False] * n
    vis[0] = True
    dep[0] = 1

    idx = [0] * n
    stk = [0]
    while stk:
        i = stk[-1]
        it, x = G[i], idx[i]
        if x < len(it):
            j = it[x]
            idx[i] += 1
            if vis[j]: continue
            vis[j] = True
            dep[j] = dep[i] + 1
            stk.append(j)
            if j == n - 1: break
        else:
            dep[i] = 0
            stk.pop()

    ans = [False] * n
    vis = [False] * n
    mx = 0
    for s in stk:
        if mx == s:
            ans[s] = True
        q = [s]
        for i in q:
            for j in G[i]:
                if dep[j]:
                    if dep[j] > dep[mx]:
                        mx = j
                elif not vis[j]:
                    vis[j] = True
                    q.append(j)
    ans = [i + 1 for i, v in enumerate(ans) if v]
    print(len(ans))
    print(*ans)
main()