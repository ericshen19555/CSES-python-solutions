def main():
    from sys import stdin

    n, k = map(int, stdin.readline().split())
    m = n + 1
    l = stdin.read() + "#" * m
    ans = [0] * k
    dp = [0] * n
    for i in range(0, n * m, m):
        ul = le = 0
        for j in range(n):
            x = i + j
            up = dp[j]
            le = dp[j] = 1 + (l[x] == l[x-1] == l[x-m] == l[x-m-1] and min(ul, up, le))
            ans[ord(l[x]) - 65] += le
            ul = up
    print(*ans, sep="\n")
main()