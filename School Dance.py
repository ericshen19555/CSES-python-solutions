def main():
    from sys import stdin
    e = stdin.readline

    n, m, k = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)

    def dfs(i):
        nonlocal ans
        for j in G[i]:
            if vis[j]: continue
            vis[j] = True
            if pair[j] == -1 or dfs(pair[j]):
                pair[j] = i
                return True
        return False

    ans = 0
    pair = [-1] * m
    for i in range(n):
        vis = [False] * m
        ans += dfs(i)
    print(ans)
    print("\n".join(f"{pair[j] + 1} {j + 1}" for j in range(m)))
main()