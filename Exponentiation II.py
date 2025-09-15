def main():
    from sys import stdin
    e = stdin.readline
    mod = 10**9 + 7

    # a ^ k % m = a ^ (k % phi(m)) % m
    # phi(m) = m - 1 if m is prime

    ans = []
    for _ in range(int(e())):
        a, b, c = map(int, e().split())
        ans.append(pow(a, pow(b, c, mod - 1), mod))
    print("\n".join(map(str, ans)))
main()