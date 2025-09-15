def main():
    mod = 10**9 + 7

    # sum i:1~n sigma(i) = sum d:1~n d*floor(n/d)

    n = int(input())
    ans = 0
    le, ri = 1, 0  # [le, ri]
    while le <= n:
        ri = n // (n // le)
        ans += (le + ri) * (ri - le + 1) * (n // le) >> 1
        le = ri + 1
    print(ans % mod)
main()