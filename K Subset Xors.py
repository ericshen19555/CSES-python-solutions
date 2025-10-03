def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    l = list(map(int, e().split()))
    bl = max(l).bit_length()

    m = 0
    basis = [0] * bl
    for v in l:
        for s in reversed(range(bl)):
            if (v >> s) & 1 == 0: continue
            if not basis[s]:
                m += 1
                basis[s] = v
                break
            v ^= basis[s]

    def dfs(x, s, cur):
        if cur >= lo:
            cand.append(x)
            return
        if basis[s]:
            dfs(x, s + 1, cur << 1)
            dfs(x ^ basis[s], s + 1, cur << 1)
        else:
            dfs(x, s + 1, cur)

    r = min(19, n - m)
    lo = (k - 1 + (1 << r)) >> r
    cand = []
    dfs(0, 0, 1)
    cand.sort()
    ans = []
    for v in cand:
        ans += [v] * (1 << r)
        if len(ans) >= k: break
    print(*ans[:k])
main()