def main():
    from sys import stdin
    e = stdin.readline

    def build(pos, s, t):
        if s + 1 == t:
            tr[pos] = l[s]
        else:
            mid = (s + t) >> 1
            build(pos << 1, s, mid)
            build(pos << 1 | 1, mid, t)
            tr[pos] = max(tr[pos << 1], tr[pos << 1 | 1])

    n, q = map(int, e().split())
    l = list(map(int, e().split()))
    tr = [0] * (n * 3 + 5)
    build(1, 0, n)

    ans = []
    for v in map(int, e().split()):
        if v > tr[1]:
            ans.append(0)
        else:
            pos, s, t = 1, 0, n
            while s + 1 < t:
                mid = (s + t) >> 1
                pos <<= 1
                if tr[pos] >= v:
                    t = mid
                else:
                    pos |= 1
                    s = mid
            tr[pos] -= v
            while pos > 1:
                pos >>= 1
                tr[pos] = max(tr[pos << 1], tr[pos << 1 | 1])
            ans.append(s + 1)
    print(" ".join(map(str, ans)))
main()