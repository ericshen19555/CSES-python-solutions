def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    pa = [-1] + [int(i) - 1 for i in e().split()]
    indeg = [0] * n
    for i in range(1, n):
        indeg[pa[i]] += 1
    dp = [0] * n
    q = [i for i, v in enumerate(indeg) if v == 0]
    for i in q:
        p = pa[i]
        dp[p] += 1 + dp[i]
        indeg[p] -= 1
        if p and indeg[p] == 0:
            q.append(p)
    print(*dp)
main()