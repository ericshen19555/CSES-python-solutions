def main():
    from sys import stdin
    from sys import setrecursionlimit
    e = stdin.readline

    setrecursionlimit(10**5 + 10)

    n = int(e())
    pre = [int(v) - 1 for v in e().split()]
    rk = [0] * (n + 1)
    rk[-1] = n
    for i, v in enumerate(map(int, e().split())):
        rk[v - 1] = i

    ans = []

    def dfs(i, p):
        j = next(pre, -1)
        if rk[j] < rk[i]:
            j = dfs(j, i)
        if rk[j] < rk[p]:
            j = dfs(j, p)
        ans.append(i + 1)
        return j

    pre = iter(pre)
    dfs(next(pre), -1)
    print(*ans)
main()