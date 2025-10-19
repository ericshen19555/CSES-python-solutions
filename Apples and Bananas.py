m1 = 469762049
m2 = 998244353
g = 3

def main():
    from sys import stdin
    e = stdin.readline

    def ntt():
        n = lim
        for i in range(n):
            if i < (j := rev_bit[i]):
                a1[i], a1[j] = a1[j], a1[i]
                a2[i], a2[j] = a2[j], a2[i]
                b1[i], b1[j] = b1[j], b1[i]
                b2[i], b2[j] = b2[j], b2[i]
        b = 1
        while b < n:
            wn1 = pow(g, (m1 - 1) // (b * 2), m1)
            wn2 = pow(g, (m2 - 1) // (b * 2), m2)
            for i in range(0, n, b * 2):
                w1 = w2 = 1
                for j in range(i, i + b):
                    x, y = a1[j + 0], a1[j + b] * w1
                    a1[j + 0] = (x + y) % m1
                    a1[j + b] = (x - y) % m1
                    x, y = a2[j + 0], a2[j + b] * w2
                    a2[j + 0] = (x + y) % m2
                    a2[j + b] = (x - y) % m2
                    x, y = b1[j + 0], b1[j + b] * w1
                    b1[j + 0] = (x + y) % m1
                    b1[j + b] = (x - y) % m1
                    x, y = b2[j + 0], b2[j + b] * w2
                    b2[j + 0] = (x + y) % m2
                    b2[j + b] = (x - y) % m2
                    w1 = (w1 * wn1) % m1
                    w2 = (w2 * wn2) % m2
            b <<= 1

    def ntt_inv():
        n = lim
        for i in range(n):
            if i < (j := rev_bit[i]):
                a1[i], a1[j] = a1[j], a1[i]
                a2[i], a2[j] = a2[j], a2[i]
        b = 1
        while b < n:
            wn1 = pow(g, -(m1 - 1) // (b * 2), m1)
            wn2 = pow(g, -(m2 - 1) // (b * 2), m2)
            for i in range(0, n, b * 2):
                w1 = w2 = 1
                for j in range(i, i + b):
                    x, y = a1[j + 0], a1[j + b] * w1
                    a1[j + 0] = (x + y) % m1
                    a1[j + b] = (x - y) % m1
                    x, y = a2[j + 0], a2[j + b] * w2
                    a2[j + 0] = (x + y) % m2
                    a2[j + b] = (x - y) % m2
                    w1 = (w1 * wn1) % m1
                    w2 = (w2 * wn2) % m2
            b <<= 1
        inv_n1 = pow(n, -1, m1)
        inv_n2 = pow(n, -1, m2)
        mm = m1 * m2
        q1 = m1 * pow(m1, -1, m2)
        q2 = m2 * pow(m2, -1, m1)
        for i in range(n):
            r1 = (a1[i] * inv_n1) % m1
            r2 = (a2[i] * inv_n2) % m2
            a1[i] = (r1 * q2 + r2 * q1) % mm

    k, n, m = map(int, e().split())
    lim = 1 << k.bit_length() + 1  # min 2^x > 2k
    rev_bit = [0] * lim
    for i in range(1, lim):
        rev_bit[i] = rev_bit[i >> 1] >> 1 | (i & 1) * (lim >> 1)

    a1 = [0] * lim
    b1 = [0] * lim
    for v in map(int, e().split()):
        a1[v] += 1
    for v in map(int, e().split()):
        b1[v] += 1
    a2, b2 = a1[:], b1[:]
    ntt()
    for i in range(lim):
        a1[i] = (a1[i] * b1[i]) % m1
        a2[i] = (a2[i] * b2[i]) % m2
    ntt_inv()
    print(*a1[2:2*k+1])
main()