def main():
    n = 8
    k = int(input())

    dd = ((0, -1), (-1, 0), (0, 1), (1, 0))
    ans = 0
    for I in range(n >> 1):
        for J in range(n >> 1):
            d = [[0] * n for _ in range(n)]
            d[I][J] = 1
            for _ in range(k):
                p = [[0] * n for _ in range(n)]
                for i in range(n):
                    for j in range(n):
                        cnt = 0
                        for di, dj in dd:
                            ni, nj = i + di, j + dj
                            if not (0 <= ni < n and 0 <= nj < n): continue
                            cnt += 1
                            p[i][j] += d[ni][nj]
                        p[i][j] /= cnt
                d = p
            x = 1
            for i in range(n):
                for j in range(n):
                    x *= 1 - d[i][j]
            ans += x
    print(f"{ans * 4:.6f}")
main()