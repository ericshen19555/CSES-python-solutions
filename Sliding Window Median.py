def main():
    from sys import stdin
    e = stdin.readline

    def add(i, v):
        i += 1
        while i <= m:
            bit[i] += v
            i += i & -i

    n, k = map(int, e().split())
    l = list(map(int, e().split()))
    hb = 1 << n.bit_length() - 1
    half = k + 1 >> 1
    sl = sorted(set(l))
    mp = {v: i for i, v in enumerate(sl)}
    m = len(mp)
    bit = [0] * (m + 1)

    ans = []
    for i in range(n):
        add(mp[l[i]], 1)
        if i >= k:
            add(mp[l[i - k]], -1)
        if i >= k - 1:
            idx = cur = 0
            b = hb
            while b:
                if idx + b <= m and cur + bit[idx + b] < half:
                    idx += b
                    cur += bit[idx]
                b >>= 1
            ans.append(sl[idx])
    print(*ans)
main()