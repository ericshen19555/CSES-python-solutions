def main():
    from sys import stdin
    e = stdin.readline

    def add(i, v):
        i += 1
        while i <= hi:
            bit[i] += v
            i += i & -i

    def que(s, t):
        s, t = max(0, s), t + 1
        res = 0
        while t > s:
            res += bit[t]
            t &= t-1
        while s > t:
            res -= bit[s]
            s &= s-1
        return res

    n, lo, hi = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        G[b].append(a)

    done = [False] * n
    pa = [-1] * n
    siz = [0] * n
    bit = [0] * (hi + 1)  # bit
    dep = [0] * n

    ans = 0

    # centroid decomposition
    cd = [0]
    for s in cd:
        # count tree size
        q = [s]
        pa[s] = -1
        for i in q:
            p = pa[i]
            siz[i] = 1
            dep[i] = hi
            for j in G[i]:
                if j == p or done[j]: continue
                pa[j] = i
                q.append(j)
        for i in reversed(q):
            if i == s: continue
            siz[pa[i]] += siz[i]

        # find centroid
        half = siz[s] >> 1
        i = s
        while True:
            p = pa[i]
            for j in G[i]:
                if j == p or done[j]: continue
                if siz[j] > half:
                    i = j
                    break
            else:
                c = i
                break

        add(0, 1)

        # update ans
        for s in G[c]:
            if done[s]: continue

            # update count
            stk = [s]
            dep[s] = 1
            pa[s] = c
            while stk:
                i = stk.pop()
                p, d = pa[i], dep[i]
                ans += que(lo - d, hi - d)
                if d == hi: continue
                nd = d + 1
                for j in G[i]:
                    if j == p or done[j]: continue
                    pa[j], dep[j] = i, nd
                    stk.append(j)

            # update ans
            stk = [s]
            while stk:
                i = stk.pop()
                p, d = pa[i], dep[i]
                add(d, 1)
                if d == hi: continue
                for j in G[i]:
                    if j == p or done[j]: continue
                    stk.append(j)

        # reset count
        for i in range(1, hi + 1):
            v = bit[i]
            if not v: break
            while i <= hi:
                bit[i] -= v
                i += i & -i

        # recursion
        done[c] = True
        for j in G[c]:
            if not done[j]:
                cd.append(j)

    print(ans)
main()