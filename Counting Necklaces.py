def main():
    from sys import stdin
    from math import gcd
    e = stdin.readline
    mod = 10**9 + 7

    # Burnside’s Lemma
    # 1/n * sum(c(r) for r in 1~n)
    # c(r) = # remain unchanged after k-th rotate

    n, m = map(int, e().split())
    print(pow(n, -1, mod) * sum(pow(m, gcd(r, n), mod) for r in range(n)) % mod)
main()