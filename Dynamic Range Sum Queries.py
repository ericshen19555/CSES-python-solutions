def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    l = list(map(int, e().split()))
    bit = [0] + l
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            bit[j] += bit[i]

    ans = []
    for _ in range(q):
        o, a, b = map(int, e().split())
        if o == 1:
            i, v = a - 1, b
            v -= l[i]
            l[i] += v
            i += 1  # bit 1-based
            while i <= n:
                bit[i] += v
                i += i & -i
        else:
            s, t = a - 1, b
            res = 0
            while t > s:
                res += bit[t]
                t &= t-1
            while s > t:
                res -= bit[s]
                s &= s-1
            ans.append(res)
    print("\n".join(map(str, ans)))
main()