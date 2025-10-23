def main():
    from sys import stdin
    e = stdin.readline

    def find(x):
        if dsu[x] < 0: return x
        dsu[x] = find(dsu[x])
        return dsu[x]

    def merge(a, b):
        a, b = find(a), find(b)
        if a == b: return False
        if dsu[a] > dsu[b]: a, b = b, a
        dsu[a] += dsu[b]
        dsu[b] = a
        return True

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    indeg = [0] * n
    dsu = [-1] * n
    ans = n
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        G[a].append(b)
        indeg[b] += 1
        merge(a, b)

    q = [i for i, v in enumerate(indeg) if v == 0]
    for i in q:
        r = find(i)
        dsu[r] += 1
        if dsu[r] == 0: ans -= 1
        for j in G[i]:
            indeg[j] -= 1
            if indeg[j] == 0:
                q.append(j)
    print(ans)
main()