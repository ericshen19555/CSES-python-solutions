# O((n + q) log n log C)
# TODO: O(n log n + q log C)
# https://cses.fi/problemset/hack/2184/entry/13577433/

def main():
    from sys import stdin
    e = stdin.readline
    inf = float("INF")
    lg = lambda x: x.bit_length() - 1

    n, q = map(int, e().split())
    l = list(map(int, e().split()))
    bl = max(l).bit_length()
    zkw = [[inf] * (n << 1) for _ in range(bl)]
    pre = [[0] * (n + 1) for _ in range(bl)]
    for i in range(n):
        v = l[i]
        k = lg(v)
        zkw[k][i + n] = pre[k][i + 1] = v
    for k in range(bl):
        row = pre[k]
        for i in range(1, n + 1):
            row[i] += row[i - 1]
        row = zkw[k]
        for i in range(n-1, 0, -1):
            row[i] = min(row[i << 1], row[i << 1 | 1])

    ans = []
    for _ in range(q):
        s, t = map(int, e().split())
        s -= 1
        target = lim = 1
        for k in range(bl):
            lim <<= 1
            if target < lim:
                row = zkw[k]
                ss, tt = s + n, t + n
                while ss < tt:
                    if ss & 1:
                        if row[ss] <= target:
                            break
                        ss += 1
                    if tt & 1:
                        tt -= 1
                        if row[tt] <= target:
                            break
                    ss >>= 1
                    tt >>= 1
                else:
                    break
            target += pre[k][t] - pre[k][s]
        ans.append(target)
    print("\n".join(map(str, ans)))
main()
