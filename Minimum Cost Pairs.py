def main():
    from sys import stdin
    from heapq import heapify, heappop, heappush
    e = stdin.readline

    def encode(v, s, t):
        return v << 40 | s << 20 | t

    def decode(x):
        return x >> 40, (x >> 20) & 0xfffff, x & 0xfffff

    n = int(e())
    l = sorted(map(int, e().split()))
    for i in range(n - 1):
        l[i] = l[i + 1] - l[i]

    ans = [0] * (n >> 1)
    le = list(range(n))
    ri = list(range(n))
    h = [encode(l[i], i, i) for i in range(n)]
    heapify(h)
    cur = 0
    for i in range(n >> 1):
        while True:
            v, s, t = decode(heappop(h))
            if not s == le[s] == le[t]: continue
            if not t == ri[s] == ri[t]: continue
            break
        cur += v
        ans[i] = cur
        if s == n - 1 or t == n - 1: continue
        s, t = le[s - 1], ri[t + 1]
        le[t], ri[s] = s, t
        l[s] = l[t] = v = l[s] + l[t] - v
        heappush(h, encode(v, s, t))
    print(" ".join(map(str, ans)))
main()