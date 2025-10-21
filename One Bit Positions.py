mod = 998244353
g = 3

def main():
    from sys import stdin
    e = stdin.readline

    def ntt(l, inv):
        n = len(l)
        for i in range(n):
            if i < (j := rev_bit[i]):
                l[i], l[j] = l[j], l[i]
        b = 1
        while b < n:
            wn = pow(g, inv * (mod - 1) // (b * 2), mod)
            for i in range(0, n, b * 2):
                w = 1
                for j in range(i, i + b):
                    x, y = l[j + 0], l[j + b] * w
                    l[j + 0] = (x + y) % mod
                    l[j + b] = (x - y) % mod
                    w = (w * wn) % mod
            b <<= 1
        if inv == -1:
            for i in range(n):
                l[i] = (l[i] * inv_n) % mod

    a = list(map(int, e().rstrip()))
    n = len(a)
    lim = 1 << n.bit_length() + 1
    a += [0] * (lim - n)
    b = a[::-1]
    inv_n = pow(lim, -1, mod)
    rev_bit = [0] * lim
    for i in range(1, lim):
        rev_bit[i] = rev_bit[i >> 1] >> 1 | (i & 1) * (lim >> 1)

    ntt(a, 1)
    ntt(b, 1)
    for i in range(lim):
        a[i] = (a[i] * b[i]) % mod
    ntt(a, -1)
    a.reverse()
    print(*a[1:n])
main()