def main():
    from sys import stdin
    e = stdin.readline

    m, n = map(int, e().split())
    l = [bytearray(e().encode()) for _ in range(m)]
    siz = m * n << 1
    scc = [-1] * siz
    q = []

    encode = lambda i, j, c: i * n + j << 1 | c
    decode = lambda x: ((x >> 1) // n, (x >> 1) % n, x & 1)
    colors = [1, 2, 0, 2, 0, 1]
    color = lambda c, x: colors[c - 65 << 1 | x]

    def edge(a, b, c, d, e, f):
        if not (0 <= a < m and 0 <= b < n): return False
        if not (0 <= d < m and 0 <= e < n): return False
        return color(l[a][b], c) == color(l[d][e], f ^ 1)

    d = [0, 1, 0, -1]
    for x in range(siz):
        if ~scc[x]: continue
        scc[x] = 0
        stk = [x << 4]
        while stk:
            x = stk.pop()
            if x & 8:
                q.append(x >> 4)
                continue
            stk.append(x + 1)
            x, di, nc = x >> 4, (x >> 1) & 3, x & 1
            i, j, c = decode(x)
            ni, nj = i + d[di], j + d[di ^ 1]
            if not edge(i, j, c, ni, nj, nc): continue
            nx = encode(ni, nj, nc)
            if ~scc[nx]: continue
            scc[nx] = 0
            stk.append(nx << 4)

    scn = 0
    for x in reversed(q):
        if scc[x]: continue
        scn += 1
        scc[x] = scn
        stk = [x]
        while stk:
            x = stk.pop()
            i, j, c = decode(x)
            for nc in range(2):
                for di in range(4):
                    ni, nj = i + d[di], j + d[di ^ 1]
                    if not edge(ni, nj, nc, i, j, c): continue
                    nx = encode(ni, nj, nc)
                    if scc[nx]: continue
                    scc[nx] = scn
                    stk.append(nx)
    if any(scc[x] == scc[x | 1] for x in range(0, siz, 2)):
        print("IMPOSSIBLE")
    else:
        for x in range(0, siz, 2):
            i, j, _ = decode(x)
            l[i][j] = color(l[i][j], scc[x] < scc[x | 1]) + 65
        print("".join(map(bytearray.decode, l)))
main()
