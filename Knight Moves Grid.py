def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    area = n * n
    ans = [[None] * n for _ in range(n)]
    ans[0][0] = 0
    q = [None] * area
    q[0] = (0, 0)
    qi = 1
    d = ((1, 2), (2, 1), (1, -2), (-2, 1), (-1, 2), (2, -1), (-1, -2), (-2, -1))
    for i, j in q:
        nv = ans[i][j] + 1
        for ni, nj in d:
            ni += i; nj += j
            if not 0 <= ni < n or not 0 <= nj < n: continue
            if ans[ni][nj] is not None: continue
            ans[ni][nj] = nv
            q[qi] = (ni, nj)
            qi += 1
            if qi == area: break
        else: continue
        break
    print("\n".join(" ".join(map(str, row)) for row in ans))
main()