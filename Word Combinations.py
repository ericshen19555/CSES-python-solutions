def main():
    from sys import stdin
    e = stdin.readline
    mod = 10**9 + 7

    s = e().rstrip()
    n = len(s)

    k = int(e())
    trie = [[0] * 27 for _ in range(10**6 + 1)]
    cnt = 1
    for _ in range(k):
        t = e().rstrip()
        o = 0
        for c in t:
            c = ord(c) - 97
            if not trie[o][c]:
                trie[o][c] = cnt
                cnt += 1
            o = trie[o][c]
        trie[o][-1] = True

    dp = [0] * (n + 1)
    dp[-1] = 1
    for i in range(n):
        x = dp[i - 1] % mod
        if not x: continue
        o = 0
        for j in range(i, n):
            o = trie[o][ord(s[j]) - 97]
            if not o: break
            if trie[o][-1]: dp[j] += x
    print(dp[n - 1] % mod)
main()