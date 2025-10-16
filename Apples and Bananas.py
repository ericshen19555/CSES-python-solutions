def main():
    from sys import stdin
    import cmath
    e = stdin.readline

    def fft(l, inv):
        n = len(l)
        for i in range(n):
            if i < (j := rev_bit[i]):
                l[i], l[j] = l[j], l[i]
        b = 1
        while b < n:
            wn = cmath.exp(inv * 1j * cmath.pi / b)
            for i in range(0, n, b * 2):
                w = 1
                for j in range(i, i + b):
                    x, y = l[j + 0], l[j + b] * w
                    l[j + 0] = x + y
                    l[j + b] = x - y
                    w *= wn
            b <<= 1
        if inv == -1:
            for i in range(n):
                l[i] /= n

    k, n, m = map(int, e().split())
    lim = 1 << k.bit_length() + 1  # min 2^x > 2k
    rev_bit = [0] * lim
    for i in range(1, lim):
        rev_bit[i] = rev_bit[i >> 1] >> 1 | (i & 1) * (lim >> 1)

    a = [0] * lim
    b = [0] * lim
    for v in map(int, e().split()):
        a[v] += 1
    for v in map(int, e().split()):
        b[v] += 1
    fft(a, 1)
    fft(b, 1)
    for i in range(lim):
        a[i] *= b[i]
    fft(a, -1)
    print(*[round(v.real) for v in a[2:2*k+1]])
main()