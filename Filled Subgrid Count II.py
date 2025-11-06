def main():
    from sys import stdin

    n, k = map(int, stdin.readline().split())
    m = n + 1
    l = stdin.read() + "#" * m
    ans = [0] * k
    h = [0] * m
    for i in range(0, n * m, m):
        for j in range(n):
            x = i + j
            if l[x] == l[x - m]:
                h[j] += 1
            else:
                h[j] = 1
        pc = "#"
        stk = []
        pv, pj = 0, -1
        res = 0
        for j in range(m):
            c = l[i + j]
            if pc != c:
                while pv:
                    x = pv
                    pv, pj = stk.pop()
                    w = j - pj
                    res += (x - pv) * w * (w - 1)
                if res: ans[ord(pc) - 65] += res >> 1
                res = 0
                pj = j - 1
                pc = c
            if j == n: break
            v = h[j]
            while pv > v:
                x = pv
                pv, pj = stk.pop()
                w = j - pj
                res += (x - max(v, pv)) * w * (w - 1)
            if pv != v: stk.append((pv, pj))
            pv, pj = v, j
    print(*ans, sep="\n")
main()