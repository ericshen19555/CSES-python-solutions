def main():
    from sys import stdin
    from itertools import count
    e = stdin.readline

    lim = 1223
    dp = [0] * lim
    for i in range(3, lim):
        u = {dp[j] ^ dp[i - j] for j in range(1, i + 1 >> 1)}
        dp[i] = next(j for j in count() if j not in u)

    ans = []
    for _ in range(int(e())):
        n = int(e())
        ans.append("first" if n >= lim or dp[n] else "second")
    print("\n".join(ans))
main()