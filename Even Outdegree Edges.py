def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        G[a].append(b)
        G[b].append(a)
    for i, it in enumerate(G):
        G[i] = iter(it)

    pa = [-1] * n
    out = [0] * n
    ans = []
    stk = []
    instk = [False] * n
    for i in range(n):
        if ~pa[i]: continue
        pa[i] = i
        stk.append(i)
        instk[i] = True
        while stk:
            i = stk[-1]
            p = pa[i]
            for j in G[i]:
                if j == p: continue
                if instk[j]:
                    o, x = i, i ^ j
                    if out[j]: o ^= x
                    out[o] ^= 1
                    ans.append(f"{o + 1} {(o ^ x) + 1}")
                    continue
                if ~pa[j]: continue
                pa[j] = i
                stk.append(j)
                instk[j] = True
                break
            else:
                o, x = p, p ^ i
                if p == i:
                    if out[i]:
                        print("IMPOSSIBLE")
                        return
                else:
                    if out[i]: o ^= x
                    out[o] ^= 1
                    ans.append(f"{o + 1} {(o ^ x) + 1}")
                stk.pop()
                instk[i] = False
    print(*ans, sep="\n")
main()