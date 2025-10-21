def main():
    from sys import stdin
    e = stdin.readline

    def merge(i):
        h = bl - i.bit_length()
        r = 1 << h
        mid = (i << h) + (r >> 1) - m
        le, ri = i << 1, i << 1 | 1
        pre[i], suf[i] = pre[le], suf[ri]
        zkw[i] = max(zkw[le] & -2, zkw[ri] & -2)
        if mid < n and l[mid - 1] == l[mid]:
            if zkw[le] & zkw[ri] & 1:
                zkw[i] = r << 1 | 1
                pre[i] = suf[i] = r
            else:
                zkw[i] = max(zkw[i], suf[le] + pre[ri] << 1)
                if zkw[le] & 1:
                    pre[i] = pre[ri] + (r >> 1)
                if zkw[ri] & 1:
                    suf[i] = suf[le] + (r >> 1)

    l = list(map(int, e().rstrip()))
    n = len(l)
    m = 1 << n.bit_length()
    bl = m.bit_length()
    zkw = [0] * (m << 1)
    pre = [0] * (m << 1)
    suf = [0] * (m << 1)
    zkw[m:m+n] = [3] * n
    pre[m:m+n] = suf[m:m+n] = [1] * n
    for i in range(m - 1, 0, -1):
        merge(i)

    e()
    ans = []
    for i in map(int, e().split()):
        i -= 1
        l[i] ^= 1
        i |= m
        while i > 1:
            i >>= 1
            merge(i)
        ans.append(zkw[1] >> 1)
    print(*ans)
main()