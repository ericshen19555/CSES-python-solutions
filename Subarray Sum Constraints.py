def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    n += 1
    G = [[] for _ in range(n)]
    for _ in range(m):
        s, t, v = map(int, e().split())
        s -= 1
        G[s].append((t, v))
        G[t].append((s, -v))

    vis = [False] * n
    ans = [0] * n
    for i in range(n):
        if vis[i]: continue
        q = [i]
        for i in q:
            for j, v in G[i]:
                if vis[j]:
                    if ans[i] + v != ans[j]:
                        return print("NO")
                else:
                    vis[j] = True
                    ans[j] = ans[i] + v
                    q.append(j)
    print("YES")
    for i in range(n - 1, 0, -1):
        ans[i] -= ans[i - 1]
    print(*ans[1:])
main()