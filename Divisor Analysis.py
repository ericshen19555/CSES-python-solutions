def main():
    from sys import stdin
    e = stdin.readline
    mod = 10**9 + 7

    n = 1
    cnt = cnt2 = tot = 1
    sqrt = 1
    for _ in range(int(e())):
        p, c = map(int, e().split())
        p_c = pow(p, c, mod)
        n = n * p_c % mod
        sqrt = sqrt * pow(p, c >> 1, mod) % mod
        cnt = cnt * (c + 1) % mod
        cnt2 = cnt2 * (c + 1) % (2 * (mod - 1))
        tot = tot * (p_c * p - 1) * pow(p - 1, -1, mod) % mod
    mul = pow(n, (cnt2 >> 1 % (mod - 1)), mod) * (sqrt if cnt2 & 1 else 1) % mod
    print(cnt, tot, mul)
main()
