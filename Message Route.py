def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    pre = [-1] * n
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        G[b].append(a)

    q = [0]
    pre[0] = 0
    for i in q:
        for j in G[i]:
            if ~pre[j]: continue
            pre[j] = i
            if j == n-1: break
            q.append(j)
        else: continue
        break
    else:
        print("IMPOSSIBLE")
        return

    ans = []
    i = n-1
    while i:
        ans.append(i + 1)
        i = pre[i]
    ans.append(1)
    print(len(ans))
    print(*reversed(ans))
main()