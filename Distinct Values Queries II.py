def main():
    from sys import stdin
    from bisect import bisect_left
    from collections import defaultdict
    e = stdin.readline
    LOAD = 1000

    def SortedList():
        return [[-1, n]], [n]

    def expand(sl, mx, i):
        if len(sl[i]) > LOAD << 1:
            chunk = sl[i]
            sl.insert(i + 1, chunk[LOAD:])
            mx.insert(i + 1, chunk[-1])
            del chunk[LOAD:]
            mx[i] = chunk[-1]

    def add(sl, mx, v):
        i = bisect_left(mx, v)
        chunk = sl[i]
        j = bisect_left(chunk, v)
        if j:
            pv = chunk[j - 1]
        else:
            pv = sl[i - 1][-1]
        update(v, pv)
        if j < len(chunk):
            nv = chunk[j]
        else:
            nv = sl[i + 1][0]
        if nv < n:
            update(nv, v)
        chunk.insert(j, v)
        mx[i] = chunk[-1]
        expand(sl, mx, i)

    def remove(sl, mx, v):
        i = bisect_left(mx, v)
        chunk = sl[i]
        j = bisect_left(chunk, v)
        del chunk[j]
        if j < len(chunk):
            nv = chunk[j]
        else:
            nv = sl[i + 1][0]
        if nv < n:
            update(nv, zkw[n + v])
        if len(chunk) >= LOAD >> 1:
            mx[i] = chunk[-1]
        elif len(sl) > 1:
            if i: i -= 1
            sl[i] += chunk
            mx[i] = chunk[-1]
            del sl[i + 1]
            del mx[i + 1]
            expand(sl, mx, i)
        else:
            mx[i] = chunk[-1]

    def merge(i):
        zkw[i] = max(zkw[i << 1], zkw[i << 1 | 1])

    def update(i, v):
        i += n
        zkw[i] = v
        while i > 1:
            i >>= 1
            merge(i)

    n, q = map(int, e().split())
    l = list(map(int, e().split()))
    mp = defaultdict(SortedList)
    zkw = [-1] * (n << 1)
    for i in range(n):
        v = l[i]
        sl, mx = mp[v]
        chunk = sl[-1]
        pi = chunk[-2]
        update(i, pi)
        chunk.insert(-1, i)
        expand(sl, mx, len(sl) - 1)

    ans = []
    for _ in range(q):
        o, a, b = map(int, e().split())
        a -= 1
        if o == 1:
            i, nv = a, b
            v = l[i]
            l[i] = nv
            remove(*mp[v], i)
            add(*mp[nv], i)
        else:
            s, t = a + n, b + n
            while s < t:
                if s & 1:
                    if zkw[s] >= a:
                        ans.append("NO")
                        break
                    s += 1
                if t & 1:
                    t -= 1
                    if zkw[t] >= a:
                        ans.append("NO")
                        break
                s >>= 1
                t >>= 1
            else:
                ans.append("YES")
                continue
    print("\n".join(ans))
main()