def main():
    from sys import stdin

    m, n = map(int, stdin.readline().split())
    ans = [[0] * n for _ in range(m + 1)]
    n += 1
    l = stdin.read()
    h = [0] * n
    for i in range(0, m * n, n):
        for j in range(n):
            x = i + j
            if l[x] == ".":
                h[j] += 1
            else:
                h[j] = 0
        stk = []
        pv, pj = 0, -1
        for j in range(n):
            v = h[j]
            while pv > v:
                x = pv
                pv, pj = stk.pop()
                w = j - pj
                ans[x][w - 2] += 1
                ans[max(pv, v)][w - 2] -= 1
            if pv != v: stk.append((pv, pj))
            pv, pj = v, j
    for row in ans:
        cur = res = 0
        for j in range(n - 2, -1, -1):
            cur += row[j]
            res += cur
            row[j] = res
    for j in range(n - 1):
        for i in range(m - 1, -1, -1):
            ans[i][j] += ans[i + 1][j]
    for i in range(1, m + 1):
        print(*ans[i])
main()