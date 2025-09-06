def main():
    from sys import stdin
    mod = 10**9 + 7
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        indeg[b] += 1

    dp = [0] * n
    dp[0] = 1
    q = [i for i, v in enumerate(indeg) if v == 0]
    for i in q:
        x = dp[i] % mod
        for j in G[i]:
            dp[j] += x
            indeg[j] -= 1
            if indeg[j] == 0:
                q.append(j)
    print(dp[n-1] % mod)
main()