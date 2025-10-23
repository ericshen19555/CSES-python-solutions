def main():
    from sys import stdin
    from random import getrandbits
    e = stdin.readline
    SALT = getrandbits(32)
    MASK = (1 << 32) - 1

    def xor_shift(x):
        x ^= x << 13
        x ^= x >> 7
        x ^= x << 17
        x ^= x >> 31
        return x + SALT

    def f():
        pa = [0] * n
        deg = [0] * n
        deg[0] = 2
        for _ in range(n - 1):
            a, b = map(int, e().split())
            a, b = a - 1, b - 1
            pa[a] ^= b
            pa[b] ^= a
            deg[a] += 1
            deg[b] += 1
        h = [1] * n
        for i in range(n):
            while deg[i] == 1:
                deg[i] = 0
                p = pa[i]
                h[p] += xor_shift(h[i]) & MASK
                pa[p] ^= i
                deg[p] -= 1
                i = p
        return h[0] & MASK

    ans = []
    for _ in range(int(e())):
        n = int(e())
        ans.append("YES" if f() == f() else "NO")
    print("\n".join(ans))
main()