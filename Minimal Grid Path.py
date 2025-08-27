def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    grid = [e() for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    rk = [0]
    for k in range(n - 1, -1, -1):
        m = n - k
        cnt = [0] * m
        for i in range(m):
            if rk[i - 1] < rk[i]:
                dp[k + i][n - 1 - i] = 0
                cnt[rk[i - 1]] += 1
            else:
                dp[k + i][n - 1 - i] = 1
                cnt[rk[i]] += 1
        for i in range(1, m):
            cnt[i] += cnt[i - 1]

        temp = [0] * m
        for i in range(m-1, -1, -1):
            key = min(rk[i - 1], rk[i])
            cnt[key] -= 1
            temp[cnt[key]] = i

        cnt = [0] * 26
        for i in range(m):
            i = temp[i]
            cnt[ord(grid[k + i][n - 1 - i]) - 65] += 1
        rk = [m] * (m + 1)
        for i in range(1, 26):
            cnt[i] += cnt[i - 1]
        for i in range(m-1, -1, -1):
            i = temp[i]
            key = ord(grid[k + i][n - 1 - i]) - 65
            cnt[key] -= 1
            rk[i] = cnt[key]

    for k in range(n - 1, 0, -1):
        m = k
        cnt = [0] * m
        for i in range(m):
            if rk[i] < rk[i + 1]:
                dp[i][k - 1 - i] = 0
                cnt[rk[i]] += 1
            else:
                dp[i][k - 1 - i] = 1
                cnt[rk[i + 1]] += 1
        for i in range(1, m):
            cnt[i] += cnt[i - 1]

        temp = [0] * m
        for i in range(m-1, -1, -1):
            key = min(rk[i], rk[i + 1])
            cnt[key] -= 1
            temp[cnt[key]] = i

        cnt = [0] * 26
        for i in range(m):
            i = temp[i]
            cnt[ord(grid[i][k - 1 - i]) - 65] += 1
        rk = [m] * (m + 1)
        for i in range(1, 26):
            cnt[i] += cnt[i - 1]
        for i in range(m-1, -1, -1):
            i = temp[i]
            key = ord(grid[i][k - 1 - i]) - 65
            cnt[key] -= 1
            rk[i] = cnt[key]

    i = j = 0
    ans = []
    for _ in range((n << 1) - 1):
        ans.append(grid[i][j])
        if dp[i][j]:
            i += 1
        else:
            j += 1
    print("".join(ans))
main()