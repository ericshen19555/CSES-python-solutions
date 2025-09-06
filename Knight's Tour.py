def main():
    from sys import stdin
    e = stdin.readline

    n = 8
    area = n * n

    j, i = map(int, e().split())
    i, j = i-1, j-1
    d = (1, 2, 1, -2, -1, 2, -1, -2)
    G = [[ni * n + nj for di in range(8) if 0 <= (ni := i + d[di]) < n and 0 <= (nj := j + d[di ^ 1]) < n] for i in range(n) for j in range(n)]

    def f(i):
        return sum(ans[j] == 0 for j in G[i])

    def bt(i, d):
        ans[i] = d
        if d == n * n:
            return True
        cand = [j for j in G[i] if not ans[j]]
        cand.sort(key=f)
        for j in cand:
            if bt(j, d + 1):
                return True
        ans[i] = 0
        return False

    ans = [0] * area
    bt(i * n + j, 1)
    for r in range(0, area, n):
        print(*ans[r:r+n])
main()
