def main():
    from sys import stdin
    e = stdin.readline
    mod = 10**9 + 7

    n = int(e())
    ans = 0
    for i in range(2, n + 1):
        ans = (i * ans + (-1 if i & 1 else 1)) % mod
    print(ans)
main()