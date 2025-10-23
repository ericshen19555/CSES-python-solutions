def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        G[a].append(b)
        G[b].append(a)
    leaves = []
    stk = [(0, -1)]
    while stk:
        i, p = stk.pop()
        if len(G[i]) == 1:
            leaves.append(i + 1)
        for j in G[i]:
            if j != p: stk.append((j, i))
    if len(leaves) & 1:
        leaves.append(leaves[0])
    m = len(leaves)
    print(m >> 1)
    ans = [0] * m
    ans[0:m:2] = leaves[:m >> 1]
    ans[1:m:2] = leaves[m >> 1:]
    print(*ans)
main()