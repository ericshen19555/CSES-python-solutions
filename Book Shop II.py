# bounded knapsack problem - monotonic deque - O(nm)

def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    m += 1

    ws = list(map(int, e().split()))  # weight
    vs = list(map(int, e().split()))  # value
    cs = list(map(int, e().split()))  # number
    p = [0] * m
    q = [0] * m
    for i in range(n):
        v, w, c = vs[i], ws[i], cs[i]
        d = p[:]
        for r in range(w):
            h, t = 0, -1
            for i in range(r, m, w):
                if h <= t and q[h] < i - w * c: h += 1
                if h <= t: p[i] = max(p[i], d[q[h]] + (i - q[h]) // w * v)
                while h <= t and d[i] >= d[q[t]] + (i - q[t]) // w * v: t -= 1
                t += 1
                q[t] = i
    print(p[-1])
main()