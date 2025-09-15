def main():
    from sys import stdin
    e = stdin.readline

    def f(n, k):
        if n == 1:
            return 1
        cur = (n + 1) >> 1
        if k <= cur:
            ret = k << 1
            if ret > n: ret %= n
            return ret
        return 2 * f(n >> 1, k - cur) + (1 if n & 1 else -1)

    ans = []
    for _ in range(int(e())):
        ans.append(f(*map(int, e().split())))
    print("\n".join(map(str, ans)))
main()