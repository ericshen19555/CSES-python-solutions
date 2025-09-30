def main():
    from sys import stdin
    e = stdin.readline

    def add(i, v):
        i += 1
        while i <= k:
            bit[i] += v
            i += i & -i

    n, k = map(int, e().split())
    l = list(map(int, e().split()))
    hb = 1 << n.bit_length() - 1
    cnt = [0] * k
    bit = [0] * (k + 1)

    ans = []
    for i, v in enumerate(l):
        if v < k:
            if cnt[v] == 0:
                add(v, 1)
            cnt[v] += 1
        if i >= k and (p := l[i - k]) < k:
            cnt[p] -= 1
            if cnt[p] == 0:
                add(p, -1)
        if i >= k - 1:
            res = 0
            b = hb
            while b:
                if res + b <= k and bit[res + b] == b:
                    res += b
                b >>= 1
            ans.append(res)
    print(*ans)
main()