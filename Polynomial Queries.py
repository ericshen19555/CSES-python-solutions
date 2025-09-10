def main():
    from sys import stdin
    from itertools import accumulate
    e = stdin.readline

    """
    x = i - j

    (x² + 3x + 2) / 2
    (i² + j² - 2ij + 3i - 3j + 2) / 2
    (i² + (-2j+3)i + (j-1)(j-2)) / 2

    (x + 1)
    (i + (-j+1))
    """

    def add(i, v, fix=0):
        a = v
        b = v * (-2*i + 3)
        c = v * (i-1)*(i-2)
        b -= fix << 1
        c -= fix * (-i + 1) << 1
        while i <= n:
            bit_a[i] += a
            bit_b[i] += b
            bit_c[i] += c
            i += i & -i

    def query(i):
        a = b = c = 0
        x = i
        while i:
            a += bit_a[i]
            b += bit_b[i]
            c += bit_c[i]
            i &= i-1
        return a*x*x + b*x + c >> 1

    n, q = map(int, e().split())
    p = list(accumulate(map(int, e().split()), initial=0))
    bit_a = [0] * (n + 1)
    bit_b = [0] * (n + 1)
    bit_c = [0] * (n + 1)

    ans = []
    for _ in range(q):
        o, s, t = map(int, e().split())
        if o == 1:
            add(s, 1)
            add(t + 1, -1, t - s + 1)
        else:
            ans.append(query(t) - query(s - 1) + p[t] - p[s - 1])
    print("\n".join(map(str, ans)))
main()